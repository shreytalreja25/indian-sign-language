import os
import cv2

def extract_frames(video_path):
    # Check if the video path exists
    if not os.path.exists(video_path):
        print("Video file not found.")
        return

    # Extract the directory and filename from the video path
    video_dir, video_file = os.path.split(video_path)
    video_name, video_ext = os.path.splitext(video_file)

    # Create a directory to store frames
    # frames_output_dir = os.path.join(video_dir, 'frames', video_name)
    frames_output_dir = "C:\chetan"
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

# Example usage:
video_path = r'C:\chetan\Video_Directory\Video_Directory\1 hello you how .MOV'
extract_frames(video_path)
