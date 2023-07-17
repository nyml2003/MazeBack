"""
This module is used to put the start and end point of the maze.
"""
from random import randint
from mazeCreator import mazeCreator, print_maze


def putter(maze, col, row):
    nothing = 0
    pos_list = []
    for i in range(1, row):
        for j in range(1, col):
            if maze[i][j] == nothing:
                degree = 0
                if maze[i - 1][j] == nothing:
                    degree += 1
                if maze[i][j - 1] == nothing:
                    degree += 1
                if maze[i + 1][j] == nothing:
                    degree += 1
                if maze[i][j + 1] == nothing:
                    degree += 1
                if degree == 1:
                    pos_list.append([i, j])
    start_pos = pos_list.pop(randint(0, len(pos_list) - 1))
    end_pos = pos_list.pop(randint(0, len(pos_list) - 1))
    maze[end_pos[0]][end_pos[1]] = 2
    for pos in pos_list:
        maze[pos[0]][pos[1]] = 3
    return maze, start_pos, end_pos


def maze_after_putter(row, col):
    print_maze(putter(mazeCreator(row - 2, col - 2), col, row))

# maze_after_putter(5, 13)
