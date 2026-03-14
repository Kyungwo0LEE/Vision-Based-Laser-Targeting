def transform_coordinates(detected_circles, params):
    if params is None:
        print("캘리브레이션 안 됨")
        return []

    a, b, c, d = params
    transformed = []

    print(f"---- 변환 좌표 & 감지된 원의 개수:({len(detected_circles)}) ----")

    for i, (x, y, r) in enumerate(detected_circles):
        img_x = a * x + b
        img_y = c * y + d

        if abs(img_x) > 40 or abs(img_y) > 40:
            continue
        

        transformed.append((img_x, img_y, 0, r))

        #출력은 앞에 5개 값만 진행 (0~4)
        if i < 5:
            print(f"[{i}] Laser Coord → X={img_x:.2f}, Y={img_y:.2f}")
        elif i == 5:
            print("... (이하 생략)")

    return transformed
