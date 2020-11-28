import pygame as pg
from settings import *
from sprites import *
from os import *
from tilemap import *
from object import *
from items import *
from inventary import *
from generatormap import *

class Start:
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode((WIDTH_FULL,HEIGHT_FULL))
        self.start=True
        self.running=True
        self.playing=True
        self.instr=False
        self.load()
        self.menu()
    def load(self):
        self.game_folder = path.dirname(__file__)
        self.start_img=pg.image.load(path.join(self.game_folder,"img\start.jpg"))
        self.start_img=pg.transform.scale(self.start_img,(WIDTH_FULL,HEIGHT_FULL))
        self.start_img_rect=self.start_img.get_rect()
        self.instr_img=pg.image.load(path.join(self.game_folder,"img\instructiuni.png"))
        self.instr_img=pg.transform.scale(self.instr_img,(WIDTH_FULL,HEIGHT_FULL))
        self.instr_img_rect=self.instr_img.get_rect()   
    def menu(self):  
        self.screen.blit(self.start_img,(0,0))
        # self.screen.blit(self.start_img,self.start_img_rect)
        pg.display.flip()
        while self.start and self.running:
         #     self.screen.blit(self.start_img,self.start_img_rect)
             for event in pg.event.get():
                  if event.type==pg.QUIT:
                       if self.playing:
                          self.playing=False
                       self.running=False
                  if event.type==pg.KEYDOWN:
                       if event.key==pg.K_z:
                           self.start=False
                       if event.key==pg.K_x:
                            self.playing=False
                            self.running=False
                            self.start=False
                       if event.key==pg.K_ESCAPE:
                            self.running=False
                            self.playing=False
                            self.star=False
                       if event.key==pg.K_i:
                           self.instr=True
                           self.screen.blit(self.instr_img,(0,0))
                           pg.display.flip()  
def draw_health_player(surf,x,y,life,lung,lat):
    if life<0:
        life=0
    fill=(life*lung)
    out_rect=pg.Rect(x,y,lung,lat)
    fill_rect=pg.Rect(x,y,fill,lat)
    col=RED
    pg.draw.rect(surf,DARKGREY,out_rect)
    pg.draw.rect(surf,col,fill_rect)
def draw_energy_player(surf,x,y,life,lung,lat):
    if life<0:
        life=0
    fill=(life*lung)
    out_rect=pg.Rect(x,y,lung,lat)
    fill_rect=pg.Rect(x,y,fill,lat)
    col=GREEN
    pg.draw.rect(surf,DARKGREY,out_rect)
    pg.draw.rect(surf,col,fill_rect)
