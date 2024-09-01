from gtts import gTTS
import os

def create_audio_files(text_file):
    # ディレクトリの作成
    if not os.path.exists('audio'):
        os.makedirs('audio')

    with open(text_file, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')

    for i, paragraph in enumerate(paragraphs):
        # 音声ファイルの作成
        tts = gTTS(text=paragraph, lang='ja')
        tts.save(f'audio/{i}.mp3')

if __name__ == "__main__":
    create_audio_files('せつめい.txt')
