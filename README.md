# Face Detection Web App

A simple web application for real-time face detection using Python, OpenCV, and Flask. Users can upload images, and the app will detect faces using Haar cascade classifiers, then display the results with rectangles drawn around detected faces.

---

## Features

- Upload an image from your computer.
- Detects faces in the image using OpenCV’s Haar cascade.
- Displays the number of faces detected and the image with faces highlighted.
- Simple, clean web interface.
- Easily containerized using Docker.

---

## Demo

![Demo Screenshot](static/demo_screenshot.png)  
*(Replace with your actual screenshot if available)*

---

## Tech Stack

- **Backend:** Python, Flask
- **Image Processing:** OpenCV (cv2)
- **Frontend:** Jinja2 (Flask templates), HTML
- **Containerization (optional):** Docker

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Face-Detection-Web-App.git
cd Face-Detection-Web-App/face_detection_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install OpenCV System Dependencies

If you encounter `ImportError: libGL.so.1: cannot open shared object file`, install the missing library:

```bash
sudo apt-get update
sudo apt-get install -y libgl1
```

### 4. Download Haar Cascade

If not already present, download the Haar cascade XML:

```bash
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml -P static
```

### 5. Run the application

```bash
python app.py
```

Visit the URL shown in your terminal (typically `http://127.0.0.1:5000/` or via your Codespace port link).

---

## Usage

1. Open the web app in your browser.
2. Upload an image file (preferably with visible faces).
3. The app will process your image and show how many faces were detected, with rectangles drawn around each face.

---

## Docker (Optional)

To run the app in a Docker container:

1. Create a `Dockerfile` (see below for sample).
2. Build and run:

```bash
docker build -t face-detection-app .
docker run -p 5000:5000 face-detection-app
```

---

## Example Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libgl1 wget && \
    wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml -P static

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

---

## Project Structure

```
face_detection_app/
│
├── app.py
├── requirements.txt
├── static/
│   └── haarcascade_frontalface_default.xml
├── templates/
│   └── index.html
└── (optional) Dockerfile
```

---

## Credits

- [OpenCV Haar Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- Flask documentation

---

## License

This project is licensed under the MIT License.