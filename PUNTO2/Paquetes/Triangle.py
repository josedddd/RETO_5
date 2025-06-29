from math import sin, degrees, acos, radians

from Paquetes.Shape import Shape
from Paquetes.Line import Line

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def compute_edges(self): 
        ## Orden de colocar los vertices 
        # [Vertice superior, Vertice_inferior derecho, Vertice inferior izquierdo]
        
        self._edge1 = Line(self._vertices[0], self._vertices[1])
        self._edge2 = Line(self._vertices[1], self._vertices[2])
        self._edge3 = Line(self._vertices[2], self._vertices[0])
        self._leng_edge1= self._edge1.compute_length()
        self._leng_edge2= self._edge2.compute_length()
        self._leng_edge3= self._edge3.compute_length()


    def get_edges(self):
        self.compute_edges()
        return [
        {
            "name": "A",
            "start": (self._edge1.point_start.x, self._edge1.point_start.y),
            "end": (self._edge1.point_end.x, self._edge1.point_end.y),
            "length": self._leng_edge1
        },
        {
            "name": "B",  
            "start": (self._edge2.point_start.x, self._edge2.point_start.y),
            "end": (self._edge2.point_end.x, self._edge2.point_end.y),
            "length": self._leng_edge2
        },
        {
            "name":"C",
            "start": (self._edge3.point_start.x, self._edge3.point_start.y),
            "end": (self._edge3.point_end.x, self._edge3.point_end.y),
            "length": self._leng_edge3
        }
    ]

    def compute_inner_angles(self):
        self.compute_edges()
         #### El orden del calculo de los angulos es 
         # [Angulo opuesto al lado "A", Angulo opuesto al Lado B, Angulo opuesto al lado C]
        self.compute_edges()
        cos_angle_edge1= (self._leng_edge3**2 + self._leng_edge2**2 - self._leng_edge1**2) / (
            2 * self._leng_edge3* self._leng_edge2)
        self.angle_edge_1 = degrees(acos(cos_angle_edge1))
        cos_angle_edge2 = (self._leng_edge3**2 + self._leng_edge1**2 - self._leng_edge2**2) / (
            2 * self._leng_edge3* self._leng_edge1)
        self.angle_edge_2 = degrees(acos(cos_angle_edge2))
        cos_angle_edge3 = (self._leng_edge2**2 + self._leng_edge1**2 - self._leng_edge3**2) / (
            2 * self._leng_edge2* self._leng_edge1)
        self.angle_edge_3 = degrees(acos(cos_angle_edge3))
       
        return[self.angle_edge_1, self.angle_edge_2, self.angle_edge_3]
        
    def compute_area(self) -> float:
        self.compute_edges()
        self.compute_inner_angles()
        return (1/2*self._leng_edge1*self._leng_edge2*sin(radians(self.angle_edge_3)))
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return (self._leng_edge1+self._leng_edge2 +self._leng_edge3)

