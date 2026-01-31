import cv2

def open_camera(index=0):       #0번 카메라 열기/노트북에서는 내장 카메라가 0번/EOS Webcam Program이 있으면 이 프로그램이 자동으로 0번으로 설정
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("카메라 인식 불가")
    return cap


#도구 역할만 진행
if __name__ == "__main__":
    open_camera()
    print("camera.py OK")