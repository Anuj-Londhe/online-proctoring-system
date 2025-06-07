import cv2
import numpy as np

# Load pre-trained face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# For phone detection, let's use a simple color filter as placeholder (phone detection models require deep learning)
# You can replace this with a proper deep learning model later.

def detect_phone(frame):
    # Placeholder: detect a rectangular object (like a phone) based on skin-tone and dark screen color in the hand area
    # This is a naive implementation, just for demonstration.
    # Real phone detection requires training or using a pretrained object detection model (like MobileNet-SSD).
    # Here, we will skip actual phone detection for simplicity.
    return False

def proctoring_system():
    cap = cv2.VideoCapture(0)  # open webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        # Check conditions:
        if len(faces) == 0:
            cv2.putText(frame, "WARNING: No face detected!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif len(faces) > 1:
            cv2.putText(frame, "WARNING: Multiple faces detected!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        else:
            cv2.putText(frame, "Face detected.", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        
        # Phone detection placeholder
        phone_detected = detect_phone(frame)
        if phone_detected:
            cv2.putText(frame, "WARNING: Phone detected!", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow("Online Proctoring", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    proctoring_system()
