import cv2
import numpy as np

def detect_circles(frame):
    detected_circles = []   #원 검출하기

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #회색으로 변환하기
    gray = cv2.GaussianBlur(gray, (9, 9), 2)         #블러처리하기

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
    #원을 판단하는 기준

    #cx는 원의 중심 x좌표 (카메라)
    #cy는 원의 중심 y좌표 (카메라)

    if circles is not None:
        for cx, cy, r in circles[0]:
            adj_x = cx - 640
            adj_y = -cy + 360
            #카메라의 원점 설정
            #1280 * 720
            #중점을 (0,0)으로 재설정
            #카메라 기준

            detected_circles.append((adj_x, adj_y, r))      #검출한 원 추가

            cv2.circle(frame, (int(cx), int(cy)), int(r), (0, 0, 255), 2)   #원 검출/반지름/빨간색/두께 2
            cv2.circle(frame, (int(cx), int(cy)), 2, (0, 255, 0), 3)        #원 검출/반지름 2/초록색/두께 3/사실상 점

    return detected_circles