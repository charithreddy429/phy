from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from pydub import AudioSegment

# Open the file in read mode
with open("g1.txt", "r") as file:
    # Read the contents of the file
    content = file.read()

    # Split the content of the file by newline character and convert each element to integer
    frames = [int(num) for num in content.strip().split('\n')]

video_clip = VideoFileClip(r"output\vid2024-04-18_23-21-48.mp4")

audio_clip = AudioFileClip("assets\sound_file.mpeg")
audio_clip = audio_clip.volumex(0.8)

all_audio_clips = []
fps = 60

for frame in frames:
    # Calculate start time in milliseconds based on frame number
    start_time_ms = frame / fps  # Assuming fps is frames per second

    # Set the start time of the audio clip to the specified time
    audio_clip_with_start_time = audio_clip.set_start(start_time_ms)

    # Append the adjusted audio clip to the list
    all_audio_clips.append(audio_clip_with_start_time)

concatenate_clip = CompositeAudioClip(all_audio_clips)

video = video_clip.set_audio(concatenate_clip)

video.write_videofile("output.mp4", codec="libx264", fps=fps)