from tkinter import *
from tkinter import messagebox
import random

current_game = ''
gamemode = "Double Player"
difficulty = "Easy"
reverse = 1
symbol = "cross"
computer_move = 1

def init_game_win():
    global game_win
    global img_square
    global img_cross
    global img_circle
    global grid
    global new_gamemode
    global new_difficulty
    global new_reverse
    
    game_win=Tk()
    game_win.geometry('1500x750')
    game_win.title("Tic tac toe")

    img_square = PhotoImage(file = r"Square.png")
    img_cross = PhotoImage(file = r"Cross.png")
    img_circle = PhotoImage(file = r"Circle.png")

    frame_settings = Frame(game_win)
    frame_settings.place(relx = 0.5, rely=0.1, anchor='center')
    
    frame_grid = Frame(game_win)
    frame_grid.place(relx=0.5, rely=0.5, anchor='center')

    new_gamemode = StringVar(value = 'Double Player')
    dd_gamemode = OptionMenu(frame_settings, new_gamemode, *['Double Player', 'Single Player'], command = update_settings)
    dd_gamemode.grid(row=0, column=0)

    new_difficulty = StringVar(value = 'Easy')
    dd_difficulty = OptionMenu(frame_settings, new_difficulty, *['Easy', 'Medium', 'Hard'], command = update_settings)
    dd_difficulty.grid(row=1, column=0)

    new_reverse = IntVar(value = 1)
    cb_reverse = Checkbutton(frame_settings, text = 'Reverse Tic tac toe', variable = new_reverse, onvalue = -1, offvalue = 1, command = lambda: update_settings(new_reverse.get()))
    cb_reverse.grid(row=2, column=0)

    btn_newgame = Button(frame_settings, text="Start new game", command = reset)
    btn_newgame.grid(row=3, column=0)
    
    btn_square_1 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(1))
    btn_square_1.grid(row=0, column=0)

    btn_square_2 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(2))
    btn_square_2.grid(row=0, column=1)

    btn_square_3 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(3))
    btn_square_3.grid(row=0, column=2)

    btn_square_4 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(4))
    btn_square_4.grid(row=1, column=0)

    btn_square_5 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(5))
    btn_square_5.grid(row=1, column=1)

    btn_square_6 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(6))
    btn_square_6.grid(row=1, column=2)

    btn_square_7 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(7))
    btn_square_7.grid(row=2, column=0)

    btn_square_8 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(8))
    btn_square_8.grid(row=2, column=1)

    btn_square_9 = Button(frame_grid, image = img_square, borderwidth = 0, command = lambda: play_move(9))
    btn_square_9.grid(row=2, column=2)

    grid = [btn_square_1, btn_square_2, btn_square_3, btn_square_4, btn_square_5, btn_square_6, btn_square_7, btn_square_8, btn_square_9]
    
    game_win.mainloop()

def update_settings(newval):
    global gamemode
    global difficulty
    global reverse
    if not(new_gamemode.get() == gamemode and new_difficulty.get() == difficulty and new_reverse.get() == reverse):
        if current_game != '':
            response = messagebox.askquestion("Reset game?", "Do you want to start a new game?")
            if response == 'no':
                new_gamemode.set(gamemode)
                new_difficulty.set(difficulty)
                new_reverse.set(reverse)
            else:
                gamemode = new_gamemode.get()
                difficulty = new_difficulty.get()
                reverse = new_reverse.get()
                reset()
        else:
            gamemode = new_gamemode.get()
            difficulty = new_difficulty.get()
            reverse = new_reverse.get()
            reset()

def reset():
    global current_game
    global grid
    global gamemode
    global difficulty
    global symbol
    global computer_move
    
    for button in grid:
        button['image'] = img_square
    current_game = ''
    symbol = "cross"
    if gamemode == "Single Player":
        if computer_move == 1:
            computer_move = 2
        else:
            computer_move = 1
    ready()
    return()

def play_move(square):
    global current_game
    
    if str(square) not in current_game:
        select_square(square)

    ready()

