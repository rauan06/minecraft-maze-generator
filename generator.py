from collections import deque
from random import randint
import time

# a x a board
global a
a = 100

def main():
    maze = [['0' for _ in range(a + 2)] for _ in range(a + 2)]

    for i in range(a + 2):
        maze[0][i] = '1'
        maze[i][0] = '1'
        maze[i][a + 1] = '1'
        maze[a + 1][i] = '1'
    
    # Generation of start and finsih coordinates
    # start_x, start_y = random_coordinate(), random_coordinate()
    # finish_x, finish_y = random_coordinate(), random_coordinate()
    # maze[start_x][start_y] = 'S'
    # maze[finish_x][finish_y] = 'F'
    

    q = deque()
    q.append((1, 1, [(1, 1)], 0))
    searched = []

    while q:
        x, y, moves, length = q.popleft()
        if (x, y) == (a, a + 1):
            print(length)
            print(moves)

            for dx, dy in moves:
                maze[dx][dy] = 'W'
            break


        if (x, y) not in searched:  
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 1 <= x + dx <= a and 1 <= y + dy <= a + 1:
                    q.append((x + dx, y + dy, moves + [(x, y)], length + 1))
                    searched.append((x, y))

    with open("maze.txt", "w") as out:
        for row in maze:
            for wall in row:
                out.write(wall)
            out.write("\n")


def random_coordinate() -> int:
    return randint(1, a - 2)

if __name__ == '__main__':
    main()