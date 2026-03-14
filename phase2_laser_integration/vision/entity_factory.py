import time
from vision.entity import Entity

def build_entities_from_coordinates(transformed_coords):
    """
    transformed_coords:
    [(x, y, z, r), ...]
    """
    entities = []  

    for x, y, z, r in transformed_coords:
        width = 2 * r * 0.115          
        height = width                  
        name = f"Entity_{int(time.time() * 1000)}"

        entity = Entity(
            name=name,
            x=x,
            y=y,
            z=z,
            width=width,
            height=height
        )

        entities.append(entity)

    return entities

