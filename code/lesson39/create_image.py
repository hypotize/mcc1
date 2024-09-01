from PIL import Image, ImageDraw, ImageFont
import os

def create_image_files(text_file):
    # ディレクトリの作成
    if not os.path.exists('image'):
        os.makedirs('image')

    # フォントの設定
    font_path = "ipaexg.ttf"
    font_size = 48
    font = ImageFont.truetype(font_path, font_size)

    with open(text_file, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')

    for i, paragraph in enumerate(paragraphs):
        # 画像の作成
        img = Image.new('RGB', (1920, 1080), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(paragraph, font=font)
        position = ((1920 - text_width) // 2, (1080 - text_height) // 2)
        draw.text(position, paragraph, font=font, fill=(0, 0, 0))

        # 画像ファイルの保存
        img.save(f'image/{i}.png')

if __name__ == "__main__":
    create_image_files('せつめい.txt')