#Checks for wins and plays computer moves
def ready():
    global current_game
    global gamemode
    global difficulty
    global reverse
    global computer_move
    
    if gamemode == "Double Player":
        win = check_win(current_game, 1)
        if win == 10:
            messagebox.showinfo("Game Over", "Cross wins")
            reset()
        elif win == -10:
            messagebox.showinfo("Game Over", "Circle wins")
            reset()
        elif win == 0:
            messagebox.showinfo("Game Over", "It is a draw")
            reset()
    else:
        win = check_win(current_game, computer_move)
        if win!= None:
            if win == 10:
                messagebox.showinfo("Game Over", "Computer wins")
                reset()
            elif win == -10:
                messagebox.showinfo("Game Over", "Player wins")
                reset()
            elif win == 0:
                messagebox.showinfo("Game Over", "It is a draw")
                reset()
        elif (len(current_game) + 1) % 2 == computer_move % 2:
             move = computer_play(current_game, difficulty, reverse)
             select_square(move)
             ready()
    
    return()

def select_square(square):
    global grid
    global current_game
    global symbol
    global img_square
    global img_cross
    global img_circle
    print(current_game)
    if symbol == "cross":
        grid[square-1]['image'] = img_cross
        symbol = "circle"
    else:
        grid[square-1]['image'] = img_circle
        symbol = "cross"
    
    current_game = current_game + str(square)

    return()

def check_win(game, player):
    square_values = {}
    winner = 0

    #Creates dictionary with square no. and player who played it
    for count, move in enumerate(game, start = 0):
        if count % 2 == 0:
            square_values[int(move)-1] = 1
        else:
            square_values[int(move)-1] = 2

    for square in range(9):
        if square not in square_values:
            square_values[square] = 0

    #Checks for win in rows and columns
    for num in range(3):
        if square_values[3*num + 0] == square_values[3*num + 1] and square_values[3*num + 0] == square_values[3*num + 2] and square_values[3*num + 0] != 0:
            winner = square_values[3*num + 0]
        elif square_values[3*0 + num] == square_values[3*1 + num] and square_values[3*0 + num] == square_values[3*2 + num] and square_values[3*0 + num] != 0:
            winner = square_values[3*0 + num]

    #Checks for win in diagonals
    if (square_values[0] == square_values[4] and square_values[0] == square_values[8] and square_values[0] != 0) or (square_values[2] == square_values[4] and square_values[2] == square_values[6] and square_values[2] != 0):
        winner = square_values[4]

    if winner == 0:
        for square in range (9):
            if square_values[square] == 0:
                return(None)
                break
        else:
            return(0)
    elif winner == player:
        return(10)
    else:
        return(-10)

def get_moves(game):
    moves = []
    for square in range(1,10):
        if str(square) not in game:
            moves.append(square)
    return(moves)

def computer_play(game, level, rev):
    if level == "Easy":
        #Chooses move randomly
        moves = get_moves(game)
        return(moves[random.randrange(0, len(moves))])
    
    elif level == "Medium":
        comp_move = (len(game) % 2) + 1
        moves = get_moves(game)
        best_move = 0
        
        if rev == 1:
            #Checks all possible moves if it will win by playing that move
            for move in moves:
                if check_win(game + str(move), comp_move) == 10:
                    best_move = move
                    break
            else:
                #Checks all possible moves if opponent can win by playing there and blocks it if they can
                for move in moves:
                    #0 is added as a fake move so that the move being checked is given the symbol of the opponent
                    if check_win(game + '0' + str(move), comp_move) == -10:
                        best_move = move
                        break

            if best_move != 0:
                return(best_move)
            else:
                #Chooses move randomly if game cannot be won within next round
                return(moves[random.randrange(0, len(moves))])
        else:
            move_list = list(moves)
            
            #Checks if it will lose by playing the move for all moves and removes it from the list
            for move in moves:
                if check_win(game + str(move), comp_move) == -10:
                    move_list.remove(move)

            ok_moves = list(move_list)

            #Checks if it can win if opponent plays the move for all moves and leaves those squares free
            for move in moves:
                #0 is added as a fake move so that the move being checked is given the symbol of the opponent
                if check_win(game + '0' + str(move), comp_move) == 10:
                    if move in move_list:
                        move_list.remove(move)

            if move_list != []:
                return(move_list[random.randrange(0, len(move_list))])
            elif ok_moves != []:
                return(ok_moves[random.randrange(0, len(ok_moves))])
            else:
                return(moves[random.randrange(0, len(moves))])

init_game_win()
