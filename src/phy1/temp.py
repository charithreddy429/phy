import cv2

# Input video file path
input_video_path = 'input/vdi-3.mp4'

# Output video file path
output_video_path = 'output/vid3.mp4'
# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get the video's width, height, and frames per second (fps)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create VideoWriter object to save the rotated video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec if needed
out = cv2.VideoWriter(output_video_path, fourcc, fps, (height, width))

# Read and rotate each frame
i = 0
while True:
    i+=1
    if i%2 ==0:
        continue
    ret, frame = cap.read()
    if not ret:
        break

    # Rotate the frame by 90 degrees
    rotated_frame = cv2.transpose(frame)
    rotated_frame = cv2.flip(rotated_frame, 1)  # Flip horizontally if needed

    # Write the rotated frame to the output video file
    out.write(rotated_frame)

# Release VideoCapture and VideoWriter objects
cap.release()
out.release()

print("Video rotation complete.")
