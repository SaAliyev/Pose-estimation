# Pose Estimation with OpenCV and MediaPipe

This repository is a collection of scripts demonstrating various techniques for pose estimation using the OpenCV library and Google's MediaPipe framework.

## Description

The scripts provided here offer solutions for real-time pose detection:

- `Pose_Estimation_Min.py`: Detects a single pose within a video file.
- `Multi_Pose.py`: Detects multiple poses and tracks them across a video stream.
- `AItrainer.py`: Counts exercise repetitions by estimating the angle between body joints.

## Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- NumPy (For `count_reps.py` script)

## Installation

Install the required libraries using the following commands:

```bash
pip install opencv-python-headless
pip install mediapipe
pip install numpy
```
## Running the script
```
python <script_name>.py
```

## Output

When you run the scripts, expect the following output:

- A window will display the video stream with pose landmarks overlaid on the detected human figures.
- Landmark coordinates and other relevant data will be printed to the console for debugging and verification purposes.
- For `AItrainer.py`, a progress bar and repetition count will be displayed on the video stream.
- FPS (frames per second) information will be shown on the video to indicate the performance.

Ensure you have sufficient computational resources as real-time video processing is resource-intensive and may affect the FPS rate.


