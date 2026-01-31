#calibration에서 구한 parameters를 이용해 레이져 좌표로 변환

def transform_coordinates(detected_circles, params):    #dected_circles와 params를 호출
   
    if params is None:
        print("캘리브레이션 안 됨")
        return []

    a, b, c, d = params
    transformed = []

    print(f"---- 변환 좌표 & 감지된 원의 개수:({len(detected_circles)}) ----")      #f는 {}안에 들어있는 함수를 자동으로 채워서 출력시킴

    for i, (x, y, r) in enumerate(detected_circles):
        img_x = a * x + b
        img_y = c * y + d

        #이미 detected_circles에서 원점 좌표변환 시켜놓음

        transformed.append((img_x, img_y, 0, r))        #x,y 좌표 그리고 평면이라서 z=0

        #출력은 앞에 5개 값만 진행 (0~4)
        if i < 5:
            print(f"[{i}] Laser Coord → X={img_x:.2f}, Y={img_y:.2f}")
        elif i == 5:
            print("... (이하 생략)")

    return transformed
