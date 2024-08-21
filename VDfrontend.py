import streamlit as st
import cv2
import tempfile
from Vehicle_Detection import get_video, get_mask

# Streamlit app
st.title("Vehicle Detection and Counting")

# Upload video
video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

# Upload mask
mask_file = st.file_uploader("Upload a mask image", type=["png", "jpg", "jpeg"])

if video_file and mask_file:
    # Save the uploaded files temporarily
    with tempfile.NamedTemporaryFile(delete=False) as video_temp:
        video_temp.write(video_file.read())
        video_path = video_temp.name
    
    with tempfile.NamedTemporaryFile(delete=False) as mask_temp:
        mask_temp.write(mask_file.read())
        mask_path = mask_temp.name
    
    # Process and display the video
    frame = get_video(video_path, mask_path)

    # Display the processed video frame by frame
    stframe = st.empty()
    for img in frame:
        stframe.image(img, channels="BGR")
