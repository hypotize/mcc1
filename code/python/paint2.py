import pygame
import sys
from pygame.locals import *
import random
import math
import datetime
import tkinter as tk
import tkinter.filedialog
from PIL import Image

# 機能拡張の概要
# ・　描画時の指定色が分かりやすい用に、アイコンを色アイコン（円形）に変更
# ・　描画時に右クリックすると、クリックされた位置の色の領域を指定色で塗りつぶす(fill機能)
# ・　oキーでセーブした画像を読み込む機能(open機能）
# ・ uキーで各処理ごとにundoする機能(undo機能、但しredo機能はなし）
# ・ iキーで画像全体とundo等を初期化する機能(initialize機能）
# ・　pキーでcut/copy and pasteモードに移行（クロスアイコンに変更）もう一度押すと
#	・　マウスボタンを押した状態から放すまでで領域を選択
#	・ 領域選択状態でxキーを押すと選択領域をカットして、クリップボードに格納（矢印アイコンに変更）
#	・ 領域選択状態でcキー押すと選択領域をカットせず、クリップボードに格納（矢印アイコンに変更）
#	・ クリップボード格納状態でvキーを押すとマウスの位置にクリップボードの内容をコピーする
#	・　再度マウスボタンを押すとクリップボードの内容が削除され、領域選択モード（クロスアイコン）に戻る
#	・　pキーをもう一度押すといつでも通常モードに戻る（クリップボードも削除）

# いろをいくつか定義
colors = ((0, 0, 0),	   #黒
		  (255, 0, 0),	   #赤
		  (0, 255, 0),	   #みどり
		  (0, 0, 255),	   #青
		  (255, 255, 255)  #白
		  )

#最初のペンキのいろ
color = 0

# 設定色の合わせてカーソル（円）の色を変更
def set_cursor():
	surf = pygame.Surface((40, 40), pygame.SRCALPHA) # you could also load an image 
	surf.fill((255, 255, 255, 0))
	pygame.draw.circle(surf, colors[color], (20, 20), 6)
	if color == 0:	#黒の時は輪郭を白に
		pygame.draw.circle(surf, colors[4], (20, 20), 6, width=1)
	else:	#黒以外は輪郭を黒に
		pygame.draw.circle(surf, colors[0], (20, 20), 6, width=1)
	cursor = pygame.cursors.Cursor((20, 20), surf)
	pygame.mouse.set_cursor(cursor)

#一個の箱の大きさ(ピクセル)
block_size = 20
#箱の数(一辺) 
matrix_size = 30

# 最初は全部白にする (白は4)
mtrx =	[[4] * matrix_size for i in range(matrix_size)]

# ファイルオープン用のダイアログ
def dialog():
	# ルートウィンドウ作成
	root = tk.Tk()
	# ルートウィンドウの非表示
	root.withdraw()

	# ファイル選択
	filetypes = [("画像ファイル", "*.jpg")]
	filename = tkinter.filedialog.askopenfilename(filetypes=filetypes, title="ファイルをひらく")
	root.destroy()
	return filename

# 画像ファイルをオープンして、箱を復元する
def openfile(filename):
	image = Image.open(filename)
	width, height = image.size
	# 画像の幅と高さが合っていなければエラー
	if width != block_size * matrix_size or height != block_size * matrix_size:
		print("invalid jpeg file!")
		return False
	for y in range(0, matrix_size):
		for x in range(0, matrix_size):
			row = x * block_size + block_size // 2
			col = y * block_size + block_size // 2
			pixel = image.getpixel((row, col))
			# JPEGでは画素情報が鈍っているので128を境に大胆にフィルタリング
			# 設定色に中間色(R,G,Bのいずれかが0か255以外)を追加する場合はフィルタの内容を変更する必要あり
			r = 0 if pixel[0] < 128 else 255
			g = 0 if pixel[1] < 128 else 255
			b = 0 if pixel[2] < 128 else 255
			pixel = (r, g, b)
			# rgbをカラーテーブルのインデックスに変換、テーブルになければとりあえず白にする
			if pixel in colors:
				c = colors.index(pixel)
			else:
				c = 4
			mtrx[y][x] = c
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
	for i in range(matrix_size):
		for j in range(matrix_size):
			val = mtrx[j][i]
			pygame.draw.rect(screen,colors[val],[i * block_size, j * block_size, block_size,block_size], 0)

pygame.init()
screen = pygame.display.set_mode([block_size * matrix_size, block_size * matrix_size])
pygame.display.set_caption("Miura Paint ")
 
done = False
clock = pygame.time.Clock()

set_cursor()

cp_mode = 0			# cut/copy and paste mode
					# 0: 通常描画モード 1: 座標未選択　2: 座標選択済み 3: 領域選択済み 4: クリープボード格納済
cp_pos = None		# cut/copy 選択位置／矩形領域
cp_buf = None		# cut/copy 矩形領域の元画像を格納するクリップボード

