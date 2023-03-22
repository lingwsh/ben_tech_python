import moviepy.editor as mp
import openai
import time
import os

# Extract audio from video to srt
path = "/ben_tech/12_python_string/output/python_string-YouTube_4k.mp4"
prompt = "使用ChatGPT基于GPT4 讲解Python String"
api_key = "Put your key in here"

# Get file name without extension
filename = path.split("/")[-1].split(".")[0]
print(filename)
my_clip = mp.VideoFileClip(path)
output_name = "/data/{}.mp3".format(filename)
# Check the path file exists
if not os.path.exists(output_name):
    my_clip.audio.write_audiofile(output_name)

# Use OpenAI API to transcribe audio to text
start_time = time.time()
openai.api_key = api_key
# Better use your local absolute path
file_path = output_name
file = open(file_path, "rb")


# response_format: default is json.  text, srt, verbose_json, or vtt are also supported.
# API link:
# https://platform.openai.com/docs/api-reference/audio/create

# language: default is autodetect.
# Supported languages:
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

print("Start transcribing...")
transcription = openai.Audio.transcribe("whisper-1", file, prompt=prompt, response_format="srt", language="zh")

# Better use your local absolute path and set the output file name
output_path = "/output/{}.srt".format(filename)

with open(output_path, "w") as f:
    f.write(str(transcription))

end_time = time.time()
time_spent = round(end_time - start_time, 2)
print("Time spent:", time_spent, "seconds")