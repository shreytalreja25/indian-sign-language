import os
import cv2

# Directory containing the videos
video_dir = r'C:\chetan\Video_Directory\Video_Directory'

# Create a directory to store frames if it doesn't exist
frames_dir = os.path.join(video_dir, 'frames')
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Iterate through each video file
for video_file in os.listdir(video_dir):
    if video_file.endswith('.mp4') or video_file.endswith('.avi') or video_file.endswith('.MOV'):
        video_path = os.path.join(video_dir, video_file)
        video_name = os.path.splitext(video_file)[0]
        frames_output_dir = os.path.join(frames_dir, video_name)
        
        # Create a directory for frames from the current video
        if not os.path.exists(frames_output_dir):
            os.makedirs(frames_output_dir)
        
        # Open the video file
        video_capture = cv2.VideoCapture(video_path)
        
        # Read frames and save them
        frame_count = 0
        while True:
            success, frame = video_capture.read()
            if not success:
                break
            frame_output_path = os.path.join(frames_output_dir, f'{video_name}_frame_{frame_count}.jpg')
            cv2.imwrite(frame_output_path, frame)
            frame_count += 1
        
        video_capture.release()

print("Frames extraction completed.")