class Game:
    def __init__(self):
        pg.init()
        #self.screen_full=pg.display.set_mode((WIDTH_FULL,HEIGHT_FULL))
        self.screen=pg.display.set_mode((WIDTH_FULL,HEIGHT_FULL))
        self.running=True
        self.load_data()
        pg.key.set_repeat(500,100)
        self.clock=pg.time.Clock()
        self.game_over_bool=False
        self.winner_bool=False
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        #self.map=Map(path.join(self.game_folder,"map2.txt"))
        img_folder_player = path.join(self.game_folder,"img\player")
        map_folder = path.join(self.game_folder,"harta")

        #harta
        self.map=Map(path.join(self.game_folder,"harta_random.txt"))
        self.map_pestera=Map(path.join(self.game_folder,"harta_random_pestera.txt"))     
        self.pause_img=pg.image.load(path.join(self.game_folder,"img\pauza.jpg"))
        self.pause_img=pg.transform.scale(self.pause_img,(WIDTH_FULL,HEIGHT_FULL))
        self.pause_rect=self.pause_img.get_rect()
        self.game_over_img=pg.image.load(path.join(self.game_folder,"img\game_over.png"))
        self.game_over_img=pg.transform.scale(self.game_over_img,(WIDTH_FULL,HEIGHT_FULL))
        self.winner_img=pg.image.load(path.join(self.game_folder,"img\winner.png"))
        self.winner_img=pg.transform.scale(self.winner_img,(WIDTH_FULL,HEIGHT_FULL))
       
        #player images
        self.move_right = [pg.image.load(path.join(img_folder_player, "d1.png")),pg.image.load(path.join(img_folder_player, "d2.png")),pg.image.load(path.join(img_folder_player, "d3.png")),pg.image.load(path.join(img_folder_player, "d2.png"))]
        self.move_left = [pg.image.load(path.join(img_folder_player, "s1.png")),pg.image.load(path.join(img_folder_player, "s2.png")),pg.image.load(path.join(img_folder_player, "s3.png")),pg.image.load(path.join(img_folder_player, "s2.png"))]
        self.move_down = [pg.image.load(path.join(img_folder_player, "f1.png")),pg.image.load(path.join(img_folder_player, "f2.png")),pg.image.load(path.join(img_folder_player, "f3.png")),pg.image.load(path.join(img_folder_player, "f2.png"))]
        self.move_up = [pg.image.load(path.join(img_folder_player, "j1.png")),pg.image.load(path.join(img_folder_player, "j2.png")),pg.image.load(path.join(img_folder_player, "j3.png")),pg.image.load(path.join(img_folder_player, "j2.png"))]
        self.stand=self.move_down[1]

        #mob images
        img_folder_mob = path.join(self.game_folder,"img\mob")
        self.mob_move_right = [pg.image.load(path.join(img_folder_mob, "d1.png")),pg.image.load(path.join(img_folder_mob, "d2.png")),pg.image.load(path.join(img_folder_mob, "d3.png")),pg.image.load(path.join(img_folder_mob, "d2.png"))]
        self.mob_move_left = [pg.image.load(path.join(img_folder_mob, "s1.png")),pg.image.load(path.join(img_folder_mob, "s2.png")),pg.image.load(path.join(img_folder_mob, "s3.png")),pg.image.load(path.join(img_folder_mob, "s2.png"))]
        self.mob_move_down = [pg.image.load(path.join(img_folder_mob, "f1.png")),pg.image.load(path.join(img_folder_mob, "f2.png")),pg.image.load(path.join(img_folder_mob, "f3.png")),pg.image.load(path.join(img_folder_mob, "f2.png"))]
        self.mob_move_up = [pg.image.load(path.join(img_folder_mob, "j1.png")),pg.image.load(path.join(img_folder_mob, "j2.png")),pg.image.load(path.join(img_folder_mob, "j3.png")),pg.image.load(path.join(img_folder_mob, "j2.png"))]
        self.stand_mob=self.mob_move_down[1]

        #super mob
        img_folder_mob = path.join(self.game_folder,"img\mob")
        self.super_mob_move_right = [pg.image.load(path.join(img_folder_mob, "d1.png")),pg.image.load(path.join(img_folder_mob, "d2.png")),pg.image.load(path.join(img_folder_mob, "d3.png")),pg.image.load(path.join(img_folder_mob, "d2.png"))]
        self.super_mob_move_left = [pg.image.load(path.join(img_folder_mob, "s1.png")),pg.image.load(path.join(img_folder_mob, "s2.png")),pg.image.load(path.join(img_folder_mob, "s3.png")),pg.image.load(path.join(img_folder_mob, "s2.png"))]
        self.super_mob_move_down = [pg.image.load(path.join(img_folder_mob, "f1.png")),pg.image.load(path.join(img_folder_mob, "f2.png")),pg.image.load(path.join(img_folder_mob, "f3.png")),pg.image.load(path.join(img_folder_mob, "f2.png"))]
        self.super_mob_move_up = [pg.image.load(path.join(img_folder_mob, "j1.png")),pg.image.load(path.join(img_folder_mob, "j2.png")),pg.image.load(path.join(img_folder_mob, "j3.png")),pg.image.load(path.join(img_folder_mob, "j2.png"))]
        self.super_stand_mob=self.super_mob_move_down[1]
        for i in range(0,4,1):
            self.super_mob_move_right[i]=pg.transform.scale(self.super_mob_move_right[i],(SP_SIZE,SP_SIZE))
            self.super_mob_move_left[i]=pg.transform.scale(self.super_mob_move_left[i],(SP_SIZE,SP_SIZE))
            self.super_mob_move_down[i]=pg.transform.scale(self.super_mob_move_down[i],(SP_SIZE,SP_SIZE))
            self.super_mob_move_up[i]=pg.transform.scale(self.super_mob_move_up[i],(SP_SIZE,SP_SIZE))

        #obsacole,harta
        img_folder_obs=path.join(self.game_folder,"img\harta")
        self.background_img=[pg.image.load(path.join(img_folder_obs,"apa.jpg")),pg.image.load(path.join(img_folder_obs,"apa2.jpg")),pg.image.load(path.join(img_folder_obs,"apa3.jpg")),pg.image.load(path.join(img_folder_obs,"apa4.jpg"))]
        self.background_img_pestera=pg.image.load(path.join(img_folder_obs,"pestera.jpg"))
        self.background_img_pestera=pg.transform.scale(self.background_img_pestera,(WIDTH_FULL,HEIGHT_FULL))
        self.loading=pg.image.load(path.join(img_folder_obs,"loading.png"))
        self.loading=pg.transform.scale(self.loading,(WIDTH_FULL,HEIGHT_FULL))
        self.copac=pg.image.load(path.join(img_folder_obs,"copac.png"))
        self.piatra=pg.image.load(path.join(img_folder_obs,"piatra.jpg"))
        self.piatra = pg.transform.scale(self.piatra, (TILESIZE,TILESIZE))
        self.nisip=pg.image.load(path.join(img_folder_obs,"nisip.png"))
        self.nisip=pg.transform.scale(self.nisip,(TILESIZE+1,TILESIZE+1))
        self.iarba=pg.image.load(path.join(img_folder_obs,"iarba.jpg"))
        self.iarba=pg.transform.scale(self.iarba,(TILESIZE+1,TILESIZE+1))
        self.scara=pg.image.load(path.join(img_folder_obs,"scara.png"))
        self.scara = pg.transform.scale(self.scara, (TILESIZE,TILESIZE))
        self.fier=pg.image.load(path.join(img_folder_obs,"fier.jpg"))
        self.fier = pg.transform.scale(self.fier, (TILESIZE,TILESIZE))
        self.diamant=pg.image.load(path.join(img_folder_obs,"diamant.png"))
        self.diamant = pg.transform.scale(self.diamant, (TILESIZE,TILESIZE))

        #masa de lucru
        img_folder_items=path.join(self.game_folder,"img\iteme")
        self.papirus=pg.image.load(path.join(img_folder_items,"inventar.png"))
        self.papirus=pg.transform.scale(self.papirus,(WIDTH_FULL-WIDTH_START_INV,HEIGHT))

        #self.papirus2=pg.image.load(path.join(img_folder_items,"inventar2.png"))
        self.papirus2=pg.transform.scale(self.papirus,(WIDTH_FULL-WIDTH_START_INV,HEIGHT_FULL-HEIGHT2))
        self.papirus3=pg.image.load(path.join(img_folder_items,"inventar3.png"))
        self.papirus3=pg.transform.scale(self.papirus3,(WIDTH_FULL-WIDTH_START_INV,60))
        self.select=pg.image.load(path.join(img_folder_items,"selectat.png"))
        self.table=pg.image.load(path.join(img_folder_items,MASA_IMG))   
        self.table=pg.transform.scale(self.table,(TILESIZE,TILESIZE))

        #items
        #self.mar=pg.image.load(path.join(img_folder_items,"mar.png"))
        self.pietricica=pg.image.load(path.join(img_folder_items,"piatra.png"))
        self.pietricica = pg.transform.scale(self.pietricica, (TILESIZE,TILESIZE))
        self.mar=pg.image.load(path.join(img_folder_items,"mar.png"))
        self.mar = pg.transform.scale(self.mar, (int(TILESIZE/2),int(TILESIZE/2)))
        self.mazga=pg.image.load(path.join(img_folder_items,"slime.png"))
        self.mazga = pg.transform.scale(self.mazga, (int(TILESIZE/2),int(TILESIZE/2)))
        self.material=pg.image.load(path.join(img_folder_items,"fabric.png"))
        self.material = pg.transform.scale(self.material, (int(TILESIZE/2),int(TILESIZE/2)))
        self.lemn=pg.image.load(path.join(img_folder_items,"lemn.png"))
        self.lemn = pg.transform.scale(self.lemn, (int(TILESIZE/2),int(TILESIZE/2)))
        self.fier_m=pg.image.load(path.join(img_folder_items,"fier_m.png"))
        self.fier_m = pg.transform.scale(self.fier_m, (int(TILESIZE/2),int(TILESIZE/2)))
        self.diamant_m=pg.image.load(path.join(img_folder_items,"diamant_m.png"))
        self.diamant_m = pg.transform.scale(self.diamant_m, (int(TILESIZE/2),int(TILESIZE/2)))

        #sound
        music_folder=path.join(self.game_folder,"music")
        pg.mixer.music.load(path.join(music_folder,BACKGROUND_MUSIC))
        self.mob_sound=pg.mixer.Sound(path.join(music_folder,ZOMBIE_SOUND))
        self.mob_sound.set_volume(0.6)
        self.mob_dead=pg.mixer.Sound(path.join(music_folder,ZOMBIE_DEAD))
        self.mob_dead.set_volume(10)
        self.hit_sound=pg.mixer.Sound(path.join(music_folder,HIT_SOUND))
        self.hit_sound.set_volume(0.4)
        self.game_over_sound=pg.mixer.Sound(path.join(music_folder,GAME_OVER_SOUND))
        self.winner_sound=pg.mixer.Sound(path.join(music_folder,WINNER_SOUND))
        self.winner_sound.set_volume(10)
        self.collect_sound=pg.mixer.Sound(path.join(music_folder,COLLECT))
        self.collect_sound.set_volume(1)
    def new(self):
        self.init_inventar()
        #grupuri
        self.player=pg.sprite.Group()
        self.all_sprites=pg.sprite.Group()
        self.mobs=pg.sprite.Group()
        self.walls=pg.sprite.Group()
        #self.copaci=pg.sprite.Group()
        self.terra=pg.sprite.Group()
        self.obstacole=pg.sprite.Group()
        self.obstacole_pestera=pg.sprite.Group()
        self.apa=pg.sprite.Group()
        self.scara_ob=pg.sprite.Group()
        #iteme grupuri
        self.items=pg.sprite.Group()
        self.to_put=pg.sprite.Group()
        self.neobstacole=pg.sprite.Group()
        #crearea obiectelor, playeri, harta
