import pygame
BLACK = (0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
RED = (255,0,0)
W=10
H=10
M=2
grid=[]
for row in range (50):
    grid.append([])
    for column in range (50):
        grid[row].append(0)

pygame.init()
WINSIZE=[600,600]
sc=pygame.display.set_mode(WINSIZE)
pygame.display.set_caption("PATH FINDER")
done=False
clock=pygame.time.Clock()
while not done:
     for  event in pygame.event.get():
         if event.type == pygame.QUIT:
             done=True
         elif event.type==pygame.MOUSEBUTTONDOWN:
             pos =pygame.mouse.get_pos()
             column=pos[0]//(W+M)
             row=pos[1]//(H+M)
             grid[row][column]=1
             print ("Click",pos,"Grid Coordinates: ",row ,column)
     sc.fill(BLACK)
     for row in range(50):
        for column in range(50):
            color=WHITE
            if grid[row][column]==1:
                color=GREEN
            pygame.draw.rect(sc,color,[(M+W)*column+M,(M+H)*row+M,W,H])
     clock.tick(60)
     pygame.display.flip()
pygame.quit()
        
