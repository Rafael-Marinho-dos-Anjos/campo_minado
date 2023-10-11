""" Field module
"""

from model.field_status import FieldStatus

class Field():
    status = FieldStatus.UNCHECKED
    neighbour_bombs = None

    def __init__(self, has_bomb: bool = False) -> None:
        self.has_bomb = has_bomb
    
    def conquer(self):
        if self.status == FieldStatus.CLICKED:
            return
        
        elif self.status == FieldStatus.CONQUERED:
            self.status = FieldStatus.UNCHECKED

        elif self.status == FieldStatus.UNCHECKED:
            self.status = FieldStatus.CONQUERED

    def check(self):
        if self.status == FieldStatus.CLICKED or self.status == FieldStatus.CONQUERED:
            return
        
        if self.status == FieldStatus.UNCHECKED:
            if self.has_bomb:
                self.status = FieldStatus.EXPLODED
            else:
                self.status = FieldStatus.CLICKED
