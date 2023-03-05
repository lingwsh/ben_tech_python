import openai
import time

start_time = time.time()

api_key = "Input your API key here"
openai.api_key = api_key

# Better use your local absolute path
file_path = "/data/test.m4a"
file = open(file_path, "rb")

prompt = "Write your prompt here"

# response_format: default is json.  text, srt, verbose_json, or vtt are also supported.
# API link:
# https://platform.openai.com/docs/api-reference/audio/create

# language: default is autodetect.
# Supported languages:
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

transcription = openai.Audio.transcribe("whisper-1", file, prompt=prompt, response_format="srt", language="zh")

# Better use your local absolute path and set the output file name
output_path = "/output/test.srt"

# Error fix file path: venv/lib/python3.9/site-packages/openai/api_requestor.py

with open(output_path, "w") as f:
    f.write(str(transcription))

end_time = time.time()
time_spent = round(end_time - start_time, 2)
print("Time spent:", time_spent, "seconds")