columns = 50
rows = 6
display = [[None for x in range(columns)] for y in range(rows)]

def dump(display):
    for row in display:
        print(''.join('#' if cell else '.' for cell in row))

display[0][0] = 1
display[1][1] = 1
display[2][2] = 1

dump(display)
