import os
import base64
import io
import httpx
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

app = FastAPI()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
GEMINI_MODEL = "gemini-3.1-flash-image-preview"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"


def resize_image(image_bytes: bytes, max_px: int = 1024) -> bytes:
    from PIL import ImageOps
    img = Image.open(io.BytesIO(image_bytes))
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")
    img.thumbnail((max_px, max_px), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    return buf.getvalue()


PROMPTS = {
    "watercolor": (
        "Transform this photo into a Japanese watercolor painting. "
        "Use soft watercolor washes, delicate brushwork, gentle bleeding of colors, "
        "and subtle paper texture. Preserve the subjects and composition. "
        "In the bottom right corner, slightly indented from the edges, add the text 'MCC' "
        "in large bold light green lettering."
    ),
    "anime": (
        "Transform this photo into a Japanese anime illustration. "
        "Use clean outlines, vibrant flat colors, cel-shading, and classic anime aesthetics. "
        "Preserve the subjects and composition. "
        "In the bottom right corner, slightly indented from the edges, add the text 'MCC' "
        "in large bold light green lettering."
    ),
}


@app.post("/api/cartoonify")
async def cartoonify(file: UploadFile = File(...), style: str = Form("watercolor")):
    if not GOOGLE_API_KEY:
        raise HTTPException(500, "GOOGLE_API_KEY not configured")

    raw = await file.read()
    resized = resize_image(raw)
    b64 = base64.b64encode(resized).decode()

    prompt = PROMPTS.get(style, PROMPTS["watercolor"])
    result_b64, mime = await generate_image(b64, prompt)
    return JSONResponse({"image": f"data:{mime};base64,{result_b64}"})


async def generate_image(image_b64: str, prompt: str) -> tuple[str, str]:
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            GEMINI_URL,
            params={"key": GOOGLE_API_KEY},
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{
                    "parts": [
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_b64,
                            }
                        },
                        {"text": prompt},
                    ]
                }],
                "generationConfig": {
                    "responseModalities": ["IMAGE", "TEXT"],
                },
            },
        )
        if not resp.is_success:
            print("Gemini error:", resp.status_code, resp.text)
        resp.raise_for_status()

        parts = resp.json()["candidates"][0]["content"]["parts"]
        for part in parts:
            if "inlineData" in part:
                return part["inlineData"]["data"], part["inlineData"]["mimeType"]

        raise HTTPException(500, "No image returned")


app.mount("/", StaticFiles(directory="static", html=True), name="static")
