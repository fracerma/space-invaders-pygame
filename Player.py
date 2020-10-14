import pygame
import os

class Player:
    MOVE_VEL=5
    playerImg= pygame.transform.scale(pygame.image.load(os.path.join("assets","Laser_Cannon.png")),(60,45))

    def __init__(self,x,y):
        self.playerX= x - self.playerImg.get_width()/2
        self.playerY= y - self.playerImg.get_height()/2
        self.velX=0
        self.velY=0
        self.arrY=[]
        self.arrX=[]

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.arrY.insert(0,"up")
            if event.key == pygame.K_DOWN:
                self.arrY.insert(0,"down")
            if event.key == pygame.K_LEFT:
                self.arrX.insert(0,"left")
            if event.key == pygame.K_RIGHT:
                self.arrX.insert(0,"right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.arrY.remove("up")
            if event.key == pygame.K_DOWN:
                self.arrY.remove("down")
            if event.key == pygame.K_LEFT:
                 self.arrX.remove("left")
            if event.key == pygame.K_RIGHT:
                 self.arrX.remove("right")
    def draw(self,screen,WIN_WIDTH,WIN_HEIGHT):
        if(len(self.arrY)==0):
            self.velY=0
        elif(self.arrY[0]=="up"):
            self.velY=-self.MOVE_VEL
        elif(self.arrY[0]=="down"):
            self.velY=+self.MOVE_VEL
        if(len(self.arrX)==0):
            self.velX=0
        elif(self.arrX[0]=="left"):
            self.velX=-self.MOVE_VEL
        elif(self.arrX[0]=="right"):
            self.velX=+self.MOVE_VEL
        if(self.playerX+self.velX<0):
            self.playerX=0
        elif(self.playerX+self.velX>WIN_WIDTH-self.playerImg.get_width()):
            self.playerX=WIN_WIDTH-self.playerImg.get_width()
        else:
            self.playerX=self.playerX+self.velX
        if(self.playerY+self.velY<0):
            self.playerY=0
        elif(self.playerY+self.velY>WIN_HEIGHT-self.playerImg.get_height()):
            self.playerY=WIN_HEIGHT-self.playerImg.get_height()
        else:
            self.playerY=self.playerY+self.velY
        
        screen.blit(self.playerImg,(self.playerX,self.playerY))
        