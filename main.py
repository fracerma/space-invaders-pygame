import pygame
import sys
import os
from random import randint
from Enemy import *
from Laser import Laser
from Player import Player

class SpaceInvaders:
    #Constant
    WIN_HEIGHT=672
    WIN_WIDTH=780
    def __init__(self):
        #Init pygame and screen
        pygame.init()
        pygame.font.init()
        self.screen= pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        #Title an Icon
        pygame.display.set_caption("Space Invaders")
        icon= pygame.image.load(os.path.join("assets","ufo.png"))
        bg=pygame.image.load(os.path.join("assets","ScreenshotStarfield.png"))
        self.bg=pygame.transform.scale(bg, (self.WIN_WIDTH, self.WIN_HEIGHT))
        pygame.display.set_icon(icon)
        #clock
        self.clock= pygame.time.Clock()
        #FPS
        self.FPS=60
        #Game props
        self.state="menu"
        self.level=1
        self.lives=3
        self.score=0
        self.tick=0
        #Font
        self.main_font=pygame.font.SysFont("comicsans",30)
        #Create Player
        self.player=Player(self.WIN_WIDTH/2,(self.WIN_HEIGHT-20))
        
        #CreateLevel
        self.buildLevel()
        

    def start(self):
        self.running=True
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                self.eventDispatcher(event)
            self.update()
            self.checkAndResolveCollision()
            self.buildLabel()
            self.draw()
            pygame.display.update()

    def eventDispatcher(self,event):
        if event.type == pygame.QUIT:
            self.running=False
        if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            self.player.move(event)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            print("shoot",self.playerLaser)
            if(self.playerLaser==None):
                self.playerLaser= self.player.shoot(-20)
        
    #update enviroment
    def update(self):
        self.update_player()
        if(self.tick%3==0):
            self.move_lasers()
        if(self.tick%30==0):
            MOVE_STEP=20
            self.move_aliens(MOVE_STEP)
            #Shoting random Enemies
            rand=randint(1,10)
            if(rand>8):
                rows=len(self.enemies)
                enemyInd=randint(0,len(self.enemies[rows-1])-1)
                self.enemiesLasers.append(self.enemies[rows-1][enemyInd].shoot(20))
        self.tick+=1

    def update_player(self):
        self.player.update(self.WIN_WIDTH)

    def move_lasers(self):
        for laser in self.enemiesLasers:
            res=laser.move(self.WIN_HEIGHT)
            if(not res):
                self.enemiesLasers.remove(laser)
        if(self.playerLaser):
            res=self.playerLaser.move(self.WIN_HEIGHT)
            if(not res):
                self.playerLaser=None

    def move_aliens(self,MOVE_STEP):
        wall_collisionL = self.leftest.getDistanceBorder()[0] - MOVE_STEP < 0
        wall_collisionR = self.rightest.getDistanceBorder()[1] - MOVE_STEP < 0
        if((self.direction=="left" and wall_collisionL) or (self.direction=="right" and wall_collisionR)):
            direction="down"
        else:
            direction=self.direction
        for row in self.enemies:
            for enemy in row:                
                enemy.move(direction,MOVE_STEP)
        if(direction=="down"):
            self.direction= "left" if self.direction=="right" else "right"

    def checkAndResolveCollision(self):
        for laser in self.enemiesLasers[:]:
            collision=self.player.collide(laser)
            if collision:
                self.enemiesLasers.remove(laser)
                self.lives-=1
        if(self.playerLaser!=None):
            for row in self.enemies[:]:
                for enemy in row[:]:
                    collision=enemy.collide(self.playerLaser)
                if collision:
                    row.remove(enemy)
                    self.playerLaser=None
                    if(len(row)==0):
                        self.enemies.remove(row)
                        if(len(self.enemies)==0):
                            self.running=False
                    self.score+=30
                    self.findExtreme()
                    break
            
    def printEnemy(self):
        print("Situa:")
        for row in self.enemies:
            for enemy in row:
                print("#",end=" ")
            print("\n")

    def buildLabel(self):
        self.lives_label= self.main_font.render(f"Lives: {self.lives}",1,(255,255,255))
        self.score_label= self.main_font.render(f"Score: {self.score}",1,(255,255,255))

    #TODO formula random per creare i livelli ed incrementare la difficoltà
    def buildLevel(self):
        self.direction="right"
        self.NUM_ROW=3
        self.NUM_COL=2
        self.enemies=[]
        self.enemiesLasers=[]
        self.playerLaser=None
        enemyWidth=Octopus.enemyImg[0].get_width()
        space=((self.WIN_WIDTH*0.8)-(enemyWidth*8))/9
        offset=(self.WIN_WIDTH*0.1)
        for i in range(self.NUM_ROW):
            row=[]
            for j in range(self.NUM_COL):
                row.append(Octopus(offset+space+((enemyWidth+space)*j),space+((enemyWidth+space)*i),self.WIN_WIDTH,self.WIN_HEIGHT))
            self.enemies.append(row)
        self.findExtreme()

        
    
    def findExtreme(self):
        #Init distance from left right down
        minLeft=self.WIN_WIDTH
        minRight=self.WIN_WIDTH
        #setting the downest enemy
        #find the leftest enemy
        for i in range(len(self.enemies)):
            distance=self.enemies[i][0].getDistanceBorder()[0]
            if(distance<minLeft):
                minLeft=distance
                self.leftest=self.enemies[i][0]
        #find the rightest enemy
        for i in range(len(self.enemies)):
            leng=len(self.enemies[i])-1
            distance=self.enemies[i][leng].getDistanceBorder()[1]
            if(distance<minRight):
                minRight=distance
                self.rightest=self.enemies[i][leng]
        

    def draw(self):
        #Draw background
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.score_label,(0,0))
        self.screen.blit(self.lives_label,(self.WIN_WIDTH-self.score_label.get_width(),0))
        self.player.draw(self.screen)
        for laser in self.enemiesLasers:
            laser.draw(self.screen)
        if(self.playerLaser):
            self.playerLaser.draw(self.screen)
        for row in self.enemies:
            for enemy in row:
                enemy.draw(self.screen)
        

if __name__ == "__main__":
    game = SpaceInvaders()
    game.start()