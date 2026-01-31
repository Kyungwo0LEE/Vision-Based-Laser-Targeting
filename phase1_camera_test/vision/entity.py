#정보의 구성방식 정의

from dataclasses import dataclass

@dataclass      #데이터 클래스를 python에 정의
class Entity:
    name: str       
    x: float        
    y: float
    z: float
    width: float
    height: float

    #x,y,z는 레이저 좌표
    #변수 선언
    # width=height/원이니깐

    def __repr__(self):
        return(
            f"{self.name} | "
            f"X={float(self.x):.2f}, "
            f"Y={float(self.y):.2f}, "
            f"Z={float(self.z):.2f}, "
            f"W={float(self.width):.2f}, "
            f"H={float(self.height):.2f} "
            )

    #print 눌렀을 때 보이는 문자열 정리