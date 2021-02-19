
#Credits to https://realpython.com/face-detection-in-python-using-a-webcam/ 
#and https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9

import cv2

#detect webcam
video_capture = cv2.VideoCapture(0)
cascade = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascade)

while True:

    out, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.05,6)

    if len(faces) == 0:
        print("No faces found")

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Face Detection", frame)

video_capture.release()
cv2.destroyAllWindows()

