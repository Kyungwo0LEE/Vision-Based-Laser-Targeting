#정보를 실제로 생성

import time
from vision.entity import Entity

def build_entities_from_coordinates(transformed_coords):        #transformed_coords를 호출
    """transformed_coords : [(x, y, z, r), ...]"""
    #윗 문장은 그냥 내가 기억할라고 쓴 주석

    entities = []   #Entity의 임시 저장 리스트 in RAM

    for x, y, z, r in transformed_coords:
        width = 2 * r * 0.115           #0.115는 configure/params에서 가져온 데이터 값
        height = width                  #원이니깐 세로=가로 
        name = f"Entity_{int(time.time() * 1000)}"

        entity = Entity(
            name=name,
            x=x,
            y=y,
            z=z,
            width=width,
            height=height
        )

        #entity.py 에서의 class Entity 이용하기
        
        entities.append(entity)

    return entities