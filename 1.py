input = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"
vX = 0
vY = 1
x = 0
y = 0

locations = [[0.0]]
twice = [0,0]

def handle_dir(dir, vX, vY):
    if (dir == 'R'):
        flip = vX == 1 or vX == -1
        vX,vY = vY,vX
        if flip:
            vY *= -1
    elif (dir == 'L'):
        flip = vY == 1 or vY == -1
        vX,vY = vY,vX
        if flip:
            vX *= -1
    else:
        print('fail')
    return vX, vY

for step in input.split(', '):
    dir = step[0]
    dist = int(step[1:])
    vX, vY = handle_dir(dir, vX, vY)
    x += (dist * vX)
    y += (dist * vY)
    if [x,y] in locations:
        print('Visiting twice!', x, y)
    locations.append([x,y])

print('HQ is %d blocks away at (%d, %d)' % (x+y, x, y))
print()
#[print(z) for z in locations]
