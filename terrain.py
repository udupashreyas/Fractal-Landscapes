import random, pygame, sys
from math import *

xmax = int(raw_input("enter the width in blocks: "))
xmin = 0
ymax = int(raw_input("enter the hieght in blocks: "))
ymin = 0
passes = int(raw_input("enter number of passes: "))
displacer = int(raw_input("enter the hieght variation of the terrain: "))
smoothness = int(raw_input("enter the smoothness of the terrain: "))
resolution = int(raw_input("enter the number of pixels per block: "))
update = int(raw_input("enter number of passes before the screen updates: "))
name = raw_input("enter the name of the saved file (do not include extention): ")
sea_level = 0

bliter = pygame.surface.Surface((resolution,resolution))

array = []
for y in range(ymin,ymax):
    row = []
    for x in range(xmin,xmax):
        row.append(0)
    array.append(row)

def fault():
    global array
    v = random.randint(xmin,xmax)
    a = sin(v)
    b = cos(v)
    d = sqrt(xmax ** 2 + ymax ** 2)
    c = random.random() * d - d/2
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            array[x][y] +=  displacer * atan(a*x + b*y - c)/smoothness

def draw():
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            if array[y][x] > 150:
                color = [255,255,255]
            elif array[y][x] <= 150 and array[y][x] > 80:
                color = [86,150,17]
            elif array[y][x] <= 80 and array[y][x] > 50:
                color = [0,100,0]
            elif array[y][x] <= 50 and array[y][x] > 25:
                color = [96,51,17]
            elif array[y][x] <= 25 and array[y][x] > 10:
                color = [0,128,255]
            else:
                color = [0,0,200]
            bliter.fill(color)
            screen.blit(bliter,(x*resolution,y*resolution))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode([len(array[0]) * resolution, len(array) * resolution])
    global screen
    for looper in range(0, passes):
        fault()
        if int(looper/update) == float(looper)/update:
            draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                except:
                    pass
    pygame.image.save(screen, name + ".jpg")
    pygame.quit()
    try:
        sys.exit()
    except:
        print "done"

main()
