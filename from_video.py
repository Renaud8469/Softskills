import subprocess
import os
import json
from BVC import *


def video_to_wav(video_file, audio_file_name):
    command = "ffmpeg -i {} -ab 16 -ac 1 -ar 8000 -vn {}.wav".format(video_file, audio_file_name)
    subprocess.call(command, shell=True)
    return audio_file_name + ".wav"


def generate_analysis_from_video(video_file):
    video_file_name, video_file_extension = os.path.splitext(video_file)
    audio_file_name = video_file_name + "_audio"
    audio_file = video_to_wav("sources/" + video_file, "sources/" + audio_file_name)

    json_analysis = get_analysis(API_KEY, audio_file)
    with open("results/" + video_file_name + "_analysis.json", 'w') as f:
        json.dump(json_analysis, f)


def generate_analysis_from_audio(audio_file):
    audio_file_name, ext = os.path.splitext(audio_file)
    json_analysis = get_analysis(API_KEY, "sources/" + audio_file)
    with open("results/" + audio_file_name + "_analysis.json", 'w') as f:
        json.dump(json_analysis, f)


if __name__ == "__main__":
    video = "failed_interview.avi"
    generate_analysis_from_video(video)
    print('Done')

