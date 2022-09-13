import pyttsx3
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

import RedditScraper
import image_creator
from moviepy.editor import ImageClip
from moviepy.editor import AudioFileClip, ImageClip

clips = []
bins = 0


def mp3_png_merge(image_path, audio_path, output_path):
    global clips
    global bins
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration

    video_clip.fps = 1
    output_path += str(bins)+'.mp4'
    video_clip.write_videofile(output_path)
    clips.append(VideoFileClip(output_path))
    bins += 1


def create_img(p):
    new = image_creator.img_converter(p)
    new.save('paragraph2.png')


def create_audio(p):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[2].id)
    engine.save_to_file(p, 'audio.mp3')
    engine.runAndWait()


def create_clip(p):
    create_img(p)
    create_audio(p)

    mp3_png_merge("paragraph2.png", "audio.mp3", "final_video")


final_text = RedditScraper.main()

for paragraph in final_text[5]:
    create_clip(paragraph)

final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("output_1.mp4")
print(len(clips))