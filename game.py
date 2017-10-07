print "Welcome to Battleship"

board = {
      # 0 1 2 3 4 5 6 7
  'A': [0,0,0,1,0,0,0,0],
  'B': [0,0,0,1,0,0,0,0],
  'C': [0,0,0,1,0,0,0,0],
  'D': [0,0,0,1,0,0,0,0],
  'E': [0,0,0,0,0,0,1,0],
  'F': [1,1,1,1,1,0,1,0],
  'G': [0,0,0,0,0,0,0,0],
  'H': [0,0,0,1,1,1,0,0]
}

print "Here is the board:"
print "  0 1 2 3 4 5 6 7"
for row_name, cells in board.items():
  print row_name,
  for cell in cells:
    if cell == 0:
      print "~",
    else:
      print "X",
  print ""

print "What row would you like to guess?"
row = raw_input()
print "What column would you like to guess?"
column = input()

cell = board[row][column]

if cell == 1:
  print "It's a HIT!"
else:
  print "It's a miss. Too bad."

