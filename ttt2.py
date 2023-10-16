import tkinter as tk
from tkinter import messagebox
import random

# Создание окна игры
window = tk.Tk()
window.title("Крестики-нолики")

# Определение размера окна и ячеек
cell_size = 100
canvas_size = cell_size * 3

canvas = tk.Canvas(window, width=canvas_size, height=canvas_size)
canvas.pack()

# Инициализация игрового поля
board = [[" " for _ in range(3)] for _ in range(3)]

# Определение текущего игрока
current_player = "X"


# Функция для отрисовки игрового поля
def draw_board():
    canvas.delete("all")

    # Рисование сетки
    for i in range(1, 3):
        canvas.create_line(0, i * cell_size, canvas_size, i * cell_size)
        canvas.create_line(i * cell_size, 0, i * cell_size, canvas_size)

    # Рисование крестиков и ноликов
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x = j * cell_size
                y = i * cell_size
                canvas.create_line(x, y, x + cell_size, y + cell_size)
                canvas.create_line(x, y + cell_size, x + cell_size, y)
            elif board[i][j] == "O":
                x = j * cell_size + cell_size // 2
                y = i * cell_size + cell_size // 2
                radius = cell_size // 2 - 10
                canvas.create_oval(x - radius, y - radius, x + radius, y + radius)


# Функция для обработки хода игрока
def handle_click(event):
    if current_player == "X":
        # Определение координат ячейки, на которую кликнул игрок
        row = event.y // cell_size
        col = event.x // cell_size

        # Проверка, что выбранная ячейка пуста
        if board[row][col] == " ":
            board[row][col] = current_player
            draw_board()

            # Проверка на победу
            if check_win(current_player):
                messagebox.showinfo("Игра окончена!", f"Игрок {current_player} победил!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Игра окончена!", "Ничья!")
                reset_game()
            else:
                switch_player()
                make_ai_move()


# Функция для переключения игрока
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Функция для проверки победы
def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Функция для проверки ничьей
def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


# Функция для сброса игры
def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    draw_board()


# Функция для хода искусственного интеллекта
def make_ai_move():
    # Создание списка доступных ходов
    available_moves = []
    lasti = -1
    lastj = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                if check_win('O'):
                    break
                board[i][j] = 'X'
                if check_win('X'):
                    board[i][j] = " ";
                    lasti = i
                    lastj = j
                else:
                    board[i][j] = " ";
                    if (lasti == -1):
                        lasti = i
                        lastj = j
                available_moves.append((i, j))
            elif (i == 2 and j == 2):
                i = lasti
                j = lastj

    # Выбор случайного доступного хода
    #row, col = random.choice(available_moves)

    # Выполнение хода и отрисовка игрового поля
    board[i][j] = current_player #row col
    draw_board()

    # Проверка на победу
    if check_win(current_player):
        messagebox.showinfo("Игра окончена!", f"Игрок {current_player} победил!")
        reset_game()
    elif check_draw():
        messagebox.showinfo("Игра окончена!", "Ничья!")
        reset_game()
    else:
        switch_player()


# Привязка обработчика кликов к игровому полю
canvas.bind("<Button-1>", handle_click)

# Отрисовка начального игрового поля
draw_board()

# Запуск главного цикла окна
window.mainloop()