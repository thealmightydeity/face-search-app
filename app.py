from flask import Flask, render_template, request
import face_recognition
import os
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
KNOWN_FOLDER = "known_faces"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def load_known_faces():

    encodings = []
    names = []

    for file in os.listdir(KNOWN_FOLDER):

        path = os.path.join(KNOWN_FOLDER, file)

        image = face_recognition.load_image_file(path)

        enc = face_recognition.face_encodings(image)

        if len(enc) == 0:
            continue

        encodings.append(enc[0])
        names.append(os.path.splitext(file)[0])

    return encodings, names


# Load database once when app starts
known_encodings, known_names = load_known_faces()


@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    if request.method == "POST":

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html", results=[("No file selected", 0, "")])
        path = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(path)

        image = face_recognition.load_image_file(path)

        enc = face_recognition.face_encodings(image)

        if len(enc) == 0:

            results.append(("No face detected", 0, ""))

        else:

            encoding = enc[0]

            distances = face_recognition.face_distance(
                known_encodings,
                encoding
            )

            indices = np.argsort(distances)

            count = 0

            for i in indices:

                distance = distances[i]

                # Only show strong matches
                if distance < 0.5:

                    confidence = (1 - distance) * 100

                    results.append(
    (known_names[i], round(confidence, 2), known_names[i] + ".jpg")
)

                    count += 1

                if count == 5:
                    break

            if len(results) == 0:
                results.append(("No strong match found", 0, ""))

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)