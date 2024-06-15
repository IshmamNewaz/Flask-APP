from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_frames():

    while(True):
        success, frame = camera.read() #Returns 2 parameters 1 boolean 2 the frames
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
            eyes_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
            faces = detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
            #draw rectangles
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w, y+w),(255,0,0), 2)
                roi_gray= gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eyes_cascade.detectMultiScale(roi_gray,1.1,3)
                for(ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0),2)
            # takes the frames and encodes to jpg or png and returns 2 things Ret, buffer
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            #Can't use return cuz it will return only 1 frame. So we need to continuously call and return it. So use Yield
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        # Dont freak out its just a content type, Why? No idea. Just Do it.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)
