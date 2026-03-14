import cv2
import numpy as np

def detect_circles(frame):
    detected_circles = []  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    gray = cv2.GaussianBlur(gray, (9, 9), 2)       

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=0.7,
        minDist=20,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=100
    )
   

    if circles is not None:
        for cx, cy, r in circles[0]:
            adj_x = cx - 640
            adj_y = -cy + 360
           

            detected_circles.append((adj_x, adj_y, r))

            cv2.circle(frame, (int(cx), int(cy)), int(r), (0, 0, 255), 2)   
            cv2.circle(frame, (int(cx), int(cy)), 2, (0, 255, 0), 3)        
    return detected_circles