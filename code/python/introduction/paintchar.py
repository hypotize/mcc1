import pygame
import sys
import os
from pygame.locals import *
import random
import math
import datetime
import tkinter as tk
import tkinter.filedialog
from PIL import Image

# 機能拡張の概要
# ・ 描画時の指定色が分かりやすい用に、アイコンを色アイコン（円形）に変更
# ・ 描画時に右クリックすると、クリックされた位置の色の領域を指定色で塗りつぶす(fill機能)
# ・ oキーでセーブした画像を読み込む機能(open機能）
# ・ uキーで各処理ごとにundoする機能(undo機能、但しredo機能はなし）
# ・ iキーを押すといつでも初期状態に戻る機能(initialize機能）
# ・ pキーでcut/copy and pasteモードに移行（クロスアイコンに変更）もう一度押すと
#	・ マウスボタンを押した状態から放すまでで領域を選択
#	・ 領域選択状態でxキーを押すと選択領域をカットして、クリップボードに格納（矢印アイコンに変更し領域も表示）
#	・ 領域選択状態でcキー押すと選択領域をカットせず、クリップボードに格納（矢印アイコンに変更し領域も表示）
#	・ クリップボード格納状態でマウスを左クリックすると表示領域ににクリップボードの内容をコピーする
#	・ マウスボタンを右クリックするとクリップボードの内容が削除され、領域選択モード（クロスアイコン）に戻る
#	・ pキーをもう一度押すといつでも通常モードに戻る（クリップボードも削除）

# いろをいくつか定義
colors = ((0, 0, 0),		# 0: 黒
		  (0, 0, 128),		# 1: 海軍
		  (128, 0, 0),		# 2: あずき色
		  (0, 128, 0),		# 3: 緑
		  (162, 82, 45),	# 4: シエナ
		  (128, 128, 128),	# 5: グレー
		  (192,192,192),	# 6: 銀
		  (255, 255, 255),	# 7: 白
		  (255, 0, 0),	   	# 8: 赤
		  (255, 165, 0),	# 9: オレンジ
		  (255, 255, 0),	# a: 黄
		  (0, 255, 0),	   	# b: ライム
		  (0, 191, 255),	# c: ディープスカイブルー
		  (147, 112, 219),	# d: ミディアムパープル
		  (255, 105, 180),	# e: ホトピンク
		  (255, 228, 196),	# f: ビスク
		  )

WHITE = 7	# 白の色番号
BLACK = 0	# 黒の色番号

CP_MODE_NONE = 0		#通常描画モード
CP_MODE_UNSELECT = 1	#座標未選択
CP_MODE_SELECTED = 2	#座標選択済み
CP_MODE_AREA = 3		#領域選択済み
CP_MODE_CLIPPED = 4		#クリープボード格納済

#最初のペンキのいろ
color = BLACK

# 設定色の合わせてカーソル（円）の色を変更
def set_cursor():
	surf = pygame.Surface((40, 40), pygame.SRCALPHA) # you could also load an image 
	surf.fill((255, 255, 255, 0))
	pygame.draw.circle(surf, colors[color], (20, 20), 6)
	if colors[color][0] + colors[color][1] + colors[color][2] < 256:	#濃い色の時は輪郭を白(7)に
		pygame.draw.circle(surf, colors[7], (20, 20), 6, width=1)
	else:	#薄い色は輪郭を黒(0)に
		pygame.draw.circle(surf, colors[0], (20, 20), 6, width=1)
	cursor = pygame.cursors.Cursor((20, 20), surf)
	pygame.mouse.set_cursor(cursor)

#一個の箱の大きさ(ピクセル)
block_size = 20
#箱の数(一辺) 
matrix_size = 16

# 最初は全部白にする
mtrx =	[[WHITE] * matrix_size for i in range(matrix_size)]

