import pygame as pg
from solver import solve, boardValid, printBoard, inputValid
from generate import generate
import time

WIDTH, HEIGHT = 750, 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (52, 178, 52)

FPS = 60
pg.init()
font = pg.font.SysFont(None, 80)

unsolved = generate(0)

copy = [row[:] for row in unsolved]
copy2 = [row[:] for row in unsolved]

start = time.time()
solved = solve(copy, 0, 0, True)
end = time.time()
solve_time = end - start
delay = 0.01
time_visual = 0
if not solved:
    pg.quit()

def solve_text(board, row, column, start):
    time.sleep(delay)
    draw_window()
    draw_numbers(board)
    pg.display.update()
    if start and not boardValid(board):
        return False
    if row == 8 and column == 9:
        return board
    elif column == 9:
        return solve_text(board, row + 1, 0, False)
    if board[row][column] != 0:
        return solve_text(board, row, column + 1, False)
    test = 1
    while test <= 9:
        if inputValid(row,column, test, board):
            board[row][column] = test
            potential = solve_text(board, row, column + 1, False)
            if potential:
                return potential
            board[row][column] = 0
        test += 1
    return False

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sudoku!")

def draw_window():
    WIN.fill(WHITE)
    pg.draw.rect(WIN, BLACK, pg.Rect(15, 15, WIDTH - 30, HEIGHT - 30), 9)
    n = 1
    box_width = (WIDTH - 30)/9
    box_height = (HEIGHT - 30)/9
    while n * box_width < WIDTH - 30:
        if n % 3 != 0:
            line_width = 3
        else:
            line_width = 7
        pg.draw.line(WIN, BLACK, pg.Vector2(15 + n * box_width, 15), pg.Vector2(15 + n * box_width, HEIGHT - 20), line_width)
        pg.draw.line(WIN, BLACK, pg.Vector2(15, 15 + n * box_height), pg.Vector2(WIDTH - 20, 15 + n * box_height), line_width)
        n += 1

def draw_numbers(board):
    box_width = (WIDTH - 30)/9
    box_height = (HEIGHT - 30)/9
    row = 0
    xoffset = 28
    yoffset = 18
    global unsolved
    global solved
    while row < 9:
        col = 0
        while col < 9:
            output = board[row][col]
            if output == unsolved[row][col]:
                color = BLACK
            elif output == solved[row][col]:
                color = GREEN
            else:
                color = RED
            if output != 0:
                n_text = font.render(str(output), True, color)
                WIN.blit(n_text, pg.Vector2(col * box_width + 15 + xoffset, row * box_height + 15 + yoffset))
            col += 1
        row += 1

def main():
    clock = pg.time.Clock()
    run = True
    keyPressed = False
    while run:
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    keyPressed = True
                    start_visual = time.time()
                    solve_text(copy2, 0, 0, True)
                    end_visual = time.time()
                    global time_visual
                    time_visual = end_visual - start_visual
        if not keyPressed:
            draw_window()
            draw_numbers(unsolved)
        

        pg.display.update()
    
    pg.quit()

if __name__ == "__main__":
    main()