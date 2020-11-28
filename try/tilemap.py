import pygame as pg
from os import path
from settings import *
import pytmx
from object import *
def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)
def collide_hit_rect_a(one, two):
    return two.hit_rect.colliderect(one.rect)
class Map:
    def __init__(self,filename):
        self.data=[]
        with open(filename,"r")as f:
            for line in f:
                self.data.append(line.strip())
        self.tilewidth=len(self.data[0])
        self.tileheight=len(self.data)
        self.width=self.tilewidth*TILESIZE
        self.height=self.tileheight *TILESIZE 
class Camera:
    def __init__(self,width,height):
        self.camera=pg.Rect(0,0,width,height)
        self.width=width
        self.height=height
    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self,rect):
        return rect.move(self.camera.topleft)
    def draw(self,game,target):
        self.game=game
        x=target.rect.x-int(WIDTH/2)
        y=target.rect.y-int(HEIGHT/2)
        #x=min(0,x)
        #y=min(0,y)
        #x=max(-(self.width-WIDTH),x)
        #y=max(-(self.height-HEIGHT),y)

        for ob in self.game.neobstacole:
            if ob.rect.centerx<x or ob.rect.centerx>x+self.width or ob.rect.centery<y or ob.rect.centerx>y+self.height:
                ob.kill()
                
        for ob in self.game.obstacole:
            if ob.rect.centerx<x or ob.rect.centerx>x+self.width or ob.rect.centery<y or ob.rect.centerx>y+self.height:
                ob.kill()
        for ob in self.game.apa:
            if ob.rect.centerx<x or ob.rect.centerx>x+self.width or ob.rect.centery<y or ob.rect.centerx>y+self.height:
                ob.kill()
        x=(int)(x/TILESIZE)
        y=(int)(y/TILESIZE)

        for i in range(x,x+(int)(NR_TILE/2)+1,1):
            for j in range(y,y+(int)(NR_TILE/2)+1,1):
                tile=self.game.map.data[i][j]
                if tile=="0":
                            if i==0:#suntem pe prima linie
                                if j==0:#suntem pe prima coloana
                                    #deci colt stanga sus
                                    if self.game.map.data[i+1][j]!='0' or self.game.map.data[i+1][j+1]!='0' or self.game.map.data[i][j+1]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.game.map.tileheight-1:
                                    if self.game.map.data[i][j-1]!='0' or self.game.map.data[i+1][j-1]!='0' or self.game.map.data[i+1][j]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.map.tileheight-1:
                                    if self.map.data[i][j-1]!='0' or self.game.map.data[i+1][j-1]!='0' or self.game.map.data[i+1][j]!='0' or self.game.map.data[i+1][j+1]!='0'or self.game.map.data[i][j+1]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                            elif i==self.game.map.tilewidth-1:
                                if j==0:#suntem pe prima coloana
                                    if self.game.map.data[i-1][j]!='0' or self.game.map.data[i-1][j+1]!='0' or self.game.map.data[i][j+1]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.game.map.tileheight-1:
                                    if self.game.map.data[i][j-1]!='0' or self.game.map.data[i-1][j-1]!='0' or self.game.map.data[i-1][j]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.game.map.tileheight-1:
                                    if self.game.map.data[i][j-1]!='0' or self.game.map.data[i-1][j-1]!='0' or self.game.map.data[i-1][j]!='0' or self.game.map.data[i-1][j+1]!='0'or self.game.map.data[i][j+1]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                            elif i>0 and i<self.game.map.tileheight-1:
                                if j==0:#suntem pe prima coloana
                                    if self.game.map.data[i-1][j]!='0' or self.game.map.data[i-1][j+1]!='0' or self.game.map.data[i][j+1]!='0'or self.game.map.data[i+1][j+1]!='0'or self.game.map.data[i+1][j]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.game.map.tileheight-1:
                                    if self.game.map.data[i-1][j]!='0' or self.game.map.data[i-1][j-1]!='0' or self.game.map.data[i][j-1]!='0'or self.game.map.data[i+1][j-1]!='0'or self.game.map.data[i+1][j]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.game.map.tileheight-1:
                                    if self.game.map.data[i-1][j-1]!='0' or self.game.map.data[i-1][j]!='0' or self.game.map.data[i-1][j+1]!='0' or self.game.map.data[i][j-1]!='0' or self.game.map.data[i][j+1]!='0' or self.game.map.data[i+1][j-1]!='0' or self.game.map.data[i+1][j+1]!='0' or self.game.map.data[i+1][j]!='0':
                                        Apa(self.game,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)   
                if tile=='1':
                    Nisip(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                if tile=='2':
                    Piatra(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                    Nisip(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                if tile=='3':
                    Nisip(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                if tile=='4':
                    Copaci(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                    Nisip(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                if tile=='5':
                    Mob(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                    Nisip(self.game,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                #if tile=='9':
                   # self.player=Player(self,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
                   # Nisip(self,j*TILESIZE+TILESIZE/2,i*TILESIZE+TILESIZE/2)
    def update(self,target):
        x=-target.rect.x+int(WIDTH/2)
        y=-target.rect.y+int(HEIGHT/2)
        x=min(0,x)
        y=min(0,y)
        x=max(-(self.width-WIDTH),x)
        y=max(-(self.height-HEIGHT),y)
        self.camera=pg.Rect(x,y,self.width,self.height)
class Scara(pg.sprite.Sprite):#ar merge o scara up si una down, pt a face cele 3 nivele
    def __init__(self,game,x,y):
        self.groups=game.scara_ob
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.scara.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center