# ファイルオープン用のダイアログ
def dialog(isOpen):
	# ルートウィンドウ作成
	root = tk.Tk()
	# ルートウィンドウの非表示
	root.withdraw()

	# ファイル選択
	iDir = os.path.abspath(os.path.dirname(__file__))
	filetypes = [("画像ファイル", ".png")]
	filename = tkinter.filedialog.askopenfilename(filetypes=filetypes, title="ファイルを開く", initialdir=iDir) if isOpen else tkinter.filedialog.asksaveasfilename(filetypes=filetypes, title="ファイルを書き込む", initialdir=iDir, defaultextension="png")
	root.destroy()
	return filename

# 画像ファイルをオープンして、箱を復元する
def openfile(filename):
	image = Image.open(filename)
	width, height = image.size
	# 画像の幅と高さが合っていなければエラー
	if width != matrix_size or height != matrix_size:
		print("invalid png file!")
		return False
	for y in range(0, matrix_size):
		for x in range(0, matrix_size):
			pixel = image.getpixel((x, y))
			min_diff = float("inf")
			min_color = -1
			# pixelの値がカラーパレットの値に一番近いカラー番号に変換する
			for i, color in enumerate(colors):
				diff = (pixel[0]-color[0])**2 + (pixel[1]-color[1])**2 + (pixel[2]-color[2])**2
				if diff < min_diff:
					min_diff = diff
					min_color = i
			mtrx[y][x] = min_color
	return True

# undo用配列（この中に配列として[(row, col, color)...]を入れる）
undo_buf = []

# undo の実行
def undo():
	if len(undo_buf) > 0:
		buf = undo_buf.pop()	# 1回分戻す
		while len(buf) > 0:		# 1回分の描画処理の座標と値の配列をまとめて処理
			col, row, c = buf.pop()
			mtrx[row][col] = c
			
# 塗りつぶして、塗りつぶす前の位置と値のundo用配列を返す
def fill(col, row, old_color, new_color):
	buf = []	# 戻り値のundo用バッファ
	if mtrx[row][col] != old_color:	# 座標が塗りつぶし対象の色でなければ終了
		return buf
	buf.append((col, row, mtrx[row][col]))	# 元の座標値をundo用配列に追加
	mtrx[row][col] = new_color
	# 上下左右を再帰的に塗りつぶす
	if col > 0:
		buf.extend(fill(col-1, row, old_color, new_color))
	if col < matrix_size-1:
		buf.extend(fill(col+1, row, old_color, new_color))
	if row > 0:
		buf.extend(fill(col, row-1, old_color, new_color))
	if row < matrix_size-1:
		buf.extend(fill(col, row+1, old_color, new_color))
	return buf

# 箱を全部書いていく
def draw():
	global cp_pos
	screen.fill((224,224,224))
	y = block_size * matrix_size + pallet_size - block_size
	for i, c in enumerate(colors):
		x = block_size * i
		pygame.draw.rect(screen, c, [x, y, block_size, block_size], 0)
		pallet_image = pallet_font.render("{:x}".format(i), True, (0,0,0))
		screen.blit(pallet_image, (x+5,y-block_size+5))
	for i in range(matrix_size):
		for j in range(matrix_size):
			val = mtrx[j][i]
			pygame.draw.rect(screen,colors[val],[i * block_size, j * block_size, block_size,block_size], 0)
	if cp_mode == CP_MODE_CLIPPED:
		col = round(cp_pos[0] / block_size)
		row = round(cp_pos[1] / block_size)
		width = cp_pos[4]
		height = cp_pos[5]
		for r in range(height):
			for c in range(width):
				i = c + col
				j = r + row
				if j < matrix_size and i < matrix_size:
					val = cp_buf[r][c]
					if val != 7:
						pygame.draw.rect(screen, cp_colors[val], [i * block_size, j * block_size, block_size, block_size], 0)
					
	if cp_mode in [CP_MODE_SELECTED, CP_MODE_AREA, CP_MODE_CLIPPED]:
		pygame.draw.rect(screen, (192, 192, 192), [cp_pos[0], cp_pos[1], cp_pos[2], cp_pos[3]], width=1)
			
	for i in range(matrix_size):
		pygame.draw.line(screen, (0,0,0), (0, i * block_size), (matrix_size * block_size, i * block_size))
		pygame.draw.line(screen, (0,0,0), (i * block_size, 0), (i * block_size, matrix_size * block_size))

