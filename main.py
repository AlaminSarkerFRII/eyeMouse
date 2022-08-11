import cv2
cam = cv2.VideoCapture(0)
while True:
    __,frame = cam.read()
    cv2.imshow('eye mouse',frame)
    cv2.waitKey(1)
