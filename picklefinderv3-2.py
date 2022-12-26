import numpy as np
import cv2 as cv 



capture = cv.VideoCapture(0)
capture.set(3, 640)
capture.set(4,480)

#import cascade
faceCascade = cv.CascadeClassifier('C:\\Users\\Nick\\pickleFinder\\cascade.xml')

if not capture.isOpened():
    print("cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    success, img = capture.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

     # Getting corners around the pickle
    # 1.3 = scale factor, 5 = minimum neighbor can be detected
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)  

     # drawing bounding box around pickle
    for (x, y, w, h) in faces:
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)

    # Display the resulting frame
    cv.imshow('frame', img)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
capture.release()
cv.destroyAllWindows()

