import sys
from PIL import Image

# 画像ファイル名を取得
if len(sys.argv) < 2:
    print("画像ファイル名を指定してください")
    sys.exit()
filename = sys.argv[1]

# 画像を開く
image = Image.open(filename)

# 画像をRGBAモードに変換する
image = image.convert("RGBA")

# 画像のピクセルデータを取得する
pixel_data = image.load()

# 画像の幅と高さを取得する
width, height = image.size

# 画像のピクセルをイテレーションして、背景色（ここでは白）を透明にする
for y in range(height):
    for x in range(width):
        r, g, b, a = pixel_data[x, y]
        if (r, g, b) == (255, 255, 255):  # 白色の場合
            pixel_data[x, y] = (r, g, b, 0)  # アルファ値を0にする

# 透明になった画像を保存する
image.save(filename)
