from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

# Open the file in read mode
with open("g1.txt", "r") as file:
    # Read the contents of the file
    content = file.read()

    # Split the content of the file by newline character and convert each element to integer
    frames = [int(num) for num in content.strip().split('\n')]
filename = r"output\vid2024-04-27_19-08-24.mp4"
video_clip = VideoFileClip(filename)

audio_clip = AudioFileClip(r"assets\sound_file1.wav")
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

video.write_videofile(filename.replace(".mp4","o.mp4"), codec="libx264", fps=fps)
