from moviepy.editor import *
import imageio_ffmpeg
import ffmpeg
import os


def ConcatVideos(input_video_path_list: list[str], output_video_path: str, temporary_process_folder: str):
    concat_file_list: list[str] = []
    for idx, input_video_path in enumerate(input_video_path_list, start=1):
        # convering individual file to .ts #
        temp_file_ts = f'{temporary_process_folder}/concat_{idx}.ts'
        os.system(
            f'''ffmpeg -y -loglevel error -i {input_video_path} -c copy -bsf:v h264_mp4toannexb -f mpegts {temp_file_ts} ''')
        concat_file_list.append(temp_file_ts)

    # concatenating .ts files and saving as .mp4 file #
    # ffmpeg will take care of encoding .ts to .mp4 #
    concat_string = '|'.join(concat_file_list)
    os.system(f'''ffmpeg -y -loglevel error -i \
        "concat:{concat_string}" -c copy {output_video_path}''')

    return output_video_path


clip1 = VideoFileClip("final_video0.mp4")
clip2 = VideoFileClip("final_video1.mp4")
clip3 = VideoFileClip("final_video2.mp4")
clip4 = VideoFileClip("final_video3.mp4")

clip5 = VideoFileClip("final_video4.mp4")
'''  
clip6 = VideoFileClip("final_video5.mp4")
clip7 = VideoFileClip("final_video6.mp4")
clip8 = VideoFileClip("final_video7.mp4")
clip9 = VideoFileClip("final_video8.mp4")
clip10 = VideoFileClip("final_video9.mp4")
'''
final = concatenate_videoclips([clip1, clip2, clip3], method="compose")
final.write_videofile("merged.mp4")
#final_video_path = ConcatVideos([clip1, clip2], 'merged.mp4', 'Temp')


