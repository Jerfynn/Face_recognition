import cv2
import numpy as np
import pyttsx3
import os

# Load face recognizer and labels
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define labels (you can customize this based on your folders)
label_dict = {
    0: "Jerfin",
    1: "Nihi",
    2: "Subin"
}

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Start video capture
cap = cv2.VideoCapture(0)

last_spoken = None  # To avoid repeating names continuously

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        id_, confidence = recognizer.predict(roi_gray)

        if confidence < 70:
            name = label_dict.get(id_, "Unknown")
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if name != last_spoken:
                print(f"🎤 Speaking: {name}")
                engine.say(f"Welcome {name}")
                engine.runAndWait()
                last_spoken = name
        else:
            cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Face Recognition with Voice", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
