#Credits to https://realpython.com/face-detection-in-python-using-a-webcam/ 
#and https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9

import cv2

imagePath = "picture.jpg" 
cascade = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascade)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 1.05,6)

if len(faces) == 0:
    print("No faces found")

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0),2)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

