import pygame
import os
from Laser import Laser

class Player:
    MOVE_VEL=5
    playerImg= pygame.transform.scale(pygame.image.load(os.path.join("assets","Laser_Cannon.png")),(60,45))

    def __init__(self,x,y):
        self.playerX= x - self.playerImg.get_width()/2
        self.playerY= y - self.playerImg.get_height()/2
        self.velX=0
        self.arrY=[]
        self.arrX=[]

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.arrX.insert(0,"left")
            if event.key == pygame.K_RIGHT:
                self.arrX.insert(0,"right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                 self.arrX.remove("left")
            if event.key == pygame.K_RIGHT:
                 self.arrX.remove("right") 

    def update(self,WIN_WIDTH):
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

    def draw(self,screen):
        screen.blit(self.playerImg,(self.playerX,self.playerY))
        
    def shoot(self,speed):
        laser = Laser((self.playerImg.get_height())/2+self.playerX+Laser.img.get_width()/2,self.playerY-Laser.img.get_height(),speed,color="red")
        return laser

    def get_mask(self):
        return pygame.mask.from_surface(self.playerImg)

    def collide(self,obj):
        pos=obj.get_position()
        maskObj= obj.get_mask()
        offset=(round(pos[0])- round(self.playerX),round(pos[1]) - round(self.playerY))
        point= self.get_mask().overlap(maskObj,offset)
        if point:
            return True

