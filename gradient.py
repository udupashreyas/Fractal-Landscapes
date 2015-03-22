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
                h = (array[y][x] - 150)/105.0
                r = int(h * (100 - 86) + 86)
                g = int(h * (200 - 150) + 150)
                b = int(h * (50 - 17) + 17)
                if r < 255 and g < 255 and b < 255: 
                    color = [r,g,b]
                else:
                    color = [255,255,255]
            elif array[y][x] <= 150 and array[y][x] > 80:
                h = (array[y][x] - 80)/70.0
                r = int(h * 86)
                g = int(h * (150 - 100) + 100)
                b = int(h * 17)
                if r < 255 and g < 255 and b < 255: 
                    color = [r,g,b]
                else:
                    color = [86,150,17]
            elif array[y][x] <= 80 and array[y][x] > 50:
                h = (array[y][x] - 50)/30.0
                r = int((1.0 - h) * 96)
                g = int(h * (100 - 51) + 51)
                b = int((1.0 - h) * 17 + 17)
                if r < 255 and g < 255 and b < 255: 
                    color = [r,g,b]
                else:
                    color = [0,100,0]
            elif array[y][x] <= 50 and array[y][x] > 25:
                h = (array[y][x] - 25)/25.0
                r = int(h * 96)
                g = int((1.0 - h) * (128 - 51) + 51)
                b = int((1.0 - h) * (255 - 17) + 17)
                if r < 255 and g < 255 and b < 255: 
                    color = [r,g,b]
                else:
                    color = [96,51,17]
            elif array[y][x] <= 25 and array[y][x] > 5:
                h = (array[y][x] - 5)/20.0
                r = 0
                g = int(h * 128)
                b = 255
                if r < 255 and g < 255 and b < 255: 
                    color = [r,g,b]
                else:
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
