print "Welcome to Battleship"

board = {
    #     0  1  2  3  4  5  6  7  8  9
    'A': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'B': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'C': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'D': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'E': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    'F': [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'H': [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'J': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

guesses = {
    "A": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "B": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "C": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "D": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "E": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "F": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "G": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "H": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "I": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    "J": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
}

print "Here is the board:"
print "  0 1 2 3 4 5 6 7 8 9"
for row_name in sorted(board.keys()):
    cells = board[row_name]
    print row_name,
    for cell in cells:
        if cell == 0:
            print "~",
        else:
            print "X",
    print ""

still_playing = True

while still_playing:
    print "What row/column would you like to guess?"
    row_column = raw_input().capitalize()

    if len(row_column) == 2:
        row = row_column[0]
        column = int(row_column[1])

        cell = board[row][column]

        if cell == 1:
            guesses[row][column] = "H"
            print "It's a HIT!"
        else:
            guesses[row][column] = "M"
            print "It's a miss. Too bad."

        print "  0 1 2 3 4 5 6 7 8 9"
        for row_name in sorted(guesses.keys()):
            cells = guesses[row_name]
            print row_name,
            for cell in cells:
                print cell,
            print ""
    else:
        print "Bye!"
        still_playing = False
