import pygame
import math
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
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
openSet=[]
closedSet=[]
cameFrom=[]

for row in range (50):
    grid.append([])
    for column in range (50):
        grid[row].append(0)
for row in range(50):
    for column in range(50):
        grid[row][column]=0
        
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
             if(a>0):
                 grid[row][column]=1
                 a=a-1
             else:
                 grid[row][column]=-1
             if(a==1):
                 r1=row
                 c1=column
                 start=grid[r1][c1]
                 start=1
             if(a==0):
                 r2=row
                 c2=column
                 end=grid[r2][c2]
                 end=1
        
             print ("Click",pos,"Grid Coordinates: ",row ,column,"r1,c1=",r1 ,c1,"r2,c2=", r2 ,c2)
     sc.fill(BLACK)
     for row in range(50):
        for column in range(50):
            color=RED
            if grid[row][column]==1:
                color=GREEN
            elif grid[row][column]==-1:
                color=WHITE
            pygame.draw.rect(sc,color,[(M+W)*column+M,(M+H)*row+M,W,H])
            
            
     def distance(r1,r2,c1,c2):
         d= math.sqrt((r2-r1)**2 + (c2-c1)**2)
         print("Distance is:"+ str(d))
     
     clock.tick(60)
     pygame.display.flip()
pygame.quit()
        
