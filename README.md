ONLINE PROCTORING SYSTEM - Face Detection Prototype

--------------------------------------------------------

This project is a simple Python-based online proctoring system prototype that uses OpenCV’s pre-trained Haar Cascade classifier to detect faces in real time via webcam. It is designed to monitor the test-taker by ensuring only one face is visible and to raise warnings when no face or multiple faces are detected.

Currently, phone detection is a placeholder and not implemented — advanced phone/object detection would require deep learning models.

--------------------------------------------------------

FEATURES:

- Real-time face detection from webcam video stream
- Warning messages when:
  - No face detected (possible absence of test-taker)
  - Multiple faces detected (possible cheating)
- Placeholder for phone detection (non-functional in this version)
- Simple GUI window displaying video feed and warnings
- Exit the application by pressing 'q'

--------------------------------------------------------

REQUIREMENTS:

- Python 3.6 or higher
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)
- Webcam connected to the system
