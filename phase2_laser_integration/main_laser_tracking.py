import cv2

from vision.camera import open_camera
from vision.detect_circle import detect_circles
from vision.calibration import calibrate, save_calibration_csv
from vision.transform import transform_coordinates
from vision.entity_factory import build_entities_from_coordinates
from vision.logger import TrackingLogger
from control.laser_client import LaserClient
import time
import random

def main():
    cap = open_camera()
    logger = TrackingLogger()
    laser=LaserClient()

    tracking = False
    frame_count = 0
    params = None

    print("조작 방법:")
    print(" c : 캘리브레이션")
    print(" t : 트래킹 ON/OFF")
    print(" ESC : 종료")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임 읽기 실패")
            break

        detected_circles = detect_circles(frame)

        
        if tracking and params is not None:
            frame_count = frame_count+1

            if frame_count % 30 == 0:       #30프레임에 한 번씩 촬영
                transformed = transform_coordinates(detected_circles,params)
                entities = build_entities_from_coordinates(transformed)
                
                logger.log(entities)
                print(f"Entity-ready data ({len(entities)} entities):")

                if entities:
                    e=random.choice(entities)
                    print("random send-->", e)
                  
                    laser.send_coordinate(e.x, e.y, e.z)   # C# 레이저 서버로 엔티티 데이터 전송

                    

        cv2.imshow("Test Camera(No Laser)", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break

        elif key == ord('c'):
            params = calibrate(detected_circles)
            if params is not None:
                save_calibration_csv(params)

        elif key == ord('t'):
            tracking = not tracking
            print("[TRACKING]", "ON" if tracking else "OFF")

    cap.release()
    cv2.destroyAllWindows()
    logger.close()

if __name__ == "__main__":
    main()
