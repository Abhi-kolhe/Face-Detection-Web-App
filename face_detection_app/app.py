from flask import Flask, render_template, request
import os
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Load the Haar cascade file
CASCADE_PATH = os.path.join(app.config['UPLOAD_FOLDER'], "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    faces_found = 0
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            image_url = filepath

            # Face detection
            img = cv2.imread(filepath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            faces_found = len(faces)
            # Draw rectangle around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            detected_path = os.path.join(app.config['UPLOAD_FOLDER'], 'detected_' + file.filename)
            cv2.imwrite(detected_path, img)
            image_url = detected_path

    return render_template('index.html', image_url=image_url, faces_found=faces_found)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")