# Object Detection with YOLOv8

This Python script uses YOLOv8 for object detection on a given video. It downloads a video from YouTube, applies YOLOv8 object detection on each frame, and creates an output video with annotated objects.

## Prerequisites

- Python 3.6 or later
- pip (Python package installer)

### Dependencies

- **OpenCV:** An open-source computer vision library used for image and video processing.
  
- **Ultralytics YOLOv8:** A deep learning object detection library that provides YOLOv8 models. It relies on PyTorch for the underlying deep learning operations.

- **PyTube:** A library for downloading YouTube videos.

- **MoviePy:** A library for video editing with capabilities to process and edit video files.


  

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ariyadmir/object-detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd object-detection
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Modify the `video_url` variable in the script with the desired YouTube video URL.

2. Run the script:

    ```bash
    python OD_YOLOv8.py.py
    ```

3. The script will download the video, perform object detection, and create an output video with annotated objects.

## Notes

- The output video is saved as 'output.mp4' in the project directory.

- Ensure you have an internet connection for downloading the video from YouTube.

## Acknowledgements

- YOLOv8: https://github.com/ultralytics/yolov5

- pytube: https://github.com/nficano/pytube

- moviepy: https://zulko.github.io/moviepy/

