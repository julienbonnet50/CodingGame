import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.dirname(p=__file__)))

class Boat:
    def __init__(self, x, y, preferedPosition="", number=0):
        self.x = x
        self.y = y
        self.preferedPosition = preferedPosition
        self.debrisCount = 0
        self.name = "B" + str(number)

    def __str__(self):
        return f"Boat {self.name}(x={self.x}, y={self.y}, preferedPosition={self.preferedPosition})"
