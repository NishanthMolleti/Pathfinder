import pygame
BLACK = (0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
RED = (255,0,0)
W=10
H=10
M=2
a=2
r1=0
c1=0
c2=0
r2=0
grid=[]
for row in range (50):
    grid.append([])
    for column in range (50):
        grid[row].append(0)

pygame.init()
WINSIZE=[602,602]
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
             a=a-1
             if(a==1):
                 r1=row
                 c1=column
             if(a==0):
                 r2=row
                 c2=column
             print ("Click",pos,"Grid Coordinates: ",row ,column,"r1,c1=",r1 ,c1,"r2,c2=", r2 ,c2)
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
        
