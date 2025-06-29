
class Shape():
    def __init__(self):
        pass

    def set_is_regular(self, is_regular:bool):
        self._is_regular=is_regular

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, vertices:list):
        self._vertices=vertices

    def get_vertices(self) -> list:
        return [(self._vertices[x].x, self._vertices[x].y) for x in range(len(self._vertices))]
    
    def compute_edges(self):
        pass

    def get_edges(self):
        pass

    def compute_inner_angles(self):
        pass        

    def compute_perimeter(self):
        pass

    def compute_area(self):
        pass