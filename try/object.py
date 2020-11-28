import pygame as pg 
from settings import *
from items import *
import random
def draw_health_obs(ob):
    if ob.health<0:
        ob.health=0
    fill=(ob.health*BAR_LENGHT_OBJ/ob.full_health)
    out_rect=pg.Rect(0,0,BAR_LENGHT_OBJ,BAR_WIDTH_OBJ)
    fill_rect=pg.Rect(0,0,fill,BAR_WIDTH_OBJ)

    if ob.health > 70/100*ob.full_health:
        col = GREEN
    elif ob.health > 30/100*ob.full_health:
        col = YELLOW
    elif ob.health>0:
        col = RED
    if ob.health<ob.full_health:
        pg.draw.rect(ob.image,DARKGREY,out_rect)
        pg.draw.rect(ob.image,col,fill_rect)    
def replace(string,index,carac):
    return string[:index] + carac + string[index+1:]
class Apa(pg.sprite.Sprite):
     def __init__(self,game,x,y,w,h):
        self.groups=game.apa,game.neobstacole
        pg.sprite.Sprite.__init__(self,self.groups)
        #x+=TILESIZE/2
        #y+=TILESIZE/2
        self.game=game
        self.rect=pg.Rect(x,y,w,h)
        self.rect.center=(x,y)
        self.x=x
        self.y=y
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
class Nisip(pg.sprite.Sprite):
     def __init__(self,game,x,y):
        self.groups=game.terra,game.neobstacole
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.nisip.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
class Iarba(pg.sprite.Sprite):
     def __init__(self,game,x,y,baza=False):
        self.groups=game.terra,game.neobstacole
        pg.sprite.Sprite.__init__(self,self.groups)
        self.baza=baza
        self.game=game
        self.image=self.game.iarba.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center       
class Copaci(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.obstacole,game.terra
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.copac.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=TREE_H
        self.full_health=TREE_H
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
        self.nume=COPAC
    def update(self):       
        if self.health<=0:
            self.game.map.data[int(self.rect.centery/TILESIZE)] = replace(self.game.map.data[int(self.rect.centery/TILESIZE)], int(self.rect.centerx/TILESIZE),'3')
            self.kill()

                        #deseneaza ce iese
            nr_item=random.choice(RANDOM_LIST)
            for i in range(nr_item):
                After_Copaci(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
            nr_item=random.choice(RANDOM_LIST_SMALL)
            for i in range(nr_item):
                After_Copaci2(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
class Piatra(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.obstacole,game.terra
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.piatra.copy()
        self.rect=self.image.get_rect()
        #self.rect.x-=20
        #self.rect.y-=20
        self.rect.center=(x,y)
        self.health=STONE_H
        self.full_health=STONE_H
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
        self.nume=PIATRA
    def update(self):       
        if self.health<=0:
            self.kill()
            self.game.map.data[int(self.rect.centery/TILESIZE)] = replace(self.game.map.data[int(self.rect.centery/TILESIZE)], int(self.rect.centerx/TILESIZE),'1')
             #creare items
            nr_item=random.choice(RANDOM_LIST)
            for i in range(nr_item):
                After_Piatra(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
class Fier(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.obstacole_pestera
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.fier.copy()
        self.rect=self.image.get_rect()
        #self.rect.x-=20
        #self.rect.y-=20
        self.rect.center=(x,y)
        self.health=FIER_H
        self.full_health=FIER_H
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
        self.nume=FIER
    def update(self):       
        if self.health<=0:
            self.kill()
            self.game.map_pestera.data[int(self.rect.centery/TILESIZE)] = replace(self.game.map_pestera.data[int(self.rect.centery/TILESIZE)], int(self.rect.centerx/TILESIZE),'1')
             #creare items
            nr_item=random.choice(RANDOM_LIST)
            for i in range(nr_item):
                After_Fier(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
class Diamant(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.obstacole_pestera
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.diamant.copy()
        self.rect=self.image.get_rect()
        #self.rect.x-=20
        #self.rect.y-=20
        self.rect.center=(x,y)
        self.health=DIAMANT_H
        self.full_health=DIAMANT_H
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
        self.nume=DIAMANT
    def update(self):       
        if self.health<=0:
            self.kill()
            self.game.map_pestera.data[int(self.rect.centery/TILESIZE)] = replace(self.game.map_pestera.data[int(self.rect.centery/TILESIZE)], int(self.rect.centerx/TILESIZE),'1')
             #creare items
            nr_item=random.choice(RANDOM_LIST)
            for i in range(nr_item):
                After_Diamant(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
class Piatra2(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.obstacole_pestera,game.terra
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=self.game.piatra.copy()
        self.rect=self.image.get_rect()
        #self.rect.x-=20
        #self.rect.y-=20
        self.rect.center=(x,y)
        self.health=STONE_H
        self.full_health=STONE_H
        self.hit_rect=OHR
        self.hit_rect.center=self.rect.center
        self.nume=PIATRA
    def update(self):       
        if self.health<=0:
            self.kill()
            self.game.map.data[int(self.rect.centery/TILESIZE)] = replace(self.game.map.data[int(self.rect.centery/TILESIZE)], int(self.rect.centerx/TILESIZE),'1')
             #creare items
            nr_item=random.choice(RANDOM_LIST)
            for i in range(nr_item):
                After_Piatra(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
      
      
            