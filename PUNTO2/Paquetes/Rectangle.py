from Paquetes.Shape import Shape
from Paquetes.Line import Line


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    
    def compute_edges(self):   
        #Estructura de vertices de un rectangulo: 
        #[point_left_up, point_right_up, point_right_down, point_left_dowm]
        self._edgeH_up = Line(self._vertices[0], self._vertices[1])
        self._edgeH_down = Line(self._vertices[3], self._vertices[2])
        self._edgeV_left = Line(self._vertices[0], self._vertices[3])
        self._edgeV_right = Line(self._vertices[1], self._vertices[2])

    def get_edges(self) -> list:
        self.compute_edges()
        return [
            {
                "name": "top edge",
                "start": (self._edgeH_up.point_start.x, self._edgeH_up.point_start.y),
                "end": (self._edgeH_up.point_end.x, self._edgeH_up.point_end.y),
                "length": self._edgeH_up.compute_length()
            },
            {
                "name": "bottom edge",
                "start": (self._edgeH_down.point_start.x, self._edgeH_down.point_start.y),
                "end": (self._edgeH_down.point_end.x, self._edgeH_down.point_end.y),
                "length": self._edgeH_down.compute_length()
            },
            {
                "name": "left edge",
                "start": (self._edgeV_left.point_start.x, self._edgeV_left.point_start.y),
                "end": (self._edgeV_left.point_end.x, self._edgeV_left.point_end.y),
                "length": self._edgeV_left.compute_length()
            },
            {
                "name": "right edge",
                "start": (self._edgeV_right.point_start.x, self._edgeV_right.point_start.y),
                "end": (self._edgeV_right.point_end.x, self._edgeV_right.point_end.y),
                "length": self._edgeV_right.compute_length()
            }
        ]

    def compute_area(self) -> float:
        self.compute_edges()
        return (self._edgeH_up.compute_length()*self._edgeV_right.compute_length() )
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return 2*self._edgeH_up.compute_length()+2*self._edgeV_right.compute_length()
    
    def compute_inner_angles(self):
        return [90, 90, 90, 90]



