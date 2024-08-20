# Vehicle Detection System

This project is a Vehicle Detection System that uses YOLO v8 and OpenCV to detect and count vehicles such as cars, motorcycles, and trucks from a video feed. The system overlays the detected vehicle count on the video frame in real-time.

## Getting Started

### Features

* Real-time Vehicle Detection: Detects and classifies different types of vehicles (cars, motorcycles, trucks) in real-time.
* Vehicle Counting: Keeps track of the number of vehicles detected, displaying counts directly on the video frame.
* Customizable: Parameters for vehicle detection and counting can be customized to fit different use cases.
  
### Installation

* Clone the repository:
  ```
  git clone https://github.com/yourusername/vehicle-detection-system.git
  cd vehicle-detection-system
  ```
* Install required dependencies:
  Make sure you have Python 3.x installed. Install the necessary Python packages using pip:
  ```
  pip install -r requirements.txt
  ```
  Typical dependencies include:
  * OpenCV
  * YOLOv8 (Ultralytics)
  * NumPy
* Download YOLOv8 weights:
  You'll need to download the pretrained YOLOv8 weights and place them in the appropriate directory. Instructions can be    
  found [here](https://github.com/ultralytics/yolov5/releases)

### Usage

* Run the vehicle detection script:
   ```
   python vehicle_detection.py --video <path_to_video_file>
   ```
   Replace <path_to_video_file> with the path to the video file you want to analyze. You can also use a webcam by omitting      the --video option.
* View Results:
   The script will display the video with vehicle counts overlaid in real-time. Press ESC to exit the video stream.

### Project Structure
* vehicle_detection.py: Main script for running the vehicle detection and counting system.
* requirements.txt: Lists all Python dependencies required for the project.
* models/: Directory to place the YOLOv8 model weights.
* data/: Sample video files for testing.

### Customization
You can customize the detection and counting parameters within the vehicle_detection.py script to suit your specific use case, such as adjusting detection confidence thresholds or changing the categories of vehicles to detect.
