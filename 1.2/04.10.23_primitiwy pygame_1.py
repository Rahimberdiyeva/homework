import pygame
pygame.init()
screen = pygame.display.set_mode((300,300))
screen.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                print('нажата на Enter')
            if keys[pygame.K_SPACE]:
                print('нажата на Space')
            if keys[pygame.K_ESCAPE]: 
                print('нажата на ESC')
            
            if keys[pygame.K_UP]: 
                print('нажата на UP')
            if keys[pygame.K_DOWN]: 
                print('нажата на DOWN')
            if keys[pygame.K_LEFT]: 
                print('нажата на LEFT')
            if keys[pygame.K_RIGHT]: 
                print('нажата на RIGHT')
           
            if keys[pygame.K_w]:
                print('нажата на W')
            if keys[pygame.K_a]: 
                print('нажата на A')
            if keys[pygame.K_s]: 
                print('нажата на S')
            if keys[pygame.K_d]: 
                print('нажата на D')
            if event.type == pygame.QUIT:
               pygame.quit()
               exit()
               
    pygame.display.update() 