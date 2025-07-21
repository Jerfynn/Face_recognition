import cv2
import os

# Set person name and dataset folder
person_name = "Nihi"  # Change this each time
dataset_dir = "dataset"

# Create folder for person if not exists
person_path = os.path.join(dataset_dir, person_name)
os.makedirs(person_path, exist_ok=True)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

count = 0
print("📸 Capturing faces... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y + h, x:x + w]
        filename = os.path.join(person_path, f"{count}.jpg")
        cv2.imwrite(filename, face)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"Image {count}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Face Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 70:
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Face images saved successfully.")
