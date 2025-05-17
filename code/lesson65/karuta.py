import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw # Pillowライブラリを使用
import os
import random
import time # 今回はtkinterのafterメソッドを使うため、直接的なtime.sleepはGUIでは避ける

# --- 定数定義 ---
IMAGE_DIR = "画像"  # 画像ファイルが格納されているフォルダ名
IMAGE_WIDTH = 150  # 表示する画像の幅
IMAGE_HEIGHT = 150 # 表示する画像の高さ
WINDOW_WIDTH = 600 # ウィンドウの幅
WINDOW_HEIGHT = 550 # ウィンドウの高さ
TOTAL_ROUNDS = 3   # ゲームの総ラウンド数
RESULT_DISPLAY_TIME_MS = 1000 # 結果表示時間 (ミリ秒)

class ImageQuizGame:
    def __init__(self, root):
        """
        ゲームの初期化処理を行うコンストラクタ
        :param root: Tkinterのメインウィンドウオブジェクト
        """
        self.root = root
        self.root.title("画像当てクイズ")

        # ウィンドウサイズを設定
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        # ウィンドウサイズを固定
        self.root.resizable(False, False)
        # ウィンドウを画面中央に表示
        self.center_window()

        # ゲームで使用する画像ファイル名のリストをロード
        self.image_files = self.load_image_files()
        if not self.image_files or len(self.image_files) < 3:
            messagebox.showerror("エラー", f"'{IMAGE_DIR}' フォルダに3つ以上の画像ファイルが見つかりません。")
            self.root.destroy()
            return

        # ゲームの状態変数
        self.current_round = 0
        self.correct_answer_file = ""
        self.selected_images_for_round = []
        self.game_state = "waiting_to_start" # "playing", "showing_result", "game_over"

        # UI要素の初期化 (最初は何も表示しないか、開始メッセージのみ)
        # メインフレームを作成し、すべてのUI要素をこの中に入れることでクリアしやすくする
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # キーイベントのバインド (スペースキー)
        self.root.bind("<space>", self.handle_space_key)

        # 開始画面を表示
        self.show_start_screen()

    def center_window(self):
        """ウィンドウを画面の中央に表示する"""
        self.root.update_idletasks() # ウィンドウの実際のサイズを計算するために必要
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (WINDOW_WIDTH // 2)
        y = (screen_height // 2) - (WINDOW_HEIGHT // 2)
        self.root.geometry(f"+{x}+{y}")

    def load_image_files(self):
        """
        指定されたディレクトリから画像ファイル名のリストをロードする。
        :return: 画像ファイル名のリスト (例: ["image1.png", "image2.jpg"])
        """
        if not os.path.isdir(IMAGE_DIR):
            return []
        
        supported_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        files = [f for f in os.listdir(IMAGE_DIR) 
                 if os.path.isfile(os.path.join(IMAGE_DIR, f)) and f.lower().endswith(supported_extensions)]
        return files

    def clear_main_frame(self):
        """メインフレーム内のすべてのウィジェットを削除する"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        """ゲーム開始前の画面を表示する"""
        self.clear_main_frame()
        self.game_state = "waiting_to_start"
        
        message_label = tk.Label(self.main_frame, text="スペースキーを押してゲームを開始", font=("Arial", 20))
        message_label.pack(pady=50, expand=True)

    def handle_space_key(self, event):
        """スペースキーが押されたときの処理"""
        if self.game_state == "waiting_to_start" or self.game_state == "game_over":
            self.start_game()

    def start_game(self):
        """ゲームを開始する"""
        self.current_round = 0
        self.game_state = "playing"
        self.next_round()

    def next_round(self):
        """次のラウンドの準備と表示を行う"""
        self.clear_main_frame() # 前のラウンドの表示をクリア

        if self.current_round >= TOTAL_ROUNDS:
            self.show_game_over_screen()
            return

        self.current_round += 1
        self.game_state = "playing"

        # 1. '画像'フォルダの中の画像ファイルからランダムに3つを選ぶ
        if len(self.image_files) < 3: # 念のため再度チェック
            messagebox.showerror("エラー", "画像ファイルが不足しています。")
            self.root.destroy()
            return
        self.selected_images_for_round = random.sample(self.image_files, 3)

        # 2. 選んだ3つの画像ファイルの中から1つを選んで、それを答えとする
        self.correct_answer_file = random.choice(self.selected_images_for_round)

        # 3. 答えの画像ファイルのファイル名から拡張子以外の部分を取り出して、それを問題文とする
        question_text, _ = os.path.splitext(self.correct_answer_file)

        # 4. 問題文と選んだ3つの画像ファイルをウィンドウに表示する
        # 問題文ラベル
        question_label = tk.Label(self.main_frame, text=question_text, font=("Arial", 24, "bold"))
        question_label.pack(pady=20)

        # 画像表示用のフレーム
        images_frame = tk.Frame(self.main_frame)
        images_frame.pack(pady=20)

        self.image_tk_objects = [] # ImageTk.PhotoImageオブジェクトを保持（ガベージコレクション対策）

        for i, img_file in enumerate(self.selected_images_for_round):
            file_path = os.path.join(IMAGE_DIR, img_file)
            try:
                # Pillowを使って画像を開き、リサイズ
                pil_image = Image.open(file_path)
                pil_image = pil_image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(pil_image)
                self.image_tk_objects.append(img_tk) # 参照を保持

                # 画像ラベルを作成し、クリックイベントをバインド
                # lambdaを使って、クリック時に正しいファイル名が渡されるようにする
                img_label = tk.Label(images_frame, image=img_tk, relief=tk.RAISED, borderwidth=2)
                img_label.image = img_tk # これもガベージコレクション対策で参照を保持
                img_label.pack(side=tk.LEFT, padx=10)
                img_label.bind("<Button-1>", lambda event, fname=img_file: self.handle_image_click(fname))
            except Exception as e:
                print(f"画像の読み込みエラー: {file_path}, {e}")
                # エラーが発生した画像は代替テキスト表示などを行うことも可能
                error_label = tk.Label(images_frame, text=f"画像読込失敗:\n{img_file[:15]}...", width=IMAGE_WIDTH//7, height=IMAGE_HEIGHT//15, relief=tk.SUNKEN)
                error_label.pack(side=tk.LEFT, padx=10)


    def handle_image_click(self, clicked_image_file):
        """
        画像がクリックされたときの処理
        :param clicked_image_file: クリックされた画像のファイル名
        """
        if self.game_state != "playing": # 結果表示中やゲームオーバー時は何もしない
            return
        
        self.game_state = "showing_result" # 状態を結果表示中に変更

        # 一時的に画像クリックイベントを無効化 (すべての画像ラベルからバインドを解除)
        for widget in self.main_frame.winfo_children(): # images_frame の子ウィジェットを対象にするのがより正確
            if isinstance(widget, tk.Frame): # images_frameを探す
                 for img_widget in widget.winfo_children():
                    if isinstance(img_widget, tk.Label) and hasattr(img_widget, 'image'):
                        img_widget.unbind("<Button-1>")


        is_correct = (clicked_image_file == self.correct_answer_file)
        self.show_result_feedback(is_correct)

        # 1秒待ってから次の処理へ (ウィンドウをクリアして、繰り返しの始めに戻る)
        self.root.after(RESULT_DISPLAY_TIME_MS, self.next_round)


    def show_result_feedback(self, is_correct):
        """
        正解・不正解のフィードバック（丸やバツ）を表示する
        :param is_correct: 正解したかどうか (True/False)
        """
        # 結果表示用のCanvasを作成 (問題文と画像の間など、適切な場所に配置)
        # pack_forget() で既存のウィジェットを隠し、Canvasを配置し、処理後に戻す方法もある
        # 今回は、既存のレイアウトを活かし、メインフレームの上部に重ねて表示する
        
        result_canvas = tk.Canvas(self.main_frame, width=100, height=100, bg=self.main_frame.cget('bg'), highlightthickness=0)
        # Canvasの配置 (例: ウィンドウの中央あたり)
        # main_frameの中心に表示するためにplaceを使う
        result_canvas.place(relx=0.5, rely=0.6, anchor=tk.CENTER) # 位置は調整が必要

        if is_correct:
            # 緑の丸を描画
            result_canvas.create_oval(10, 10, 90, 90, fill="green", outline="green")
        else:
            # 赤のバツを描画
            result_canvas.create_line(10, 10, 90, 90, fill="red", width=10)
            result_canvas.create_line(10, 90, 90, 10, fill="red", width=10)
        
        # RESULT_DISPLAY_TIME_MS後にこのCanvasを消す処理を next_round 内の clear_main_frame で行うか、
        # ここでafterを使って消すようにスケジュールする。next_roundでクリアされるので、ここでは不要。


    def show_game_over_screen(self):
        """ゲーム終了画面を表示する"""
        self.clear_main_frame()
        self.game_state = "game_over"
        
        message_label = tk.Label(self.main_frame, text="ゲーム終了", font=("Arial", 24))
        message_label.pack(pady=30)
        
        retry_label = tk.Label(self.main_frame, text="スペースキーを押すと、もういちどできます", font=("Arial", 16))
        retry_label.pack(pady=10, expand=True)

# --- メイン処理 ---
if __name__ == "__main__":
    root = tk.Tk()  # メインウィンドウの作成
    game_app = ImageQuizGame(root) # ゲームクラスのインスタンスを作成
    root.mainloop() # Tkinterのイベントループを開始
