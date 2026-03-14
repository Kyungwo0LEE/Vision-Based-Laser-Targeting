import cv2

def open_camera(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("카메라 인식 불가")
    return cap


#도구 역할만 진행
if __name__ == "__main__":
    open_camera()
    print("camera.py OK")