import moviepy.editor as mp
import os

def create_video():
    # 画像と音声のファイルリストを取得
    image_files = sorted([f'image/{f}' for f in os.listdir('image') if f.endswith('.png')])
    audio_files = sorted([f'audio/{f}' for f in os.listdir('audio') if f.endswith('.mp3')])

    clips = []
    for img_file, audio_file in zip(image_files, audio_files):
        # 画像と音声を結合
        img_clip = mp.ImageClip(img_file).set_duration(mp.AudioFileClip(audio_file).duration)
        audio_clip = mp.AudioFileClip(audio_file)
        video_clip = img_clip.set_audio(audio_clip)
        clips.append(video_clip)

    # 動画ファイルの作成
    final_clip = mp.concatenate_videoclips(clips)
    final_clip.write_videofile('せつめいどうが.mp4', fps=24)

if __name__ == "__main__":
    create_video()
