#A kinda crappy recursive Sierpinski program
#Written by j.moriarty, Fall 2021

import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("Sierpinski gasket!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background blue

#midpoint function definition--------------------------
def midpoint(p1, p2):
    return ((p1+p2)/2) 

#sierpinski function definition(recursive version)-----
def sierpinski(x1, y1, x2, y2, x3, y3, counter, isEven):
    #finds midpoint of each side, draw a trignale there
    counter+=50
    if counter>300:
        return 0
    if counter<255 and isEven == 1:
        pygame.draw.polygon(screen, (50, counter/2, 255), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
    elif counter < 255 and isEven == -1:
        pygame.draw.polygon(screen, (0,0,0), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
        print("black")
    else:
        pygame.draw.polygon(screen, (150, 0, 250), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  )) 
    pygame.display.flip()
    isEven *=-1
    #RECURSIVE CALL (function is calling itself) create 3 new triangles (top, left, right)
    #top
    sierpinski(x1, y1, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )
    #left
    sierpinski(x2, y2, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x2) ,midpoint(y3, y2), counter, isEven  )
    #right
    sierpinski(x3, y3, midpoint(x2, x3), midpoint(y2, y3),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )
    
#"main" function---------------------------------------------------------------------------------------------
  
#coordinate points for base triangle
#top point (use midpoint and trig to find if missing!)
x1 = 400
y1 = 81
#bottom left point
x2 = 100
y2 = 600
#bottom right point
x3 = 700
y3 = 600    
pygame.draw.polygon(screen, (0,0, 250), ((x1, y1), (x2, y2), (x3, y3)))
sierpinski(x1, y1, x2, y2, x3, y3, 0,1)#function call

print("all done!")

#this part is just here so the pygame window doesn't close until we want it to
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()