def draw_cp_area(pos):	# cut/copyの選択領域を矩形の線で表示し、左上の位置を返す
	x = min(pos[0], cp_pos[0])
	y = min(pos[1], cp_pos[1])
	w = abs(pos[0] - cp_pos[0])
	h = abs(pos[1] - cp_pos[1])
	pygame.draw.rect(screen, (192, 192, 192), [x, y, w, h], width=1)
	return (x, y)

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
			if cp_mode == 0:	# cut/copy and pasteモードの時は描画系の処理は無効
				#色の切り替え 1 ~ 5 までのの色
				if event.key == K_1:
					color = 0
					set_cursor()
				if event.key == K_2:
					color = 1
					set_cursor()
				if event.key == K_3:
					color = 2
					set_cursor()
				if event.key == K_4:
					color = 3
					set_cursor()
				if event.key == K_5:
					color = 4
					set_cursor()
				# s で保存
				if event.key == K_s:
					dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
					filename = "screenshot_" + dt + ".jpg"
					pygame.image.save(screen ,filename)
					print(filename, "で保存しました。")
				# o で読み込み
				if event.key == K_o:
					filename = dialog()
					if openfile(filename):
						print(filename, "を読み込みました。")
					undo_buf.clear()
			# i で画面と状態を全て初期化
			if event.key == K_i:
				cp_mode = 0
				cp_pos = None
				cp_buf = None
				color = 0
				set_cursor()
				undo_buf.clear()
				mtrx =	[[4] * matrix_size for i in range(matrix_size)]
			# u でundo
			if event.key == K_u:
				undo()
			# p でcut/copy and paste モードと通常モードの切り替え
			if event.key == K_p:
				cp_pos = None
				cp_buf = None
				if cp_mode > 0:
					cp_mode = 0
					set_cursor()
				else:
					cp_mode = 1
					# カーソルをcut/copy 領域設定用のクロスマークに変更
					cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
					pygame.mouse.set_cursor(cursor)
			# cut/copy and paste モードのとき　x でcutしてクリップボードにコピー
			if cp_mode == 3 and event.key == K_x:
				cp_buf = [[mtrx[r][c] for c in range(col, col+width)] for r in range(row, row+height)]
				cp_mode = 4
				buf = []
				for r in range(cp_pos[0], cp_pos[0]+cp_pos[1]):
					for c in range(cp_pos[2], cp_pos[2]+cp_pos[3]):
						buf.append((c, r, mtrx[r][c]))
						mtrx[r][c] = 4
				undo_buf.append(buf)	# cutしても戻せるようにundoバッファに格納
				# クリップボードに格納したらpaste用の矢印アイコンに変更
				cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
				pygame.mouse.set_cursor(cursor)
			# cut/copy and paste モードのとき　c そのままでクリップボードにコピー
			if cp_mode == 3 and event.key == K_c:
				cp_buf = [[mtrx[r][c] for c in range(col, col+width)] for r in range(row, row+height)]
				cp_mode = 4
				# クリップボードに格納したらpaste用の矢印アイコンに変更
				cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
				pygame.mouse.set_cursor(cursor)
			# cut/copy and paste モードでクリップボードが空でなければ　v でマウスの位置にクリップボードを貼り付け
			if cp_mode == 4 and event.key == K_v:
				buf = []
				pos = pygame.mouse.get_pos()
				col = math.floor(pos[0] / block_size)
				row = math.floor(pos[1] / block_size)
				for r in range(cp_pos[1]):
					for c in range(cp_pos[3]):
						if r+row < matrix_size and c+col < matrix_size:
							buf.append((c+col, r+row, mtrx[r+row][c+col]))
							mtrx[r+row][c+col] = cp_buf[r][c]
				undo_buf.append(buf)
		#クリックで描く
		if event.type == pygame.MOUSEBUTTONDOWN:
			if cp_mode != 0:	# cut/copy and pasteモードの時はマウスの位置を保存し、クリップボードはクリア
				cp_pos = pygame.mouse.get_pos()
				cp_buf = None
				cp_mode = 2
				# カーソルをcut/copy 領域設定用のクロスマークに変更
				cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
				pygame.mouse.set_cursor(cursor)
			elif pygame.mouse.get_pressed()[0]:  # 左クリックなら単純描画
				pos = pygame.mouse.get_pos()
				col = math.floor(pos[0] / block_size)
				row = math.floor(pos[1] / block_size)
				if mtrx[row][col] != color:	# 同じところに二度書きするとundoの動作が不自然になるので、禁止する
					undo_buf.append([(col, row, mtrx[row][col])])
					mtrx[row][col] = color
			elif pygame.mouse.get_pressed()[2]:	# 右クリックなら塗りつぶし(fill)
				pos = pygame.mouse.get_pos()
				col = math.floor(pos[0] / block_size)
				row = math.floor(pos[1] / block_size)
				undo_buf.append(fill(col, row, mtrx[row][col], color))		

		#マウスののボタンを押した状態でマウスを動かして、描く
		if cp_mode == 0 and event.type == pygame.MOUSEMOTION:
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				col = math.floor(pos[0] / block_size)
				row = math.floor(pos[1] / block_size)
				if mtrx[row][col] != color:	# 同じところに二度書きするとundoの動作が不自然になるので、禁止する
					undo_buf.append([(col, row, mtrx[row][col])])
					mtrx[row][col] = color
		
		#cut/copy and pasteモードでマウスボタンが解除されたら、cut/copy領域を線描画し、領域を記録する
		if cp_mode == 2 and event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			x, y = draw_cp_area(pos)
			col = math.ceil(x / block_size)
			row = math.ceil(y / block_size)
			width = math.floor(pos[0] / block_size) - col + 1
			height = math.floor(pos[1] / block_size) - row + 1
			cp_pos = (row, height, col, width)
			cp_mode = 3

	if cp_mode != 3:	# cut/copy領域が線描がされている場合は描画更新しない
		draw()
	pygame.display.flip()
	clock.tick(20) 
pygame.quit()
