columns = 50
rows = 6
display = [[0 for x in range(columns)] for y in range(rows)]

def dump(display):
    for row in display:
        print(''.join('#' if cell else ' ' for cell in row))
    print()

def activate(display, x, y):
    for i in range(y):
        for j in range(x):
            display[i][j] = 1

def rotate_column_down(display, column):
    temp = display[rows-1][column]
    for row in range(rows-1, 0, -1):
        display[row][column] = display[row-1][column]
    display[0][column] = temp

def rotate_column_up(display, column):
    temp = display[0][column]
    for row in range(0, rows-1):
        display[row][column] = display[row+1][column]
    display[rows-1][column] = temp

def rotate_row(display, row, n):
    l = display[row]
    display[row] = l[-n:] + l[:-n]

# Test data
# lines = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1""".split('\n')

with open('input-8.txt') as f:
    lines = f.readlines()

for line in lines:
    task, _, parms = line.partition(' ')
    if 'rect' in task:
        x, y = parms.split('x')
        activate(display, int(x), int(y))
    elif 'rotate' in task:
        target, num = parms.split('=')[-1].split(' by ')
        if 'column' in parms:
            for _ in range(int(num)):
                rotate_column_down(display, int(target))
        elif 'row' in parms:
            rotate_row(display, int(target), int(num))
        else:
            assert False, 'Unknown rotate target'
    else:
        assert False, 'Unknown task'

dump(display)

pixels_on = sum(map(sum, display))
print(pixels_on)
