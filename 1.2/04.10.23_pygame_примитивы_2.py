import pygame
import random
sc = pygame.display.set_mode((300,300))

BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
color=[BLACK, GRAY, LIGHT_BLUE,  GREEN, YELLOW, PINK]
color_1=0
x = 10
y = 10
pygame.display.set_caption("My game")
t=0
sc.fill((255,255,255))
#fat = 10 
#FPS = 10
#pos = (x, y, fat, fat)
#color = (0,255, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x-10>=0:
                x-=10
   
        if keys[pygame.K_RIGHT]:
            if x+10<=290:
                x+=10
       
        if keys[pygame.K_UP]:
           if y-10>=0:
                y-=10
     
        if keys[pygame.K_DOWN]:
           if y+10<=290:
                y+=10

        if keys[pygame.K_c]:
            color_1 = random.choice(color)  
            
    r = pygame.Rect(x,y, 10,10)
    pygame.draw.rect(sc, color_1, r,0)
    print(t)
   
    pygame.display.update()
   
