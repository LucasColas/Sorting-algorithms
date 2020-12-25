import pygame

def greatest_value(Board):
    best =  Board[0]

    for indx, value in enumerate(Board):
        if value > best:
            best = value

    return best

def plot(Board, Window, Width):
    best = greatest_value(Board)
    Black = (0,0,0)


    for i in range(Board):
        pygame.draw.line(Window,Black, ((i*(1/len(Board)))*Width,0), (i*(1/len(Board)), (Board[i]//best))*Width)
