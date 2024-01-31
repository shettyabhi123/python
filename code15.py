import cv2
import os

# Open the video capture device
video_capture = cv2.VideoCapture(0)

# Create directories for persons A and B
person_a_dir = 'person_a'
person_b_dir = 'person_b'
os.makedirs(person_a_dir, exist_ok=True)
os.makedirs(person_b_dir, exist_ok=True)

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.haarcascades +'haarcascade_frontalface_default.xml')

while True:
    # Capture a frame from the video
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Crop the faces of persons A and B from the frame
    person_a_face = None
    person_b_face = None
    for (x, y, w, h) in faces:
        if x < frame.shape[1] / 2:
            person_a_face = frame[y:y+h, x:x+w]
        else:
            person_b_face = frame[y:y+h, x:x+w]

    # Save the faces of persons A and B to files
    if person_a_face is not None:
        cv2.imwrite(os.path.join(person_a_dir, 'person_a.jpg'), person_a_face)
    if person_b_face is not None:
        cv2.imwrite(os.path.join(person_b_dir, 'person_b.jpg'), person_b_face)

    # Display the faces of persons A and B
    if person_a_face is not None:
        cv2.imshow('Person A', person_a_face)
    if person_b_face is not None:
        cv2.imshow('Person B', person_b_face)

    # Exit the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device
video_capture.release()

# Close all windows
cv2.destroyAllWindows()
