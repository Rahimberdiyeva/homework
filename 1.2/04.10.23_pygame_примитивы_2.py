import pygame
sc = pygame.display.set_mode((300,300))

BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
color=[BLACK, GRAY, LIGHT_BLUE,  GREEN, YELLOW, PINK]
x0=50
y0=50
x1 = 50
y1 = 50
x = 0
y = 0
r = pygame.Rect(x1,y1,10,10)
pygame.display.set_caption("My game")
pygame.draw.rect(sc, color[0], r,0)
t=0

#fat = 10 
#FPS = 10
#pos = (x, y, fat, fat)
#color = (0,255, 0)
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x1-10>=0 :
                x-=10
   
        if keys[pygame.K_RIGHT]:
            if x1+10<=290:
                x+=10
       
            #pos = (x, y, fat*2, fat) 
        if keys[pygame.K_UP]:
            if y1-10>=0:
                y-=10
     
           # pos = (x, y, fat*2, fat) 
        if keys[pygame.K_DOWN]:
            if y1+10<=290:
                y+=10
        
            #pos = (x, y, fat*2, fat) 
     
        x1 += x
        y1 += y
        sc.fill((255,255,255))
        r = pygame.Rect(x0,y0, x1,y1)
        pygame.draw.rect(sc, color[t], r,0)
        x=y=0
   
    pygame.display.update()
    if t<5:
        t+=1
    else:
        t=0   

    
quit