import sys

gridSize = 100
numSteps = 100
grid = [x[:] for x in [[False]*gridSize]*gridSize]

# Parse initial state of the grid.
with open('day18.txt') as inFile:
    rowNum = 0
    for line in inFile:
        colNum = 0
        for char in line:
            if colNum < gridSize:
                grid[rowNum][colNum] = True if char == '#' else False
            colNum += 1

        rowNum += 1

# Count total number of lights that are on
def countOn(grid):
    numOn = 0
    for row in grid:
        for light in row:
            numOn += 1 if light == True else 0
    return numOn

#Count number of neighbors that are lit.
def countNeighbors(grid,row,col):
    numNeighbors = 0

    for x in range(-1,2):
        for y in range(-1,2):
            if row+x >= 0 and row+x < gridSize and col+y >= 0 and col+y < gridSize:
                if grid[row+x][col+y] == True and (x != 0 or y != 0):
                    numNeighbors += 1

    return numNeighbors

#Take a step in Conway's Game of Life
def step(grid):
    newGrid = [x[:] for x in [[False]*gridSize]*gridSize]
    for row in range(gridSize):
        for col in range(gridSize):
            numNeighbors = countNeighbors(grid,row,col)
            if grid[row][col] == True:
                newGrid[row][col] = True if numNeighbors == 2 or numNeighbors == 3 else False
            else:
                newGrid[row][col] = True if numNeighbors == 3 else False

            # And if it's in a corner, just turn it on.
            newGrid[0][0] = True
            newGrid[0][gridSize-1] = True
            newGrid[gridSize-1][0] = True
            newGrid[gridSize-1][gridSize-1] = True

    return newGrid

#Prints the grid.
def printGrid(grid):
    for row in grid:
        for char in row:
            if char == True:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        print ''

# Turn corners on after we parse.
grid[0][0] = True
grid[0][gridSize-1] = True
grid[gridSize-1][0] = True
grid[gridSize-1][gridSize-1] = True

# Go through all steps.
for i in range(numSteps):
    grid = step(grid)

# printGrid(grid)
print countOn(grid)
