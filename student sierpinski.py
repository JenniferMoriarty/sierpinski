#A kinda crappy recursive Sierpinski program
#Written by j.moriarty, Fall 2021
#a few lines have been removed for class purposes...

import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("sierpinski")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 250))#paint background blue

#midpoint function definition----------------------------------------------------
#def midpoint(p1, p2):
    #LINE REMOVED BY MO

#sierpinski function definition(recursive version)-------------------------------
def sierpinski(x1, y1, x2, y2, x3, y3, counter, isEven):
    #this counter is set up so the recursion doesn't run forever
    counter+=50
    if counter>300:
        return 0
    
    #find midpoint of each side, draw a trignale there
    
    #draw pink triangles
    if counter<255 and isEven == 1:
        pygame.draw.polygon(screen, (255, counter, 255), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
    #draw black triangles   
    elif counter < 255 and isEven == -1:
        pygame.draw.polygon(screen, (0,0,0), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
    #white triangles
    else:
        pygame.draw.polygon(screen, (255, 255, 255), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  )) 
    
    pygame.display.flip()
    isEven *=-1 #helps swap colors with every other call of function
    
    #RECURSIVE CALL (function is calling itself) create 3 new triangles (top, left, right)
    #top
    sierpinski(x1, y1, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )
    #left
    sierpinski(x2, y2, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x2) ,midpoint(y3, y2), counter, isEven  )
    #right
    #LINE REMOVED BY MO
#end sierpinski function definition----------------------------------------------------------------------------


#"main" function---------------------------------------------------------------------------------------------
  
#coordinate points for base triangle
#top middle    
#REMOVED BY MO
#bottom left
x2 = 100
y2 = 600
#bottom right
x3 = 700
y3 = 600    
pygame.draw.polygon(screen, (200, 0, 200), ((x1, y1), (x2, y2), (y3, y3))) #base triangle
sierpinski(x1, y1, x2, y2, x3, y3, 0,1)#function call

print("all done!")

#this part is just here so the pygame window doesn't close until we want it to
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()


