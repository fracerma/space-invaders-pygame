import pygame
import os
class Laser:
    img=pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
        pass

    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    
    def move(self):
        self.y+=self.speed
    
