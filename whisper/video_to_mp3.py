import moviepy.editor as mp

# This path is your video file path
path = "extract_file_path"
my_clip = mp.VideoFileClip(path)

output_name = "output.mp3"

my_clip.audio.write_audiofile(output_name)