
from ast import arg
from ultralytics import YOLO
import argparse
import cv2
import numpy as np
from pytube import YouTube
from moviepy.editor import VideoFileClip
from ultralytics.utils.plotting import Annotator
from ultralytics.utils.plotting import Colors



# declare video url to be analyzed for object detection
video_url = r'https://www.youtube.com/watch?v=xjLJKoWU-n0'
yt = YouTube(video_url)
print("Video Title: ", yt.title)

# download video
video_path = yt.streams \
  .filter(progressive=True, file_extension='mp4') \
  .order_by('resolution') \
  .desc() \
  .first() \
  .download() 
     

# get color pallete
colors = Colors()

# define function for frame annotation
def annotate_frame(frame_analyses, frame):

  # draw boxes on image
  for analysis in frame_analyses:

    # set frame to annotate
    annotator = Annotator(frame)
          
    # draw boxes with classes on frame
    boxes = analysis.boxes
    for box in boxes:
        bbox = box.xyxy[0] 
        cls = int(box.cls)
        annotator.box_label(box=bbox, label=model.names[cls], color=colors(cls))

  # return annotated frame
  return annotator.result() 


# load yolov8 model
model = YOLO('yolov8n.pt')

# loading video stream (from external link)
video = cv2.VideoCapture(video_path)

# get frame rate
fps = video.get(cv2.CAP_PROP_FPS)

# for storing video frames and yolo model analysis results for each frame (for output video)
result_frames = []
frames = []
i = 0

# looping over frames of loaded video stream
while True:
    
    return_value, frame = video.read()
    
    # condition for when video ends (return value == False)
    if not return_value:
        break
    
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(image)

    # get detections
    analysis = model(source=frame, stream=True)
    result_frames.append(annotate_frame(analysis, frame))

# live video stream released and all windows closed
video.release()
cv2.destroyAllWindows()

# creating output video with objects detected
output = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), fps, (1280,720))

for frame in result_frames:
  output.write(frame)

output.release()

# save output video
videoclip = VideoFileClip(video_path)
detection_video = VideoFileClip('output.mp4')