pallet_size	= 40


pygame.init()
screen = pygame.display.set_mode([block_size * matrix_size, block_size * matrix_size + pallet_size], pygame.SRCALPHA)
pygame.display.set_caption("Character Paint")
pallet_font = pygame.font.Font("ipaexg.ttf", 12)

done = False
clock = pygame.time.Clock()

set_cursor()

cp_mode = CP_MODE_NONE		# cut/copy and paste mode
cp_pos = None				# cut/copy 選択位置／矩形領域
cp_buf = None				# cut/copy 矩形領域の元画像を格納するクリップボード

cp_colors = []
for r, g, b in colors:
	r = 128 if r == 0 else 255
	g = 128 if g == 0 else 255
	b = 128 if b == 0 else 255
	cp_colors.append((r, g, b, 0))
	

def get_cp_area(pos):	# cut/copyの選択領域を矩形の線で表示し、左上の位置を返す
	minx = min(pos[0], cp_pos[0])
	miny = min(pos[1], cp_pos[1])
	maxx = max(pos[0], cp_pos[0])
	maxy = max(pos[1], cp_pos[1])
	return (minx, miny, maxx-minx, maxy-miny)
	
def clipboard(cut):
	global cp_buf, cp_pos, mtrx, undo_buf
	col = round(cp_pos[0] / block_size)
	row = round(cp_pos[1] / block_size)
	width = round((cp_pos[0] + cp_pos[2]) / block_size) - col + 1
	height = round((cp_pos[1] + cp_pos[3]) / block_size) - row + 1
	cp_pos = (cp_pos[0], cp_pos[1], cp_pos[2], cp_pos[3], width, height)
	cp_buf = [[mtrx[r][c] for c in range(col, col+width)] for r in range(row, row+height)]
	if cut:
		buf = []
		for r in range(row, row+height):
			for c in range(col, col+width):
				buf.append((c, r, mtrx[r][c]))
				mtrx[r][c] = WHITE
		undo_buf.append(buf)	# cutしても戻せるようにundoバッファに格納
		
