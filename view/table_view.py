""" Table view generator
"""

import cv2
import numpy as np
from controller.table import Table, FieldStatus


def draw_table(table: Table, field_scale = float):
    field_odd = cv2.imread(r"view\images\odd_field.jpg")
    field_pair = cv2.imread(r"view\images\pair_field.jpg")
    field_conquered = cv2.imread(r"view\images\conquered_field.jpg")
    field_bomb = cv2.imread(r"view\images\bomb_field.jpg")
    field_0 = cv2.imread(r"view\images\0.jpg")
    field_1 = cv2.imread(r"view\images\1.jpg")
    field_2 = cv2.imread(r"view\images\2.jpg")
    field_3 = cv2.imread(r"view\images\3.jpg")
    field_4 = cv2.imread(r"view\images\4.jpg")
    field_5 = cv2.imread(r"view\images\5.jpg")
    field_6 = cv2.imread(r"view\images\6.jpg")
    field_7 = cv2.imread(r"view\images\7.jpg")
    field_8 = cv2.imread(r"view\images\8.jpg")

    field_odd = cv2.resize(field_odd, (int(field_scale * 100), int(field_scale * 100)))
    field_pair = cv2.resize(field_pair, (int(field_scale * 100), int(field_scale * 100)))
    field_conquered = cv2.resize(field_conquered, (int(field_scale * 100), int(field_scale * 100)))
    field_bomb = cv2.resize(field_bomb, (int(field_scale * 100), int(field_scale * 100)))
    field_0 = cv2.resize(field_0, (int(field_scale * 100), int(field_scale * 100)))
    field_1 = cv2.resize(field_1, (int(field_scale * 100), int(field_scale * 100)))
    field_2 = cv2.resize(field_2, (int(field_scale * 100), int(field_scale * 100)))
    field_3 = cv2.resize(field_3, (int(field_scale * 100), int(field_scale * 100)))
    field_4 = cv2.resize(field_4, (int(field_scale * 100), int(field_scale * 100)))
    field_5 = cv2.resize(field_5, (int(field_scale * 100), int(field_scale * 100)))
    field_6 = cv2.resize(field_6, (int(field_scale * 100), int(field_scale * 100)))
    field_7 = cv2.resize(field_7, (int(field_scale * 100), int(field_scale * 100)))
    field_8 = cv2.resize(field_8, (int(field_scale * 100), int(field_scale * 100)))

    dimensions = (int(table.dimensions[0] * field_scale * 100), int(table.dimensions[1] * field_scale * 100))

    img = np.zeros((dimensions[1], dimensions[0], 3), dtype=np.uint8)

    for y in range(table.dimensions[1]):
        for x in range(table.dimensions[0]):
            status = table.table[x][y].status
            field = table.table[x][y]
            if status == FieldStatus.UNCHECKED:
                if (x + y) % 2 == 0:
                    img_field = field_pair
                else:
                    img_field = field_odd

            elif status == FieldStatus.CLICKED:
                if field.neighbour_bombs == 0:
                    img_field = field_0
                elif field.neighbour_bombs == 1:
                    img_field = field_1
                elif field.neighbour_bombs == 2:
                    img_field = field_2
                elif field.neighbour_bombs == 3:
                    img_field = field_3
                elif field.neighbour_bombs == 4:
                    img_field = field_4
                elif field.neighbour_bombs == 5:
                    img_field = field_5
                elif field.neighbour_bombs == 6:
                    img_field = field_6
                elif field.neighbour_bombs == 7:
                    img_field = field_7
                elif field.neighbour_bombs == 8:
                    img_field = field_8
            
            elif status == FieldStatus.CONQUERED:
                img_field = field_conquered

            elif status == FieldStatus.EXPLODED:
                img_field = field_bomb
        
            x1, x2 = x * img_field.shape[1], (x + 1) * img_field.shape[1]
            y1, y2 = y * img_field.shape[0], (y + 1) * img_field.shape[0]

            img[y1:y2, x1:x2, :] = img_field[:,:,:]

    return img