import cv2
import os
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
cascPath = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier(cascPath)


# Open the device at the ID 0

cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print("Could not open video device")

#To set the resolution

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):

    # Capture frame-by-frame

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE

    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print(len(faces))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    #Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()