from math import atan2, degrees
from Paquetes.Point import Point

class Line:
    def __init__(self, point_start: Point, point_end: Point):
        self.point_start = point_start
        self.point_end = point_end
        self.length = ((point_end.x - point_start.x) ** 2 + (point_end.y - point_start.y) ** 2) ** 0.5
        self.slope = atan2((point_end.y - point_start.y),(point_end.x - point_start.x))
        self.slope_degrees = degrees(self.slope)

    def compute_length(self) -> float:
        return self.length