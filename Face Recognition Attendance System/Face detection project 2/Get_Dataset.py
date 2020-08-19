# Import OpenCV2 for image processing

import cv2
import os


face_id = input('Enter Your ID :::  ')

# Start capturing video 
vid_cam = cv2.VideoCapture(0)
vid_cam.set(3, 1080)
vid_cam.set(4, 720)


# Detect object in video stream using Haarcascade Classifier
face_detector = cv2.CascadeClassifier('D:/Programs/Python Project/FINAL YEAR PROJECT 2/Face detection project 2/'
                                      'haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0


# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 7)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("D:/Programs/Python Project/FINAL YEAR PROJECT 2/"
                    "Faces Dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        print('Image Number ' + str(count) + ' Is Saved')

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    elif count == 50:
        print('Dataset Is Successfully Collected !!! ')
        break


# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
