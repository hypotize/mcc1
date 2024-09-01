import os
import shutil
from create_image import create_image_files
from create_audio import create_audio_files
from create_video import create_video

def delete_previous_files():
    # 画像ファイルの削除
    if os.path.exists('image'):
        shutil.rmtree('image')
    
    # 音声ファイルの削除
    if os.path.exists('audio'):
        shutil.rmtree('audio')
    
    # 動画ファイルの削除
    if os.path.exists('せつめいどうが.mp4'):
        os.remove('せつめいどうが.mp4')

def main():
    # 前回実行したときに作成されたファイルを削除
    delete_previous_files()
    
    # 画像ファイル作成処理を実行
    create_image_files('せつめい.txt')
    
    # 音声ファイル作成処理を実行
    create_audio_files('せつめい.txt')
    
    # 動画ファイル作成処理を実行
    create_video()

if __name__ == "__main__":
    main()
