import cv2
import numpy as np
import os

# Path to dataset folder
dataset_path = "dataset"

# Initialize the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Arrays to hold face data and labels
faces = []
labels = []
label_dict = {}   # e.g., {0: "jerfin", 1: "subin"}
current_label = 0

# Loop through each person folder in dataset/
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_folder):
        continue

    label_dict[current_label] = person_name

    for filename in os.listdir(person_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(person_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            faces.append(image)
            labels.append(current_label)

    current_label += 1

# Train recognizer
print("🧠 Training recognizer...")
recognizer.train(faces, np.array(labels))
print("✅ Training complete.")

# Save the model and label dictionary
recognizer.save("trained_model.yml")
np.save("labels.npy", label_dict)

print("💾 Model and labels saved.")
