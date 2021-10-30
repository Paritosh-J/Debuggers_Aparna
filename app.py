from flask import Flask, render_template, Response
from camera import Video
import cv2, dlib

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


def gen(camera):
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video=cv2.VideoCapture(0)
    faceDetector = dlib.get_frontal_face_detector()
    while True:
            # check, frame = video.read()
            ret,frame=video.read()
            # flip the frame captured like a mirror image
            frame = cv2.flip(frame, 1)
            grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect face
            face = faceDetector(grayImg)
            # variable with intial count for no. of faces = 0
            count = 0
            # flag for face limit warning
            flag = 0

            for f in face:
                # checking face limit
                if count == 1:
                    cv2.putText(frame, "WARNING! Max limit reached", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)
                    flag = 1

                if count > 1:  # if more than 3 persons in 2 wheeler vehicle
                    # function call to capture the snap of 3 or more faces
                    cv2.putText(frame, "ALERT! Defaulter Found", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)

                # coordinates for drawing rectangle around face
                x, y = f.left(), f.top()
                a, b = f.right(), f.bottom()

                # draw rectangle around the face
                if flag == 1: # max faces detected
                    cv2.rectangle(frame, (x, y), (a, b), (0, 255, 255), 2)  
                else:
                    cv2.rectangle(frame, (x, y), (a, b), (255, 0, 0), 2)  

                # increment face count upon detection
                count += 1
            ret,jpg=cv2.imencode('.jpg',frame)
    frame = jpg.tobytes()
    yield(b'--frame\r\n'
   b'Content-Type:  image/jpeg\r\n\r\n' + frame +
     b'\r\n\r\n')
    
        
        
@app.route('/video')
def video():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