# -------- Main Program Loop -----------
while not done:

	#イベント処理
	had_event = False
	for event in pygame.event.get():
		had_event = True

		#画面を閉じるボタン
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		#キーが押されたとき
		if event.type == KEYDOWN:
			
			#終了
			if event.key == K_q or event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if cp_mode == CP_MODE_NONE:	# cut/copy and pasteモードの時は描画系の処理は無効
				# s で保存
				if event.key == K_s:
					filename = dialog(False)
					if filename != "":
						# 16x16のpngイメージで保存する
						img = pygame.Surface((matrix_size, matrix_size));
						for y in range(0, matrix_size):
							for x in range(0, matrix_size):
								img.set_at((x, y), colors[mtrx[y][x]])
						pygame.image.save(img ,filename)
						print(filename, "で保存しました。")
				# o で読み込み
				if event.key == K_o:
					filename = dialog(True)
					if filename != "":
						if openfile(filename):
							print(filename, "を読み込みました。")
						undo_buf.clear()
			# i で画面と状態を全て初期化
			if event.key == K_i:
				cp_mode = CP_MODE_NONE
				cp_pos = None
				cp_buf = None
				color = BLACK
				set_cursor()
				undo_buf.clear()
				mtrx =	[[WHITE] * matrix_size for i in range(matrix_size)]
			# u でundo
			if event.key == K_u:
				undo()
			# p でcut/copy and paste モードと通常モードの切り替え
			if event.key == K_p:
				cp_pos = None
				cp_buf = None
				if cp_mode != CP_MODE_NONE:
					cp_mode = CP_MODE_NONE
					set_cursor()
				else:
					cp_mode = CP_MODE_UNSELECT
					# カーソルをcut/copy 領域設定用のクロスマークに変更
					cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
					pygame.mouse.set_cursor(cursor)
			# cut/copy and paste モードのとき x でcutしてクリップボードにコピー
			if cp_mode == CP_MODE_AREA and event.key == K_x:
				clipboard(True)
				cp_mode = CP_MODE_CLIPPED
				# クリップボードに格納したらpaste用の矢印アイコンに変更
				pygame.mouse.set_pos([cp_pos[0], cp_pos[1]])
				cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
				pygame.mouse.set_cursor(cursor)
			# cut/copy and paste モードのとき c でそのままでクリップボードにコピー
			if cp_mode == CP_MODE_AREA and event.key == K_c:
				clipboard(False)
				cp_mode = CP_MODE_CLIPPED
				# クリップボードに格納したらpaste用の矢印アイコンに変更
				pygame.mouse.set_pos([cp_pos[0], cp_pos[1]])
				cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
				pygame.mouse.set_cursor(cursor)
				
		#クリックで描く
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if pos[1] < block_size * matrix_size:
				if cp_mode != CP_MODE_NONE:
					if cp_mode == CP_MODE_CLIPPED and pygame.mouse.get_pressed()[0]:
						buf = []
						col = round(pos[0] / block_size)
						row = round(pos[1] / block_size)
						width = cp_pos[4]
						height = cp_pos[5]
						for r in range(height):
							for c in range(width):
								if r+row < matrix_size and c+col < matrix_size:
									buf.append((c+col, r+row, mtrx[r+row][c+col]))
									mtrx[r+row][c+col] = cp_buf[r][c]
						undo_buf.append(buf)
					elif cp_mode != CP_MODE_SELECTED or pygame.mouse.get_pressed()[2]:	# cut/copy and pasteモードの時はマウスの位置を保存し、クリップボードはクリア
						x, y = pos
						cp_pos = (x, y, 0, 0)
						cp_buf = None
						cp_mode = CP_MODE_SELECTED
						# カーソルをcut/copy 領域設定用のクロスマークに変更
						cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
						pygame.mouse.set_cursor(cursor)
				elif pygame.mouse.get_pressed()[0]:	 # 左クリックなら単純描画
					if pos[1] < block_size * matrix_size: 
						col = math.floor(pos[0] / block_size)
						row = math.floor(pos[1] / block_size)
						if mtrx[row][col] != color:	# 同じところに二度書きするとundoの動作が不自然になるので、禁止する
							undo_buf.append([(col, row, mtrx[row][col])])
							mtrx[row][col] = color
				elif pygame.mouse.get_pressed()[2]:	# 右クリックなら塗りつぶし(fill)
					col = math.floor(pos[0] / block_size)
					row = math.floor(pos[1] / block_size)
					undo_buf.append(fill(col, row, mtrx[row][col], color))
			# パレットの領域でクリックしたら色が変わる
			elif pos[1] >= block_size * matrix_size + pallet_size - block_size and \
				pos[1] < block_size * matrix_size + pallet_size:
				color = math.floor(pos[0] / block_size)
				set_cursor()
		#マウスののボタンを押した状態でマウスを動かして、描く
		if event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			if pos[1] < block_size * matrix_size:			
				if pygame.mouse.get_pressed()[0]:
					if cp_mode == CP_MODE_NONE:
						if pos[1] < block_size * matrix_size:
							col = math.floor(pos[0] / block_size)
							row = math.floor(pos[1] / block_size)
							if mtrx[row][col] != color:	# 同じところに二度書きするとundoの動作が不自然になるので、禁止する
								undo_buf.append([(col, row, mtrx[row][col])])
								mtrx[row][col] = color
					elif cp_mode == CP_MODE_SELECTED:
						if pos[1] < block_size * matrix_size:
							cp_pos = get_cp_area(pos)
		
		if cp_mode == CP_MODE_CLIPPED:
			pos = pygame.mouse.get_pos()
			if pos[1] < block_size * matrix_size:
				cp_pos = (pos[0], pos[1], cp_pos[2], cp_pos[3], cp_pos[4], cp_pos[5])
		
		#cut/copy and pasteモードでマウスボタンが解除されたら、cut/copy領域を線描画し、領域を記録する
		if cp_mode == CP_MODE_SELECTED and event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if pos[1] < block_size * matrix_size:
				cp_pos = get_cp_area(pos)
				cp_mode = CP_MODE_AREA

	draw()
	pygame.display.flip()
	clock.tick(20) 
pygame.quit()
