from PIL import Image, ImageDraw

# 画像サイズを指定
width = 500
height = 500

# 画像を作成
img = Image.new('RGB', (width, height), (255, 255, 255))

# ImageDrawオブジェクトを作成して、画像に四角形を描画
draw = ImageDraw.Draw(img)
draw.rectangle((100, 100, 400, 400), outline=(0, 0, 0), width=5)

# 画像を保存
img.save('example.png')
