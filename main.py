
from controller.table import Table, FieldStatus
from view.table_view import draw_table, cv2
from tkinter import messagebox

dim = (20, 20)
bombs = 30
scale = 0.5

table = Table(dim, bombs)

game_over = False

def callback_(event, y, x, flags, params):
    x_index = y // int(100 * scale)
    y_index = x // int(100 * scale)

    global game_over
    if game_over:
        return
    
    if event == 1:
        if table.click(x_index, y_index) == FieldStatus.EXPLODED:
            game_over = True
            cv2.imshow("Campo Minado", draw_table(table, scale))
            messagebox.showinfo("Fim de jogo", "Você pisou em uma bomba...")
            return
        
    elif event == 2:
        table.conquer(x_index, y_index)
        

    if table.check_is_over():
        game_over = True
        cv2.imshow("Campo Minado", draw_table(table, scale))
        messagebox.showinfo("Parabéns!", "Você evitou todas as bombas!")
        return

    cv2.imshow("Campo Minado", draw_table(table, scale))

cv2.namedWindow('Campo Minado', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Campo Minado', callback_)

# while not game_over:
#     cv2.imshow("Campo Minado", draw_table(table, scale))
#     cv2.waitKey(0)

cv2.imshow("Campo Minado", draw_table(table, scale))
cv2.waitKey(0)
