#! /usr/bin/env python

import cv2
from automator_loader import AutomatorModel
from homebridge import HomeBridgeController
from utils import *
import time
from decouple import config


categories = [
    'close',
    'open',
]

source = config('CAM_SOURCE')

bridge = HomeBridgeController()
model = AutomatorModel()
# detector = ObjectDetectorController()

cap = cv2.VideoCapture(source)

prev_frame_time = 0
new_frame_time = 0

status_count = 0
current_status = None

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    new_frame_time = time.time()

    category_index = model.predict_class(frame)

    if status_count == 7:
        On = True if current_status == 1 else False
        bridge.toggle_entrance_light(On)

    if current_status != category_index:
        status_count = 0

    current_status = category_index
    status_count += 1

    # detections = detector.get_predictions(frame)
    
    # for i in range(0, len(detections["boxes"])):
    #     confidence = detections["scores"][i]
    #     if confidence > .5:
    #         idx = int(detections["labels"][i])
    #         box = detections["boxes"][i].detach().cpu().numpy()
    #         (startX, startY, endX, endY) = box.astype("int")
    #         label = "{:.2f}%".format(confidence * 100)
    #         print("[INFO] {}".format(label))
    #         cv2.rectangle(frame, (startX, startY), (endX, endY),
    #             (255, 255, 0), 2)
    #         y = startY - 15 if startY - 15 > 15 else startY + 15
    #         cv2.putText(frame, label, (startX, y),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)


    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)
    font = cv2.FONT_HERSHEY_SIMPLEX

    textsize = cv2.getTextSize(categories[category_index], font, 3, 3)[0]

    textX = int((frame.shape[1] - textsize[0]) / 2)
    textY = int((frame.shape[0] + textsize[1]) / 2)

    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    cv2.putText(frame, categories[category_index],
                (textX, textY), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    
    cv2.imshow('HOME AUTOMATOR', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
