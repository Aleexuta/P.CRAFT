import pygame as pg
from settings import *

class After_Piatra(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="PIATRA"
        self.image_nume="piatra.png"
        self.image=self.game.pietricica.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Copaci(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="LEMN"
        self.image_nume="lemn.png"
        self.image=self.game.lemn.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Copaci2(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="MAR"
        self.image_nume="mar.png"
        self.image=self.game.mar.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Mobs(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="MAZGA"
        self.image_nume="slime.png"
        self.image=self.game.mazga.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Mobs2(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="MATERIAL"
        self.image_nume="fabric.png"
        self.image=self.game.material.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Fier(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="FIER"
        self.image_nume="fier_m.png"
        self.image=self.game.fier_m.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
class After_Diamant(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.nume="DIAMANT"
        self.image_nume="diamant_m.png"
        self.image=self.game.diamant_m.copy()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.health=ITEMS_LIFE
        self.object=0
    def update(self):    
        self.health-=1
        if self.health<=0:
            self.kill()
