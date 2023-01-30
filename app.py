from flask import Flask, render_template, Response
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

app = Flask(__name__)

camera = cv2.VideoCapture(source)  # use 0 for web camera


def gen_frames():
    
    prev_frame_time = 0
    new_frame_time = 0

    status_count = 0
    current_status = None
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            new_frame_time = time.time()

            category_index = model.predict_class(frame)

            if status_count == 7:
                On = True if current_status == 1 else False
                bridge.toggle_entrance_light(On)

            if current_status != category_index:
                status_count = 0

            current_status = category_index
            status_count += 1

            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps)
            fps = str(fps)
            font = cv2.FONT_HERSHEY_SIMPLEX

            textsize = cv2.getTextSize(
                categories[category_index], font, 3, 3)[0]

            textX = int((frame.shape[1] - textsize[0]) / 2)
            textY = int((frame.shape[0] + textsize[1]) / 2)

            cv2.putText(frame, fps, (7, 70), font, 3,
                        (100, 255, 0), 3, cv2.LINE_AA)
            cv2.putText(frame, categories[category_index],
                        (textX, textY), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
