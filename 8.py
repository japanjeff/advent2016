columns = 50
rows = 6
display = [[None for x in range(columns)] for y in range(rows)]

def dump(display):
    for row in display:
        print(''.join('#' if cell else '.' for cell in row))
    print()

def rotate_column_down(display, column):
    temp = display[5][column]
    for row in range(5, 0, -1):
        display[row][column] = display[row-1][column]
    display[0][column] = temp

def rotate_column_up(display, column):
    temp = display[0][column]
    for row in range(0, 5):
        display[row][column] = display[row+1][column]
    display[5][column] = temp

def rotate_row(display, row, n):
    l = display[row]
    display[row] = l[-n:] + l[:-n]

display[0][0] = 1
display[1][1] = 1
display[2][2] = 1

dump(display)
rotate_row(display, 0, 3)
dump(display)
rotate_row(display, 0, -3)
dump(display)
rotate_column_up(display, 0)
dump(display)
rotate_column_up(display, 0)
dump(display)
rotate_column_down(display, 0)
dump(display)
rotate_column_down(display, 0)
dump(display)
