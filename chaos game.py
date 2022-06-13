import pygame
import random
pygame.init()
pygame.display.set_caption("Chaos")
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0, 0, 0))

xList = []
yList = []

num = 0
while num < 3 or num > 6: 
    num = int(input("Enter a number of points from 3 to 6: "))

def randomPoints(coord,pointNumber):
    if coord == 1: #x values
        if num == 3: #triangle
            if pointNumber == 0:
                return random.randint(50,950)
            elif pointNumber == 1:
                return (random.randint(50,450))
            elif pointNumber == 2:
                return random.randint(550,950)
        elif num == 4: # square
            if pointNumber == 0:
                return random.randint(50,450)
            elif pointNumber == 1:
                return random.randint(550,950)
            elif pointNumber == 2:
                return random.randint(50,450)
            elif pointNumber == 3:
                return random.randint(550,950)
        elif num == 5: #heptagon
            if pointNumber == 0:
                return random.randint(400,600)
            elif pointNumber == 1:
                return (random.randint(100,300))
            elif pointNumber == 2:
                return random.randint(250,450)
            elif pointNumber == 3:
                return random.randint(550,750)
            elif pointNumber == 4:
                return random.randint(700,900)
        elif num == 6: #hexagon
            if pointNumber == 0:
                return random.randint(400,600)
            elif pointNumber == 1:
                return (random.randint(100,300))
            elif pointNumber == 2:
                return random.randint(100,300)
            elif pointNumber == 3:
                return random.randint(400,600)
            elif pointNumber == 4:
                return random.randint(700,900)
            elif pointNumber == 5:
                return random.randint(700,900)
    elif coord == 2: #y values
        if num == 3: #triangle
            if pointNumber == 0:
               return random.randint(50,400)
            if pointNumber == 1:
               return random.randint(600,950)
            if pointNumber == 2:
               return random.randint(600,950)
        elif num == 4: # square
            if pointNumber == 0:
                return random.randint(50,450)
            elif pointNumber == 1:
                return (random.randint(50,450))
            elif pointNumber == 2:
                return random.randint(550,950)
            elif pointNumber == 3:
                return random.randint(550,950)
        elif num == 5: #heptagon
            if pointNumber == 0:
                return random.randint(100,300)
            elif pointNumber == 1:
                return (random.randint(400,600))
            elif pointNumber == 2:
                return random.randint(700,900)
            elif pointNumber == 3:
                return random.randint(700,900)
            elif pointNumber == 4:
                return random.randint(400,600)
        elif num == 6: #hexagon
            if pointNumber == 0:
                return random.randint(50,250)
            elif pointNumber == 1:
                return (random.randint(250,450))
            elif pointNumber == 2:
                return random.randint(550,750)
            elif pointNumber == 3:
                return random.randint(750,950)
            elif pointNumber == 4:
                return random.randint(550,750)
            elif pointNumber == 5:
                return random.randint(250,450)

for x in range(0,num):
    xList.append(randomPoints(1,x))
    yList.append(randomPoints(2,x))

dpx = random.randint(500,600)
dpy = random.randint(500,600)

def midpoint(dp, pp):
    if num == 3:
        return ((dp * 1/2) + (pp * 1/2))
    elif num == 4:
        return ((dp * 1/4) + (pp * 3/4))
    elif num == 5:
        return ((dp * 1/5) + (pp * 4/5))
    elif num == 6:
        return ((dp * 1/6) + (pp * 5/6))

def move(dpx,dpy,px,py):
    dpx = midpoint(dpx,px)
    dpy = midpoint(dpy,py)

    return (dpx, dpy)

doExit = False

for x in range(len(xList)):
    pygame.draw.circle(screen, (255,255,255), (xList[x],yList[x]), 3)

while doExit == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    
    dice = random.randint(1,num)
    if dice == 1:
        (dpx, dpy) = move(dpx,dpy,xList[0],yList[0])
    elif dice == 2:
        (dpx, dpy) = move(dpx,dpy,xList[1],yList[1])
    elif dice == 3:
        (dpx, dpy) = move(dpx,dpy,xList[2],yList[2])
    elif dice == 4:
        (dpx, dpy) = move(dpx,dpy,xList[3],yList[3])
    elif dice == 5:
        (dpx, dpy) = move(dpx,dpy,xList[4],yList[4])
    elif dice == 6:
        (dpx, dpy) = move(dpx,dpy,xList[5],yList[5])

    pygame.draw.circle(screen, (random.randint(50,250),random.randint(50,250),random.randint(50,250)), (dpx,dpy), 1)
    
    pygame.display.flip()

pygame.quit()
