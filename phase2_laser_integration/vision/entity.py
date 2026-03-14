from dataclasses import dataclass

@dataclass
class Entity:
    name: str       
    x: float        
    y: float
    z: float
    width: float
    height: float

    # width=height

    def __repr__(self):
        return(
            f"{self.name} | "
            f"X={float(self.x):.2f}, "
            f"Y={float(self.y):.2f}, "
            f"Z={float(self.z):.2f}, "
            f"W={float(self.width):.2f}, "
            f"H={float(self.height):.2f} "
            )
