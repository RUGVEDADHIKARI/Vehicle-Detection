# Vehicle Detection and Counting System

This repository contains a vehicle detection and counting system built using YOLO v8, OpenCV, and Streamlit. The system allows users to upload videos, detect vehicles, and track their count in real-time.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)

## Overview

This project aims to provide an easy-to-use interface for detecting and counting vehicles in videos. The system is powered by the YOLO v8 model for object detection, and it uses a custom tracking algorithm to keep track of the detected vehicles.

## Features

- **Real-time Vehicle Detection**: Uses YOLO v8 to detect vehicles in uploaded videos.
- **Vehicle Tracking**: Tracks detected vehicles across frames to count them accurately.
- **User-Friendly Interface**: Built with Streamlit, the app provides a simple interface for video uploads and result visualization.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RUGVEDADHIKARI/Vehicle-Detection.git
   cd vehicle-detection
2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
3. **Download YOLO Weights**:
   Download the YOLO v8 model weights and place them in the appropriate directory (e.g., Yolo-Weights/).
4. **Run the Application**:
   Start the Streamlit application by running:
   ```bash
   streamlit run VDfrontend.py

## Usage

1. **Upload Video**: Use the interface to upload a video file (.mp4, .avi, .mov).
2. **Upload Mask**: Upload mask for the video. You can generate it on the canva.
3. **Process Video**:The system will process the video, detect, and count vehicles in real-time.
4. **View Results**:The results, including the detected vehicles and their count, will be displayed.

## File Structure

* **tracker.py**: Contains the Tracker class responsible for tracking detected vehicles.
* **VDfrontend.py**: Streamlit app that provides the user interface for the system.
* **Vehicle_Detection.py**: Core script that integrates YOLO and tracking for vehicle detection.
