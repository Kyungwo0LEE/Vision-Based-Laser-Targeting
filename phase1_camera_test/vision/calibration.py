def calibrate(detected_circles):

    if len(detected_circles) < 3:
        print("캘리브레이션 실패: 원 3개 필요")
        return None

    circles = sorted(detected_circles, key=lambda x: float(x[0]))           #x좌표 기준으로 원 정렬

    X1, Y1, _ = circles[0]      #가장 왼쪽 원
    X3, Y3, _ = circles[2]      #가장 오른쪽 원
    #늘 3개의 원이 필요. 많아도 원쪽 기준으로 1,3번째 원만 Calibration에 사용

    #X_laser=a*X_cam+b
    #Y_laser=b*Y_cam+d
    #60mm laser coord기준 

    a = 60 / (X3 - X1)
    b = -30 - a * X1
    c = 60 / (Y3 - Y1)
    d = -30 - c * Y1

    #레이저 좌표 변환에 필요한 parameters 구하기

    print("[Calibration 완료]\n")
    print(f"a={a:.4f}, b={b:.4f}, c={c:.4f}, d={d:.4f}")

    return a,b,c,d
    

#csv로 데이터 저장하기
import csv, os
from datetime import datetime

def save_calibration_csv(params):
    a,b,c,d=params
    os.makedirs("logs/calibration", exist_ok=True)

    filename = (
        "logs/calibration/"
        f"calibration_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    )

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "a", "b", "c", "d"])
        writer.writerow([
            datetime.now().isoformat(),a,b,c,d])

    print(f"[CALIBRATION] CSV 저장 완료 → {filename}")