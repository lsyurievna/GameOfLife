"""Conway's Game of Life
The program takes initial state of a grid as input. In the grid, state 1 is equivalent to a living cell,
0 - to the dead cell. The state is updated according to the rules: if a cell has less than 2 or more 
than 3 neighbours, the the cell dies; if the cell has exactly three neighbours, it is born. Only a couple
of iterations of the game are being printed as output to the console, since I haven't figured out yet how
to make a proper simulation.

01.12.2020
Liudmila Strelnikova
"""

#Different simple initial states for the game.
#
Blinker = [[0,1,0],
          [0,1,0],
          [0,1,0]]
Toad = [[0,0,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,0,0]]
Glider = [[0,0,1,0,0,0],
          [1,0,1,0,0,0],
          [0,1,1,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]

#The function takes a grid and caclulates neighbours for each state.
#Then it returns a two-D array with all the nighbours.
#@a array descibing the state
#@return nei 2-D array with all the neighbours
#
def nei(a):
  row = len(a)
  r=row
  col = len(a[0])
  c=col
  nei=[]
  for i in range (row):
    nei_row=[]
    for j in range(col):
      nei_row.append(neighbours(a,i,j,r,c))
    nei.append(nei_row)
  return nei

#The function looks at a specific cell and calculates neigbours for it. 
#@a array that describes a state
#@i row position of a cell
#@j column position of a cell
#@r number of rows in a
#@c number of columns in a
#@return total number of neighbours for a specific cell
#  
def neighbours(a,i,j,r,c):
  #top left angle
      if (i==0 and j==0):
        total = a[i][j+1] + a[i+1][j+1] + a[i+1][j]
        #print("Top left cell has", total, "neighbours.")

      #top right angle
      elif (i==0 and j==c-1):
        total = a[i][j-1] + a[i+1][j-1] + a[i+1][j]
        #print("Top right cell has", total, "neighbours.")

      #bottom left angle
      elif (i==r-1 and j==0):
        total = a[i-1][j] + a[i-1][j+1] + a[i][j+1]
        #print("Bottom left cell has", total, "neighbours.")

      #bottom right angle
      elif (i==r-1 and j == c-1):
        total = a[i-1][j] + a[i-1][j-1] + a[i][j-1]
        #print("Bottom right cell has", total, "neighbours.")

      #top border
      elif (i==0 and j!=0 and j!=c-1): 
        total=0
        sub = a[i][j]
        for n in range (i,i+2,1):
          for m in range (j-1,j+2,1):
            total += a[n][m]
        total -= sub
        #print("Top middle cell has", total, "neighbours.")

      #bottom border
      elif (i==r-1 and j!=0 and j!=c-1): 
        total=0
        sub = a[i][j]
        for n in range (i-1,i+1,1):
          for m in range (j-1,j+2,1):
            total += a[n][m]
        total -= sub
        #print("Bottom middle cell has", total, "neighbours.")

      #left border
      elif (j==0 and i!=0 and i!=r-1): 
        total=0
        sub = a[i][j]
        for n in range (i-1,i+2,1):
          for m in range (j,j+2,1):
            total += a[n][m]
        total -= sub
        #print("Left middle cell has", total, "neighbours.")

      #right border
      elif (j==c-1 and i!=0 and i!=r-1): 
        total=0
        sub = a[i][j]
        for n in range (i-1,i+2,1):
          for m in range (j-1,j+1,1):
            total += a[n][m]
        total -= sub
        #print("Right middle cell has", total, "neighbours.")  
        #  
      else:
        total=0
        sub = a[i][j]
        for n in range (i-1,i+2,1):
          for m in range (j-1,j+2,1):
            total += a[n][m]
        total -= sub
        #print("Middle cell has", total, "neighbours.")

      return (total)

#The function takes arrray containing current state and array containing neighbours for each cell
#and returns a new state
#@a array describing the state
#@ nei array containing neighbours
#@return b array containing new state
#
def newState(a,nei):
  b = a.copy()
  row = len(nei)
  col = len(nei[0])
  for i in range(row):
    for j in range(col):
      #print(nei[i][j])

      if (nei[i][j] > 3 or nei[i][j] < 2):
        b[i][j] = 0
      elif (nei[i][j] == 3):
        b[i][j] = 1

  return b

#Prints the grid nicely.
#@input grid the built grid
#
def render(grid):
  for r in grid:
    for c in r:
      if c == 1:print ("●",end = " ")
      else: print (" ",end =" ")
    print()

#The function reads initial state of the grid, and updates it it times
#@init initial state of the grid
#@it number of iterations
#@return it number of states nicely rendered
#
def game(init,it):
  render(init)
  for i in range(it):
    init = (newState(init,nei(init)))
    render(init)

game(Glider,6)