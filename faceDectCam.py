
#Credits to https://realpython.com/face-detection-in-python-using-a-webcam/ 
#and https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9

import cv2

#detect webcam
video_capture = cv2.VideoCapture(0)

#haar cascade
cascade = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascade)

while True:

    #webcam capture frame
    out, frame = video_capture.read()

    #grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces in frame
    faces = faceCascade.detectMultiScale(gray, 1.05,6)

    #highlight the faces in the frame
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

    #quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Face Detection", frame)

video_capture.release()
cv2.destroyAllWindows()

