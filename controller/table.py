""" Table model
"""

from random import choice
from model.field import Field
from model.field_status import FieldStatus


class Table():
    def __init__(self,
                 dimension: tuple = (15, 15),
                 bombs: int = 20) -> None:
        self.dimensions = dimension
        self.table = [[Field() for j in range(dimension[1])] for i in range(dimension[0])]
        bomb_count = 0
        while bomb_count < bombs:
            field = self.table[choice(range(dimension[0]))][choice(range(dimension[1]))]
            if not field.has_bomb:
                field.has_bomb = True
                bomb_count += 1
    
    def click(self, x: int, y: int):
        field = self.table[x][y]
        if field.status in (FieldStatus.CLICKED, FieldStatus.CONQUERED):
            return
        
        field.check()

        if field.status == FieldStatus.EXPLODED:
            for line in self.table:
                for fld in line:
                    if fld.has_bomb:
                        fld.status = FieldStatus.EXPLODED
        
        elif field.status == FieldStatus.CLICKED:
            neighbours = [
                [x - 1, y - 1],
                [x, y - 1],
                [x - 1, y],
                [x + 1, y - 1],
                [x - 1, y + 1],
                [x, y + 1],
                [x + 1, y],
                [x + 1, y + 1]
            ]
            bombs = 0
            
            for nghbr in neighbours:
                try:
                    if self.table[nghbr[0]][nghbr[1]].has_bomb:
                        if nghbr[0] != -1 and nghbr[1] != -1:
                            bombs += 1
                except:
                    pass
            
            field.neighbour_bombs = bombs
            
            if bombs == 0:
                for nghbr in neighbours:
                    if -1 in nghbr:
                        continue
                    try:
                        self.click(nghbr[0], nghbr[1])
                    except:
                        pass
        
        return field.status
    
    def conquer(self, x: int, y: int):
        self.table[x][y].conquer()
    
    def check_is_over(self):
        bombs_untracked = False
        free_fields_untracked = False
        for line in self.table:
            for field in line:
                if field.has_bomb and field.status != FieldStatus.CONQUERED:
                    bombs_untracked  =True
                
                if field.status != FieldStatus.CLICKED and not field.has_bomb:
                    free_fields_untracked = True
                
                if bombs_untracked and free_fields_untracked:
                    return False
        return True
