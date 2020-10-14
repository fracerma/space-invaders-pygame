import pygame
import os
class Laser:
    img=pygame.transform.scale(pygame.image.load(os.path.join("assets","pixel_laser_green.png")),(8,24))
    def __init__(self,x,y,speed,color="green"):
        self.x=x
        self.y=y
        self.speed=speed
        #if(color=="red"):
        #    self.img=pygame.transform.scale(pygame.image.load(os.path.join("assets","pixel_laser_red.png")),(8,24))
            

    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    
    def move(self,WIN_HEIGHT):
        newY=self.y+self.speed
        if(newY>=0 and newY<=WIN_HEIGHT):
            self.y+=self.speed
            return True
        else:
            return False

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
    def get_position(self):
        return( self.x , self.y)
