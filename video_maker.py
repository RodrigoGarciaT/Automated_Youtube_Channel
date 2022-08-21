#from moviepy.editor import AudioFileClip, ImageClip
import pyttsx3
#from moviepy.video.VideoClip import VideoClip
import RedditScraper
import image_creator
#from moviepy.editor import *
from moviepy.editor import ImageClip
from moviepy.editor import AudioFileClip, ImageClip


def mp3_png_merge(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration

    video_clip.fps = 1
    video_clip.write_videofile(output_path)


def create_img():
    new = image_creator.img_converter(final_text[5][0])
    new.save('paragraph2.png')


def create_audio():
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[2].id)
    engine.save_to_file(final_text[5][0], 'audio.mp3')
    engine.runAndWait()


final_text = RedditScraper.main()

create_img()
create_audio()

mp3_png_merge("paragraph2.png", "audio.mp3", "final_video.mp4")


'''
clip1 = VideoFileClip("audio.mp3").subclip(10, 20)
clip2 = VideoFileClip("audio.mp3").subclip(10,20)

combined = concatenate_videoclips([clip1, clip2])
combined.write_videofile("combined.mp4")
'''