#0 apa
#1 nisip
#2 piatra
#3 iarba
#4 copaci
#5 mobi
#9 player
        #self.player=Player(self,NR_TILE*TILESIZE/2,NR_TILE*TILESIZE/2)
        x=25
        y=25
        self.player=Player(self,x*TILESIZE,y*TILESIZE)
        #eliberare chenar in jurul playerylui
        self.map.data[y] = replace(self.map.data[y], x,'1')
        self.map.data[y-1] = replace(self.map.data[y-1], x-1,'1')
        self.map.data[y-1] = replace(self.map.data[y-1], x,'1')
        self.map.data[y-1] = replace(self.map.data[y-1], x+1,'1')
        self.map.data[y] = replace(self.map.data[y], x-1,'1')
        self.map.data[y] = replace(self.map.data[y], x+1,'1')
        self.map.data[y+1] = replace(self.map.data[y+1], x-1,'1')
        self.map.data[y+1] = replace(self.map.data[y+1], x,'1')
        self.map.data[y+1] = replace(self.map.data[y+1], x+1,'1')
        #bagare scara si inlocuire in harta a elementului
        x=random.randrange(CHENAR_APA,NR_TILE-CHENAR_APA,1)*TILESIZE
        y=random.randrange(CHENAR_APA,NR_TILE-CHENAR_APA,1)*TILESIZE
        x=28
        y=28
        Scara(self,x*TILESIZE,y*TILESIZE)
        self.map.data[y] = replace(self.map.data[y], x,'1')
        self.map_pestera.data[y] = replace(self.map_pestera.data[y], x,'1')
        self.map_pestera.data[y-1] = replace(self.map_pestera.data[y-1], x-1,'1')
        self.map_pestera.data[y-1] = replace(self.map_pestera.data[y-1], x,'1')
        self.map_pestera.data[y-1] = replace(self.map_pestera.data[y-1], x+1,'1')
        self.map_pestera.data[y] = replace(self.map_pestera.data[y], x-1,'1')
        self.map_pestera.data[y] = replace(self.map_pestera.data[y], x+1,'1')
        self.map_pestera.data[y+1] = replace(self.map_pestera.data[y+1], x-1,'1')
        self.map_pestera.data[y+1] = replace(self.map_pestera.data[y+1], x,'1')
        self.map_pestera.data[y+1] = replace(self.map_pestera.data[y+1], x+1,'1')
        
        x=random.randrange(CHENAR_APA,NR_TILE-CHENAR_APA,1)*TILESIZE
        y=random.randrange(CHENAR_APA,NR_TILE-CHENAR_APA,1)*TILESIZE
        x=20
        y=20
        SuperMob(self,x*TILESIZE,y*TILESIZE)
        #Mob(self,(NR_TILE-6)*TILESIZE/2,NR_TILE*TILESIZE/2)
        for i in range(0,NR_TILE):
             for j in range(0,NR_TILE):
                tile=self.map.data[i][j]
                  
                if tile=='1':
                    Nisip(self,j*TILESIZE,i*TILESIZE)
                elif tile=='2':
                    Piatra(self,j*TILESIZE,i*TILESIZE)
                    Nisip(self,j*TILESIZE,i*TILESIZE)
                elif tile=='3':
                    Iarba(self,j*TILESIZE,i*TILESIZE)
                elif tile=='4':
                    Copaci(self,j*TILESIZE,i*TILESIZE)
                    Iarba(self,j*TILESIZE,i*TILESIZE,True)
                elif tile=='5':
                    Mob(self,j*TILESIZE,i*TILESIZE)
                    Iarba(self,j*TILESIZE,i*TILESIZE)
                elif tile=='9':
                    #self.player=Player(self,j*TILESIZE,i*TILESIZE)
                    Nisip(self,j*TILESIZE,i*TILESIZE)
                else: 
                    if i==0:#suntem pe prima linie
                        if j==0:#suntem pe prima coloana
                            #deci colt stanga sus
                            if self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j==self.map.tileheight-1:
                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j>0 and j<self.map.tileheight-1:
                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                    elif i==self.map.tilewidth-1:
                        if j==0:#suntem pe prima coloana
                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j==self.map.tileheight-1:
                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j>0 and j<self.map.tileheight-1:
                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                    elif i>0 and i<self.map.tileheight-1:
                        if j==0:#suntem pe prima coloana
                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0'or self.map.data[i+1][j+1]!='0'or self.map.data[i+1][j]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j==self.map.tileheight-1:
                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i][j-1]!='0'or self.map.data[i+1][j-1]!='0'or self.map.data[i+1][j]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                        elif j>0 and j<self.map.tileheight-1:
                            if self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j-1]!='0' or self.map.data[i][j+1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i+1][j]!='0':
                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE) 
       
        self.camera=Camera(self.map.width,self.map.height)
        self.draw_debug = False
        self.pause=False
        self.background_schimb=0
        self.nr_poza_background=self.background_img[0]
        self.draw_table=False
        self.ce_harta=HARTA_NR
        self.in_scara=False
        self.sound=False
        self.time_after_win=pg.time.get_ticks()
    def init_inventar(self):
        self.invx=WIDTH+START_SCRIS_DREAPTA
        self.invy=START_SCRIS-HEIGHT_INV
        self.inventory=False
        self.inventar_nume=[MASA_LUCRU]
        self.inventar_nr=[1]
        self.inventar_poze=["masa.png"]
        self.inventar_mat=[" "]
        self.nr_iteme=1
        self.pos_inv=-1
        self.hand=-1
        self.masa_lemn=False
        self.masa_piatra=False
        self.nicovala=False
        self.hand_masa_lemn=1
        self.invy_lemn=START_SCRIS-HEIGHT_INV
        self.old_selectat=-1
    def run(self):
        self.playing=True
        pg.mixer.music.play(loops=-2)
        while self.playing:
            self.dt=self.clock.tick(FPS)/1000
            self.time=self.clock.tick(FPS)/1000
            self.events()
            if not self.pause:
                self.update()
                #incerc sa desenez ce se vede pe camera doar
            #self.camera.draw(self,self.player)
            self.draw()         
    def draw_pe_ecran_h1(self):
        for i in range(self.player.tile[1]-MARGINE2,self.player.tile[1]+MARGINE2):
            for j in range(self.player.tile[0]-MARGINE,self.player.tile[0]+MARGINE):
                        tile=self.map.data[i][j]  #~schimba numele aici dupa ce vezi ca merge
                        if tile=='1':
                            Nisip(self,j*TILESIZE,i*TILESIZE)
                        elif tile=='2':
                            Piatra(self,j*TILESIZE,i*TILESIZE)
                            Nisip(self,j*TILESIZE,i*TILESIZE)
                        elif tile=='3':
                            Iarba(self,j*TILESIZE,i*TILESIZE)
                        elif tile=='4':
                            Copaci(self,j*TILESIZE,i*TILESIZE)
                            Iarba(self,j*TILESIZE,i*TILESIZE,True)
                        elif tile=='5':
                            Mob(self,j*TILESIZE,i*TILESIZE)
                            Iarba(self,j*TILESIZE,i*TILESIZE)
                        elif tile=='9':
                            #self.player=Player(self,j*TILESIZE,i*TILESIZE)
                            Nisip(self,j*TILESIZE,i*TILESIZE)
                        else: 
                            if i==0:#suntem pe prima linie
                                if j==0:#suntem pe prima coloana
                                    #deci colt stanga sus
                                    if self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.map.tileheight-1:
                                    if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.map.tileheight-1:
                                    if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                            elif i==self.map.tilewidth-1:
                                if j==0:#suntem pe prima coloana
                                    if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.map.tileheight-1:
                                    if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.map.tileheight-1:
                                    if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                            elif i>0 and i<self.map.tileheight-1:
                                if j==0:#suntem pe prima coloana
                                    if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0'or self.map.data[i+1][j+1]!='0'or self.map.data[i+1][j]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j==self.map.tileheight-1:
                                    if self.map.data[i-1][j]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i][j-1]!='0'or self.map.data[i+1][j-1]!='0'or self.map.data[i+1][j]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                elif j>0 and j<self.map.tileheight-1:
                                    if self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j-1]!='0' or self.map.data[i][j+1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i+1][j]!='0':
                                        Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE) 
    def draw_pe_ecran_h2(self):
        for i in range(self.player.tile[1]-MARGINE2,self.player.tile[1]+MARGINE2):
            for j in range(self.player.tile[0]-MARGINE,self.player.tile[0]+MARGINE):
                        tile=self.map_pestera.data[i][j]  #~schimba numele aici dupa ce vezi ca merge
                        if tile=='2':
                            Diamant(self,j*TILESIZE,i*TILESIZE)
                        if tile=='3':
                            Fier(self,j*TILESIZE,i*TILESIZE)
                        if tile=='4':
                            Piatra2(self,j*TILESIZE,i*TILESIZE)
                        if tile=='5':
                            Mob(self,j*TILESIZE,i*TILESIZE)                            
    def draw(self):
       pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
       if pg.time.get_ticks()-self.time_after_win>=3000 and self.winner_bool:
            self.screen.blit(self.winner_img,(0,0))
            self.mob_sound.stop()
            if self.sound==False:
                self.winner_sound.play()
                self.sound=True
       elif self.game_over_bool:
            self.screen.blit(self.game_over_img,(0,0))
            self.mob_sound.stop()
            if self.sound==False:
                self.game_over_sound.play()
                self.sound=True
       #self.draw_grid()
       #deseneaza harta
       else:     
           if not pg.sprite.spritecollide(self.player,self.scara_ob,False,collide_hit_rect):
               self.in_scara=False
               if self.ce_harta==1:
                   self.screen.blit(self.nr_poza_background,(0,0))
                   self.background_schimb+=1
                   if self.background_schimb%10==0:
                       self.nr_poza_background=random.choice(self.background_img)
                       self.background_schimb=0
               elif self.ce_harta==2:
                   self.screen.blit(self.background_img_pestera,(0,0))
              #afisam nisip, piatra, doar in harta 1
               for ob in self.neobstacole:
                   #afisam nisipul, iarba
                   if not isinstance(ob,Apa):
                       if self.ce_harta!=1 or ob.rect.centerx<self.player.pos.x-(MARGINE+1)*TILESIZE or ob.rect.centerx>self.player.pos.x+(MARGINE+1)*TILESIZE or ob.rect.centery<self.player.pos.y-(MARGINE2+1)*TILESIZE  or ob.rect.centery>self.player.pos.y +(MARGINE2+1)*TILESIZE:
                            ob.kill()
                       else:
                            self.screen.blit(ob.image,self.camera.apply(ob))
                   if self.draw_debug:
                       pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(ob.rect), 1)
               #afisam obiectele de colectat
               for obs in self.items:
                   if obs.health>80 or obs.health % 6:
                       self.screen.blit(obs.image,self.camera.apply(obs))
               #afisam copaci, piatra
               for ob in self.obstacole:
                   if self.ce_harta!=1 or ob.health <=0 or ob.rect.centerx<self.player.pos.x-(MARGINE+1)*TILESIZE or ob.rect.centerx>self.player.pos.x+(MARGINE+1)*TILESIZE or ob.rect.centery<self.player.pos.y-(MARGINE2+1)*TILESIZE  or ob.rect.centery>self.player.pos.y +(MARGINE2+1)*TILESIZE:
                       ob.kill()
                   else:
                       draw_health_obs(ob)
                       self.screen.blit(ob.image,self.camera.apply(ob))
                       if self.draw_debug:
                               pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(ob.rect), 1)
               for ob in self.obstacole_pestera:
                   if self.ce_harta!=2 or ob.health <=0 or ob.rect.centerx<self.player.pos.x-(MARGINE+1)*TILESIZE or ob.rect.centerx>self.player.pos.x+(MARGINE+1)*TILESIZE or ob.rect.centery<self.player.pos.y-(MARGINE2+1)*TILESIZE  or ob.rect.centery>self.player.pos.y +(MARGINE2+1)*TILESIZE:
                       ob.kill()
                   else:
                       draw_health_obs(ob)
                       self.screen.blit(ob.image,self.camera.apply(ob))
                       if self.draw_debug:
                               pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(ob.rect), 1)      
               #readaugare obiecte pe harta 1
               if self.ce_harta==1:
                   if self.player.tile!=self.player.tile_old:
                       if self.player.photo==2 or self.player.photo==4 or self.player.photo>4 :
                            if self.player.photo==4:
                                    i=self.player.tile[1]+MARGINE2
                            elif self.player.photo==2:
                                    i=self.player.tile[1]-MARGINE2
                            elif self.player.photo==5 or self.player.photo==6:
                                i=self.player.tile[1]-MARGINE2
                            elif self.player.photo==7 or self.player.photo==8:
                                i=self.player.tile[1]+MARGINE2
                            for j in range(self.player.tile[0]-MARGINE-1,self.player.tile[0]+MARGINE+1):

                                tile=self.map.data[i][j]
                     
                                if tile=='1':
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='2':
                                    Piatra(self,j*TILESIZE,i*TILESIZE)
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='3':
                                    Iarba(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='4':
                                    Copaci(self,j*TILESIZE,i*TILESIZE)
                                    Iarba(self,j*TILESIZE,i*TILESIZE,True)
                                elif tile=='5':
                                    Mob(self,j*TILESIZE,i*TILESIZE)
                                    Iarba(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='9':
                                    #self.player=Player(self,j*TILESIZE,i*TILESIZE)
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                else: 
                                    if i==0:#suntem pe prima linie
                                        if j==0:#suntem pe prima coloana
                                            #deci colt stanga sus
                                            if self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                    elif i==self.map.tilewidth-1:
                                        if j==0:#suntem pe prima coloana
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                    elif i>0 and i<self.map.tileheight-1:
                                        if j==0:#suntem pe prima coloana
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0'or self.map.data[i+1][j+1]!='0'or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i][j-1]!='0'or self.map.data[i+1][j-1]!='0'or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j-1]!='0' or self.map.data[i][j+1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE) 
                       if self.player.photo==1 or self.player.photo==3 or self.player.photo>4:
                           if self.player.photo==1:
                                    j=self.player.tile[0]+MARGINE
                           elif self.player.photo==3:
                                     j=self.player.tile[0]-MARGINE
                           elif self.player.photo==7 or self.player.photo==6:
                                j=self.player.tile[0]-MARGINE
                           elif self.player.photo==8 or self.player.photo==8:
                                j=self.player.tile[0]+MARGINE
                           for i in range(self.player.tile[1]-MARGINE2-1,self.player.tile[1]+MARGINE2+1):
                    
                                 #elif self.player.photo==5 or self.player.photo==8:
                                 #   i=int(self.player.pos.x/TILESIZE)+MARGINE2
                                 #elif self.player.photo==7 or self.player.photo==6:
                                 #   i=int(self.player.pos.x/TILESIZE)-MARGINE2
                                tile=self.map.data[i][j]
                    
                                if tile=='1':
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='2':
                                    Piatra(self,j*TILESIZE,i*TILESIZE)
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='3':
                                    Iarba(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='4':
                                    Copaci(self,j*TILESIZE,i*TILESIZE)
                                    Iarba(self,j*TILESIZE,i*TILESIZE,True)
                                elif tile=='5':
                                    Mob(self,j*TILESIZE,i*TILESIZE)
                                    Iarba(self,j*TILESIZE,i*TILESIZE)
                                elif tile=='9':
                                    #self.player=Player(self,j*TILESIZE,i*TILESIZE)
                                    Nisip(self,j*TILESIZE,i*TILESIZE)
                                else: 
                                    if i==0:#suntem pe prima linie
                                        if j==0:#suntem pe prima coloana
                                            #deci colt stanga sus
                                            if self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j]!='0' or self.map.data[i+1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                    elif i==self.map.tilewidth-1:
                                        if j==0:#suntem pe prima coloana
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i][j-1]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0'or self.map.data[i][j+1]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                    elif i>0 and i<self.map.tileheight-1:
                                        if j==0:#suntem pe prima coloana
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j+1]!='0'or self.map.data[i+1][j+1]!='0'or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j==self.map.tileheight-1:
                                            if self.map.data[i-1][j]!='0' or self.map.data[i-1][j-1]!='0' or self.map.data[i][j-1]!='0'or self.map.data[i+1][j-1]!='0'or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE)
                                        elif j>0 and j<self.map.tileheight-1:
                                            if self.map.data[i-1][j-1]!='0' or self.map.data[i-1][j]!='0' or self.map.data[i-1][j+1]!='0' or self.map.data[i][j-1]!='0' or self.map.data[i][j+1]!='0' or self.map.data[i+1][j-1]!='0' or self.map.data[i+1][j+1]!='0' or self.map.data[i+1][j]!='0':
                                                Apa(self,j*TILESIZE,i*TILESIZE,TILESIZE,TILESIZE) 
               elif self.ce_harta==2:
                  if self.player.tile!=self.player.tile_old:
                       if self.player.photo==2 or self.player.photo==4 or self.player.photo>4 :
                            if self.player.photo==4:
                                    i=self.player.tile[1]+MARGINE2
                            elif self.player.photo==2:
                                    i=self.player.tile[1]-MARGINE2
                            elif self.player.photo==5 or self.player.photo==6:
                                i=self.player.tile[1]-MARGINE2
                            elif self.player.photo==7 or self.player.photo==8:
                                i=self.player.tile[1]+MARGINE2
                            for j in range(self.player.tile[0]-MARGINE,self.player.tile[0]+MARGINE):

                                tile=self.map_pestera.data[i][j]
                     
                                if tile=='2':
                                    Diamant(self,j*TILESIZE,i*TILESIZE)
                                if tile=='3':
                                    Fier(self,j*TILESIZE,i*TILESIZE)
                                if tile=='4':
                                    Piatra2(self,j*TILESIZE,i*TILESIZE)
                                if tile=='5':
                                    Mob(self,j*TILESIZE,i*TILESIZE)
                            
                       if self.player.photo==1 or self.player.photo==3 or self.player.photo>4:
                           if self.player.photo==1:
                                    j=self.player.tile[0]+MARGINE
                           elif self.player.photo==3:
                                     j=self.player.tile[0]-MARGINE
                           elif self.player.photo==7 or self.player.photo==6:
                                j=self.player.tile[0]-MARGINE
                           elif self.player.photo==8 or self.player.photo==8:
                                j=self.player.tile[0]+MARGINE
                           for i in range(self.player.tile[1]-MARGINE2,self.player.tile[1]+MARGINE2):
                    
                                 #elif self.player.photo==5 or self.player.photo==8:
                                 #   i=int(self.player.pos.x/TILESIZE)+MARGINE2
                                 #elif self.player.photo==7 or self.player.photo==6:
                                 #   i=int(self.player.pos.x/TILESIZE)-MARGINE2
                                 tile=self.map_pestera.data[i][j]
                    
                                 if tile=='2':
                                    Diamant(self,j*TILESIZE,i*TILESIZE)
                                 if tile=='3':
                                    Fier(self,j*TILESIZE,i*TILESIZE)
                                 if tile=='4':
                                    Diamant(self,j*TILESIZE,i*TILESIZE)
                                 if tile=='5':
                                    Mob(self,j*TILESIZE,i*TILESIZE)                           
               #afisam masele doar in harta 1
               for ob in self.to_put:
                   if self.ce_harta==1:
                       self.screen.blit(ob.image,self.camera.apply(ob))
                   if self.draw_debug:
                           pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(ob.rect), 1)
               #afisam scara oricum in aceasi pozitie
               for sc in self.scara_ob:
                    self.screen.blit(sc.image,self.camera.apply(sc)) 
               #afisam mobii oricum
               for sprite in self.all_sprites:
                   if isinstance(sprite,Mob):
                       sprite.draw_health()
                       if sprite.rect.centerx<self.player.pos.x-(MARGINE+1)*TILESIZE or sprite.rect.centerx>self.player.pos.x+(MARGINE+1)*TILESIZE or sprite.rect.centery<self.player.pos.y-(MARGINE2+1)*TILESIZE  or sprite.rect.centery>self.player.pos.y +(MARGINE2+1)*TILESIZE:
                            sprite.kill()
                   if not isinstance(sprite,SuperMob):
                            self.screen.blit(sprite.image,self.camera.apply(sprite))
                   if isinstance(sprite,SuperMob)and self.ce_harta==2:
                       sprite.draw_health()
                       self.screen.blit(sprite.image,self.camera.apply(sprite))
                   if self.draw_debug:
                        pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)           
               draw_health_player(self.screen,10,10,self.player.health/BAR_LENGHT_PL,BAR_LENGHT_PL,BAR_WIDTH_PL) 
               draw_energy_player(self.screen,10,40,self.player.energy/BAR_LENGHT_PL,BAR_LENGHT_PL,BAR_WIDTH_PL) 
               self.draw_inventar()
                   #verifcare ce a disparut
               if self.pause:
                   self.screen.blit(self.pause_img,self.pause_rect)
                   pg.draw.rect(self.screen,RED,self.pause_rect,1)
               #cat timp de  imortalitate mai avem
               timp_scurs=pg.time.get_ticks()-self.player.start_5_sec
               if self.player.start_5_sec_bool and timp_scurs<=5000:
                   self.text=pg.font.SysFont(None,SIZE_SCRIS*2).render(str(5-int(timp_scurs/1000)),True,RED)
                   self.screen.blit(self.text,[WIDTH_START_INV+120+START_SCRIS_DREAPTA,HEIGHT2+160])
                   self.player.health=FULL_HEALTH
       pg.display.flip()      
    def draw_inventar(self):
       #elementul de selectat, jos dreapta+scris ce e selectat
       self.screen.blit(self.papirus3,(WIDTH_START_INV,HEIGHT2+140))
       if self.pos_inv>=0 and self.nr_iteme>0 and self.pos_inv<self.nr_iteme:
           self.text=pg.font.SysFont(None,SIZE_SCRIS).render(self.inventar_nume[self.pos_inv],True,RED)
           self.screen.blit(self.text,[WIDTH_START_INV+80+START_SCRIS_DREAPTA,HEIGHT2+160])
           self.player.selectat=self.inventar_nume[self.pos_inv]#ce avem in mana
           self.player.selectat_material=self.inventar_mat[self.pos_inv]        
          #poza
           self.screen.blit(self.select_img,(WIDTH_START_INV+20+START_SCRIS_DREAPTA,HEIGHT2+150))
       k=START_SCRIS+10
       if self.masa_lemn:#ne aflam la masa de lucru lemn
           self.screen.blit(self.papirus,(WIDTH_START_INV,0))
           self.screen.blit(self.papirus2,(WIDTH2,HEIGHT2))
           if self.invy_lemn >=START_SCRIS:
                self.screen.blit(self.select,(self.invx+20,self.invy_lemn))
           for i in self.masa_lemn_clasa.continut:
               #scris elemente
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(i.name,True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NUME+START_SCRIS_DREAPTA,k])
               #scris nr pe care il avem
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(i.nr),True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NR+START_SCRIS_DREAPTA,k])
               k+=HEIGHT_INV
               #scris ce avem nevoie
           k2=START_SCRIS+10+HEIGHT2
           ind2=int(self.invy_lemn/HEIGHT_INV)-1
           if ind2>=0:
               ii=self.masa_lemn_clasa.continut[ind2]
               for j in ii.needs:#desenam pt cel selectat
                   #numele
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(j,True,RED)
                   self.screen.blit(self.text,[WIDTH2+80+START_SCRIS_DREAPTA,k2])
                   #cate avem nevoie
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(ii.needs[j]),True,RED)
                   self.screen.blit(self.text,[WIDTH2+150+START_SCRIS_DREAPTA,k2])
                   k2+=HEIGHT_INV
       elif self.masa_piatra:#ne aflam la masa de lucru piatra
           self.screen.blit(self.papirus,(WIDTH_START_INV,0))
           self.screen.blit(self.papirus2,(WIDTH2,HEIGHT2))
           if self.invy_lemn >=START_SCRIS:
                self.screen.blit(self.select,(self.invx+20,self.invy_lemn))
           for i in self.masa_piatra_clasa.continut:
               #scris elemente
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(i.name,True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NUME+START_SCRIS_DREAPTA,k])
               #scris nr pe care il avem
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(i.nr),True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NR+START_SCRIS_DREAPTA,k])
               k+=HEIGHT_INV
               #scris ce avem nevoie
           k2=START_SCRIS+10+HEIGHT2
           ind2=int(self.invy_lemn/HEIGHT_INV)-1
           if ind2>=0:
               ii=self.masa_piatra_clasa.continut[ind2]
               for j in ii.needs:#desenam pt cel selectat
                   #numele
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(j,True,RED)
                   self.screen.blit(self.text,[WIDTH2+80+START_SCRIS_DREAPTA,k2])
                   #cate avem nevoie
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(ii.needs[j]),True,RED)
                   self.screen.blit(self.text,[WIDTH2+START_SCRIS_NR+START_SCRIS_DREAPTA,k2])
                   k2+=HEIGHT_INV
       elif self.nicovala:#ne aflam la nicovala
           self.screen.blit(self.papirus,(WIDTH_START_INV,0))
           self.screen.blit(self.papirus2,(WIDTH2,HEIGHT2))
           if self.invy_lemn >=START_SCRIS:
                self.screen.blit(self.select,(self.invx+20,self.invy_lemn))
           for i in self.nicovala_clasa.continut:
               #scris elemente
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(i.name,True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NUME+START_SCRIS_DREAPTA,k])
               #scris nr pe care il avem
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(i.nr),True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NR+START_SCRIS_DREAPTA,k])
               k+=HEIGHT_INV
               #scris ce avem nevoie
           k2=START_SCRIS+10+HEIGHT2
           ind2=int(self.invy_lemn/HEIGHT_INV)-1
           if ind2>=0:
               ii=self.nicovala_clasa.continut[ind2]
               for j in ii.needs:#desenam pt cel selectat
                   #numele
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(j,True,RED)
                   self.screen.blit(self.text,[WIDTH2+80+START_SCRIS_DREAPTA,k2])
                   #cate avem nevoie
                   self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(ii.needs[j]),True,RED)
                   self.screen.blit(self.text,[WIDTH2+150+START_SCRIS_DREAPTA,k2])
                   k2+=HEIGHT_INV    
       elif self.inventory:#suntem in inventar
           k=START_SCRIS+10
           self.screen.blit(self.papirus,(WIDTH_START_INV,0))
           if self.invy >=START_SCRIS:
               self.screen.blit(self.select,(self.invx+20,self.invy))
           image_folder=path.join(self.game_folder,"img\iteme")
           for i in self.inventar_nume:
               #nume
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(i,True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NUME+START_SCRIS_DREAPTA,k])
               ind=self.inventar_nume.index(i)
               #nr
               afis=self.inventar_nr[ind]
               self.text=pg.font.SysFont(None,SIZE_SCRIS).render(str(afis),True,RED)
               self.screen.blit(self.text,[WIDTH_START_INV+START_SCRIS_NR+START_SCRIS_DREAPTA,k])
               #poza
               
               img=pg.image.load(path.join(image_folder,self.inventar_poze[ind]))
               img=pg.transform.scale(img,(SIZE_INVENTAR,SIZE_INVENTAR))
               self.screen.blit(img,(WIDTH_START_INV+10+START_SCRIS_DREAPTA,k-5))
               k+=HEIGHT_INV
    def construim(self,masa_lucru):
        can=True
        ce_vrem=masa_lucru.continut[self.pos_inv]
        for elem in ce_vrem.needs:
            if elem in self.inventar_nume:
                ind=self.inventar_nume.index(elem)
                if ce_vrem.needs[elem]>self.inventar_nr[ind]:
                    can=False
            else:
                can=False
        if can:
            ce_vrem.nr+=1
            avem_ce_ne_tebe=True
            for elem in ce_vrem.needs:
                if elem in self.inventar_nume:
                    ind=self.inventar_nume.index(elem)
                    self.inventar_nr[ind]-=ce_vrem.needs[elem]
                    if self.inventar_nr[ind]<=0:
                        remove_inventory(self,self.inventar_nume[ind])
                        ind-=1
                add_inventory(self,ce_vrem.name,1,ce_vrem.poza,ce_vrem.material)          
    def events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key==pg.K_p:
                    self.pause=not self.pause
                    #daca se afla in inventar, cheie sus jos, z(nu pun la get_keys pt ca merge lung, aici un click=o comanda, acolo un click=comanda lunga)
                if event.key==pg.K_ESCAPE:
                    self.running=False
                    self.playing=False
                if event.key==pg.K_x:
                    self.hand=-1
                    self.inventory=not self.inventory
                    if self.masa_lemn:
                        self.masa_lemn=False
                        self.inventory=False
                    elif self.masa_piatra:
                        self.masa_piatra=False
                        self.inventory=False
                    elif self.nicovala:
                        self.nicovala=False
                        self.inventory=False
                    self.invx=WIDTH_START_INV+START_SCRIS_DREAPTA
                    self.invy=START_SCRIS-HEIGHT_INV
                    self.invy_lemn=START_SCRIS-HEIGHT_INV
                if event.key==pg.K_UP:
                    if self.masa_lemn:
                        self.invy_lemn-=HEIGHT_INV
                        self.invy_lemn=max(self.invy_lemn,START_SCRIS-HEIGHT_INV)
                        self.hand-=1
                        self.hand=max(self.hand,0)
                    elif self.masa_piatra:
                        self.invy_lemn-=HEIGHT_INV
                        self.invy_lemn=max(self.invy_lemn,START_SCRIS-HEIGHT_INV)
                        self.hand-=1
                        self.hand=max(self.hand,0)
                    elif self.nicovala:
                        self.invy_lemn-=HEIGHT_INV
                        self.invy_lemn=max(self.invy_lemn,START_SCRIS-HEIGHT_INV)
                        self.hand-=1
                        self.hand=max(self.hand,0)
                    elif self.inventory:
                        self.invy-=HEIGHT_INV
                        self.invy=max(self.invy,START_SCRIS-HEIGHT_INV)
                        self.hand-=1
                        self.hand=max(self.hand,0)          
                if event.key==pg.K_DOWN:
                    if self.masa_lemn:
                        self.invy_lemn+=HEIGHT_INV
                        self.invy_lemn=min(self.invy_lemn,(self.masa_lemn_clasa.nr_obiecte-1)*HEIGHT_INV+START_SCRIS)
                        self.hand+=1
                        self.hand=min(self.hand,self.masa_lemn_clasa.nr_obiecte-1) 
                    elif self.masa_piatra:
                        self.invy_lemn+=HEIGHT_INV
                        self.invy_lemn=min(self.invy_lemn,(self.masa_piatra_clasa.nr_obiecte-1)*HEIGHT_INV+START_SCRIS)
                        self.hand+=1
                        self.hand=min(self.hand,self.masa_piatra_clasa.nr_obiecte-1) 
                    elif self.nicovala:
                        self.invy_lemn+=HEIGHT_INV
                        self.invy_lemn=min(self.invy_lemn,(self.nicovala_clasa.nr_obiecte-1)*HEIGHT_INV+START_SCRIS)
                        self.hand+=1
                        self.hand=min(self.hand,self.nicovala_clasa.nr_obiecte-1)                   
                    elif self.inventory:
                        self.invy+=HEIGHT_INV
                        self.invy=min(self.invy,(self.nr_iteme-1)*HEIGHT_INV+START_SCRIS)
                        self.hand+=1
                        self.hand=min(self.hand,self.nr_iteme-1)
                if event.key==pg.K_z:

                    if self.masa_lemn:
                        self.pos_inv=self.hand
                        self.construim(self.masa_lemn_clasa)
                    elif self.masa_piatra:
                        self.pos_inv=self.hand
                        self.construim(self.masa_piatra_clasa)
                        #daca suntem in masa de lucru vedem daca avem ce e nevoie si construim
                    elif self.nicovala:
                        self.pos_inv=self.hand
                        self.construim(self.nicovala_clasa)
                    elif self.inventory:
                        self.pos_inv=self.hand
                        if self.pos_inv>=0:
                            image_folder=path.join(self.game_folder,"img\iteme")
                            self.select_img=pg.image.load(path.join(image_folder,self.inventar_poze[self.pos_inv]))
                            self.select_img=pg.transform.scale(self.select_img,(SIZE_INVENTAR,SIZE_INVENTAR))
                    masa=pg.sprite.spritecollide(self.player,self.to_put,False)
                    if masa and self.inventory==False:
                        for mas in masa:
                            self.invx=WIDTH_START_INV+START_SCRIS_DREAPTA
                            self.invy_lemn=START_SCRIS-HEIGHT_INV
                            self.inventory= True
                            if isinstance(mas,Masa_lucru):
                                self.masa_lemn=True
                                self.masa_piatra=False
                                self.nicovala=False
                            elif isinstance(mas,Masa_piatra):
                                self.masa_piatra=True
                                self.masa_lemn=False
                                self.nicovala=False
                            elif isinstance(mas,Nicovala):
                                self.masa_piatra=False
                                self.masa_lemn=False
                                self.nicovala=True
    def update(self): 
        self.all_sprites.update()
        self.obstacole.update()
        self.obstacole_pestera.update()
        self.camera.update(self.player)
        self.items.update()

s=Start()
GenerateMap("harta_random.txt")
GenerateMap("harta_random_pestera.txt")
if s.running:
    g=Game()
    while g.running:
        g.new()
        g.run()
pg.quit()