import pygame
import os
from Laser import Laser

class Enemy:
    def __init__(self,x,y,WIN_WIDTH,WIN_HEIGHT):
        self.WIN_WIDTH=WIN_WIDTH
        self.WIN_HEIGHT=WIN_HEIGHT
        self.enemyX=x
        self.enemyY=y
        self.move_vel=0
        self.alive=True
        self.currImg = 0
    
    def move(self,dir,long):
        if(dir=="left"):
            self.enemyX-=long
        elif(dir=="down"):
            self.enemyY+=long
        elif(dir=="right"):
            self.enemyX+=long
        if(self.currImg==0):
            self.currImg=1
        else:
            self.currImg=0
    def draw(self,screen):
        screen.blit(self.enemyImg[self.currImg],(self.enemyX,self.enemyY))

    def shoot(self,speed):
        laser = Laser( (self.enemyImg[self.currImg].get_height())/2+self.enemyX+Laser.img.get_width()/2,self.enemyImg[self.currImg].get_height()+self.enemyY-5,speed)
        return laser
    
    def getDistanceBorder(self):
        left=self.enemyX
        right=self.WIN_WIDTH-(self.enemyX+self.enemyImg[0].get_width())
        down=self.WIN_HEIGHT-(self.enemyY+self.enemyImg[0].get_height())
        return (left,right,down)
    def get_mask(self):
        return pygame.mask.from_surface(self.enemyImg[self.currImg])

    def collide(self,obj):
        pos=obj.get_position()
        maskObj= obj.get_mask()
        offset=(round(pos[0])- round(self.enemyX),round(pos[1]) - round(self.enemyY))
        point= self.get_mask().overlap(maskObj,offset)
        if point:
            return True


class Octopus(Enemy):
    hit_need = 1
    MOVE_VEL= 1
    enemyImg = [pygame.image.load(os.path.join("assets","OctopusOpen.png")),pygame.image.load(os.path.join("assets","OctopusClose.png"))]
    def __init__(self,x,y,WIN_WIDTH,WIN_HEIGHT):
        super(Octopus,self).__init__(x,y,WIN_WIDTH,WIN_HEIGHT)