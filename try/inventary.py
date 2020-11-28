from settings import *
import pygame as pg
from items import *
from os import path
#o lista care sa ai itemul_poza, numele, cate obiecte sun
class Masa_lucru(pg.sprite.Sprite):
    name=MASA_LUCRU
    needs={"LEMN":15}
    nr=0
    poza=MASA_IMG
    material=" "
    def __init__(self, game,x,y):
        self.groups=game.to_put
        pg.sprite.Sprite.__init__(self,self.groups)
        self.name_inv=MASA_LUCRU
        self.game=game
        self.continut=[Tarnacop_lemn,Sabie_lemn,Topor_lemn,Lopata_lemn,Harta,Masa_lucru,Masa_piatra]#mai intra chestul si lab
        self.nr_obiecte=7
        #self.nume=["tarnacop","sabie","topor","lopata"]
        #self.nr=[0,0,0,0]
        #self.poza=[]
        self.image=self.game.table
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
class Masa_piatra(pg.sprite.Sprite):
    name=MASA_PIATRA
    needs={"PIATRA":15}
    #needs={"PIATRA":1}
    nr=0
    poza="masa_piatra.png"
    material=" "
    def __init__(self, game,x,y):
        self.groups=game.to_put
        pg.sprite.Sprite.__init__(self,self.groups)
        self.name_inv=MASA_PIATRA
        self.game=game
        self.continut=[Tarnacop_piatra,Sabie_piatra,Topor_piatra,Lopata_piatra,Nicovala]
        self.nr_obiecte=5
        img_folder_items=path.join(self.game.game_folder,"img\iteme")
        self.image=pg.image.load(path.join(img_folder_items,"masa_piatra.png"))   
        self.image=pg.transform.scale(self.image,(TILESIZE,TILESIZE))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
class Nicovala(pg.sprite.Sprite):
    name=NICOVALA
    needs={"FIER":25,"LEMN":10,"PIATRA":25}
    #needs={"LEMN":2}
    nr=0
    poza="nicovala.png"
    material=" "
    def __init__(self, game,x,y):
        self.groups=game.to_put
        pg.sprite.Sprite.__init__(self,self.groups)
        self.name_inv=MASA_PIATRA
        self.game=game
        self.continut=[Tarnacop_fier,Sabie_fier,Topor_fier,Lopata_fier,Tarnacop_diamant,Sabie_diamant,Topor_diamant,Lopata_diamant,Super_item]
        self.nr_obiecte=9
        #self.nume=["tarnacop","sabie","topor","lopata"]u
        #self.nr=[0,0,0,0]
        #self.poza=[]
        img_folder_items=path.join(self.game.game_folder,"img\iteme")
        self.image=pg.image.load(path.join(img_folder_items,"nicovala.png"))   
        self.image=pg.transform.scale(self.image,(TILESIZE,TILESIZE))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)      
class Harta:
    name=HARTA
    needs={"LEMN":30,"MATERIAL":5,"MAZGA":3}
    nr=0
    poza="harta_small.png"
class Tarnacop_lemn:
    name=TARNACOP_L
    needs={"LEMN":5}
    nr=0
    poza="tarnacop.png"
    material=LEMN
class Sabie_lemn:
     name=SABIE_L
     needs={"LEMN":7}
     nr=0
     poza="sabie.png"
     material=LEMN
class Topor_lemn:
    name=TOPOR_L
    needs={"LEMN":5}
    nr=0
    poza="topor.png"
    material=LEMN
class Lopata_lemn:
    name=LOPATA_L
    needs={"LEMN":7}
    nr=0
    poza="lopata.png"
    material=LEMN
class Tarnacop_piatra:
    name=TARNACOP_P
    needs={"PIATRA":5}
    nr=0
    poza="tarnacop2.png"
    material=LEMN
class Sabie_piatra:
     name=SABIE_P
     needs={"PIATRA":7}
     nr=0
     poza="sabie2.png"
     material=PIATRA
class Topor_piatra:
    name=TOPOR_P
    needs={"PIATRA":5}
    nr=0
    poza="topor2.png"
    material=PIATRA
class Lopata_piatra:
    name=LOPATA_P
    needs={"PIATRA":7}
    nr=0
    poza="lopata2.png"
    material=PIATRA
class Tarnacop_fier:
    name=TARNACOP_F
    needs={"FIER":5}
    nr=0
    poza="tarnacop3.png"
    material=LEMN
class Sabie_fier:
     name=SABIE_F
     needs={"FIER":7}
     nr=0
     poza="sabie3.png"
     material=LEMN
class Topor_fier:
    name=TOPOR_F
    needs={"FIER":5}
    nr=0
    poza="topor3.png"
    material=LEMN
class Lopata_fier:
    name=LOPATA_F
    needs={"FIER":7}
    nr=0
    poza="lopata3.png"
    material=LEMN
class Tarnacop_diamant:
    name=TARNACOP_D
    needs={"DIAMANT":5}
    nr=0
    poza="tarnacop4.png"
    material=LEMN
class Sabie_diamant:
     name=SABIE_D
     needs={"DIAMANT":7}
     nr=0
     poza="sabie4.png"
     material=LEMN
class Topor_diamant:
    name=TOPOR_D
    needs={"DIAMANT":5}
    nr=0
    poza="topor4.png"
    material=LEMN
class Lopata_diamant:
    name=LOPATA_D
    needs={"DIAMANT":7}
    nr=0
    poza="lopata4.png"
    material=LEMN
class Super_item:
    name=SUPER_ITEM
    needs={"LEMN":10, "FIER":15,"PIATRA":10,"DIAMANT":20}
    #needs={"LEMN":2}
    nr=0
    poza="super_item.png"
    material=SUPER_MATERIAL