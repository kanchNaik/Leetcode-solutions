"""
There is a Rabbit at top left corner of the maze.
The Rabbit can only move right and down.
The Rabbit has to reach the bottom right corner of the maze.
The Rabbit can only move either right or down at a time.
find number of ways the Rabbit can reach the bottom right corner of the maze.

example:
Input: m = 3, n = 3
Output: 6
"""

def maze(m,n):
    matrix = [[float('inf') for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        matrix[i][0] = 1

    for j in range(n):
        matrix[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[m-1][n-1]


print(maze(4,3))
