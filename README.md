# AI Face Search Web Application

## Overview

This project is a **web-based facial recognition search tool** built using Python and Flask.
The application allows a user to upload an image and compare the detected face against a database of known faces.

The system calculates facial embeddings using the `face_recognition` library and returns the **top matching results with confidence scores**.

This project demonstrates practical use of:

* Computer Vision
* Facial Recognition
* Web Application Development
* Python Backend Development

The application was developed as part of a **Educational project**.

---

# Features

* Upload image through web interface
* Automatic face detection
* Face encoding using deep learning
* Compare against known face database
* Return **top 5 strongest matches**
* Filter weak matches using distance threshold
* Display:

  * Matched face image
  * Person name
  * Confidence score

---

# Technologies Used

* Python
* Flask (Web Framework)
* face_recognition (Face detection & encoding)
* dlib (Machine learning backend)
* NumPy (Numerical processing)
* OpenCV (Image processing)

---

# Project Structure

```
face_search_app
│
├── app.py
├── requirements.txt
├── README.md
│
├── known_faces
│   ├── messi1.jpg
│   ├── ronaldo.jpg
│   └── ...
│
├── static
│   └── known_faces
│       ├── messi1.jpg
│       ├── ronaldo.jpg
│
├── templates
│   └── index.html
│
└── uploads
```

---

# How the System Works

1. User uploads an image through the web interface
2. The system detects faces in the image
3. The detected face is converted into a **face encoding vector**
4. The encoding is compared against the database
5. The algorithm calculates **face distance values**
6. Only results with **distance < 0.4** are considered strong matches
7. The **top 5 closest matches** are displayed with confidence score

Confidence is calculated as:

```
confidence = (1 - distance) * 100
```

---

# Installation Guide

## 1. Clone the Repository

```
git clone https://github.com/thealmightydeity/face-search-app.git
cd face-search-app
```

## 2. Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Run the Application

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

# Usage

1. Upload an image containing a face
2. Click **Search**
3. The system will return the closest matches from the database

Results include:

* Person name
* Matched image
* Confidence percentage

---

# Limitations

* The system only searches within the **local face database**
* Accuracy depends on image quality and lighting
* Currently processes **one face per upload**
* Does not perform real-time webcam detection

---

# Possible Future Improvements

* Support **multiple faces in uploaded images**
* Display **face detection bounding boxes**
* Add **confidence bars for visual clarity**
* Implement **real-time webcam recognition**
* Integrate with **online image search APIs**
* Improve UI using modern frameworks like React or Bootstrap
* Add a **face dataset management dashboard**

---

# Educational Purpose

This project was developed for **educational and research purposes only**.

It demonstrates how facial recognition systems work but should not be used for unauthorized surveillance or privacy-invasive applications.

---

# Author

Mosses Joseph
BCA Final Year Student

---

# License

This project is open source and available for educational use.

