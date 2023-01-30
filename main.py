#! /usr/bin/env python

import cv2
import torch
from torchvision import models
from utils import *
import time

device = torch.device('cpu')
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.fc = torch.nn.Linear(512, 2)
model.load_state_dict(torch.load('automator.pth', map_location=device))
model.to(device)
model.eval()

image = cv2.imread('dog.jpg')

categories = [
    'open',
    'close'
]

# source = 'rtsp://192.168.1.201:8080/h264_ulaw.sdp'
source = 'rtsp://admin:112233@192.168.1.113:554/h264Preview_01_sub'

cap = cv2.VideoCapture(source)

prev_frame_time = 0
new_frame_time = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    new_frame_time = time.time()

    preprocessed = preprocess(frame)
    output = model(preprocessed)
    output = F.softmax(output, dim=1).detach().cpu().numpy().flatten()
    category_index = output.argmax()
    print(categories[category_index])
    
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    textsize = cv2.getTextSize(categories[category_index], font, 3, 3)[0]

    textX = int((frame.shape[1] - textsize[0]) / 2)
    textY = int((frame.shape[0] + textsize[1]) / 2)
    
    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.putText(frame, categories[category_index], (textX, textY), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('STREAM', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# print(model.eval())
