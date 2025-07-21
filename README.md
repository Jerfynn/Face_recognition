🔍 Face Recognition with Raspberry Pi & Arduino Servo Control
📌 Overview
This project performs real-time face recognition using a webcam and Python. When a known face is detected, the system triggers an Arduino-controlled servo motor to perform an action (e.g., wave or unlock).

🛠️ Hardware Requirements
Raspberry Pi 3/4 (or PC/laptop)

USB Webcam

Arduino UNO/Nano

Servo Motor (e.g., MG996R)

Jumper Wires & Breadboard

USB Cable (for Arduino to Pi communication)

💻 Software & Libraries
Python 3.x

face_recognition

OpenCV

pyserial

pyttsx3 (optional for voice output)

Install using:

bash
Copy
Edit
pip install face_recognition opencv-python pyserial pyttsx3
⚙️ Step-by-Step Procedure
1️⃣ Face Dataset Collection
Capture images of each person using OpenCV or a simple script.

Store them in a folder named /dataset/<person_name>/.

2️⃣ Train the Face Recognizer
Encode all known faces using the face_recognition library.

Save encodings and labels using pickle.

python
Copy
Edit
import face_recognition
import pickle
3️⃣ Real-time Face Recognition
Load the trained encodings.

Access the webcam.

Detect and recognize faces frame-by-frame.

If a known face is detected:

Print/announce the name

Send a command (e.g., via Serial) to the Arduino

4️⃣ Arduino Servo Control
Upload a simple Arduino sketch that listens for serial commands.

On receiving a specific keyword (e.g., "jerfin"), rotate the servo.

Example (Arduino code):

cpp
Copy
Edit
#include <Servo.h>
Servo myServo;
void setup() {
  Serial.begin(9600);
  myServo.attach(9);
}
void loop() {
  if (Serial.available()) {
    String name = Serial.readStringUntil('\n');
    if (name == "jerfin") {
      myServo.write(90);
      delay(1000);
      myServo.write(0);
    }
  }
}
5️⃣ Voice Feedback (Optional)
Use pyttsx3 to add voice messages like:

"Welcome, Jerfin!"

🚀 Run the Project
bash
Copy
Edit
python recognize.py

