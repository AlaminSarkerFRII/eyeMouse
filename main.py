import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
face_mash = mp.solutions.face_mesh.FaceMesh()
while True:
    __,frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mash.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    print(landmark_points)
    cv2.imshow('eye mouse',frame)
    cv2.waitKey(1)
