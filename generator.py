import matplotlib.pyplot as plt
import numpy as np
import random
from queue import Queue
from random import randint
import time

# a x a board
global a
a = 100

def main():
    start = time.time()
    maze = create_maze(10)
    print(maze)
    finish = time.time()
    print("Time for maze creation:", finish - start, "seconds")


    start = time.time()
    with open("maze.csv", "w") as out:
        for row in maze:
            for i in range(len(row) - 1):
                out.write(str(row[i])[0] + ", ")
            out.write(str(row[-1])[0] + "\n")
    finish = time.time()
    print("Time for writing:", finish - start, "seconds")


def create_maze(dim):
    # Create a grid filled with walls
    maze = np.ones((dim*2+1, dim*2+1))

    # Define the starting point
    x, y = (0, 0)
    maze[2*x+1, 2*y+1] = 0

    # Initialize the stack with the starting point
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        # Define possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1, 2*ny+1] == 1:
                maze[2*nx+1, 2*ny+1] = 0
                maze[2*x+1+dx, 2*y+1+dy] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()
            
    # Create an entrance and an exit
    maze[1, 0] = 0
    maze[-2, -1] = 0

    return maze


if __name__ == '__main__':
    main()