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
