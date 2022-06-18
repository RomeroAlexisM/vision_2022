import numpy as np
import cv2
import cv2.aruco as aruco
dict_aruco= aruco.Dictionary_get(cv2.aruco.DICT_5X5_250)
parameters = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    bboxs, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(frame, dict_aruco, parameters=parameters)
    markerCorners = markerIds, rejectedCandidates
    
    if markerIds is not None:
        for i, corner in zip(markerIds, markerCorners):
            print('ID: {}; Corners: {}'.format(i, corner))
            frame = cv2.putText(frame, "Id {0}".format(i), (int(corner[0][0][0]+20, int(corner[0][0][1]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)))
            
        frame = aruco.drawDetectedMarkers(frame, markerCorners, borderColor=(0, 255, 0))
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
