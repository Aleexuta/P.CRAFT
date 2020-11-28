import pygame as pg
from settings import *
from os import path
import math
from random import *
vec=pg.math.Vector2
from tilemap import collide_hit_rect
from tilemap import collide_hit_rect_a
from object import *
from inventary import *

def colide_with_walls(sprite,group,directie):
       if directie=="x":
            hits=pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > sprite.hit_rect.centerx:
                    sprite.pos.x=hits[0].rect.left-sprite.hit_rect.width/2
                if hits[0].rect.centerx < sprite.hit_rect.centerx:
                    sprite.pos.x=hits[0].rect.right+sprite.hit_rect.width/2
                sprite.vel.x=0
                sprite.hit_rect.centerx=sprite.pos.x
       if directie=="y":
            hits=pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
            if hits:
                if hits[0].rect.centery> sprite.hit_rect.centery:
                    sprite.pos.y=hits[0].rect.top-sprite.hit_rect.height/2
                if hits[0].rect.centery < sprite.hit_rect.centery:
                    sprite.pos.y=hits[0].rect.bottom+sprite.hit_rect.height/2
                sprite.vel.y=0
                sprite.hit_rect.centery=sprite.pos.y

def add_inventory(self,nume,nr,image_nume,material):
    if nume in self.inventar_nume:
        self.inventar_nr[self.inventar_nume.index(nume)]+=1
    else:
        self.inventar_nume.append(nume)
        ind=self.inventar_nume.index(nume)
        self.inventar_nr.insert(ind,1)
        self.inventar_poze.append(image_nume)
        self.inventar_mat.append(material)
        self.nr_iteme+=1
def remove_inventory(self,nume):
    ind=self.inventar_nume.index(nume)
    self.inventar_nume.remove(self.inventar_nume[ind])
    self.inventar_poze.remove(self.inventar_poze[ind])
    self.inventar_nr.remove(self.inventar_nr[ind])
    self.inventar_mat.remove(self.inventar_mat[ind])
    self.pos_inv=-1
    self.nr_iteme-=1
class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.player
        self.walk_count=WALK_COUNT
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        #self.image=pg.Surface((TILESIZE,TILESIZE))
        self.image=game.stand
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        #self.image.fill(RED)
        self.hit_rect=PLAYER_HIT_RECT
        self.hit_rect.center=self.rect.center
        self.vel=vec(0,0)
        self.pos=vec(x,y)
        self.health=FULL_HEALTH
        self.energy=FULL_ENERGY
        self.damage=PLAYER_DMG_SIMPLE
        self.last_hit=0
        self.photo=0#1-dr,2-sus,3-st,4-jos
        self.movement=0
        self.speed=0   
        self.selectat=" "
        self.selectat_material=" "
        self.tile_old=(0,0)
        self.tile=(int(x/TILESIZE),int(y/TILESIZE))
        self.start_5_sec=self.game.clock.tick()
        self.start_5_sec_bool=False
    def verify_move(self):
          self.walk_count+=SPEED_FRAME
          if self.walk_count>=20:
            self.walk_count=0
    def get_keys(self):#tastele
        self.vel.x=0
        self.vel.y=0
        keys=pg.key.get_pressed()
        if keys[pg.K_q]:
            if self.start_5_sec_bool==False:
                self.start_5_sec=pg.time.get_ticks()
                self.start_5_sec_bool=True
        if keys[pg.K_LEFT]:
            if not self.game.inventory:
                self.vel.x=-self.movement
                self.photo=3
                self.image=self.game.move_left[int(self.walk_count)%4]
            else:
                pass
        if keys[pg.K_RIGHT]:
            if not self.game.inventory:
                self.vel.x=self.movement
                self.photo=1
                self.image=self.game.move_right[int(self.walk_count)%4]
            else:
                pass
        if keys[pg.K_UP]:
            if not self.game.inventory:
                self.vel.y=-self.movement
                self.image=self.game.move_up[int(self.walk_count)%4]
                self.photo=2
        if keys[pg.K_DOWN]:
            if not self.game.inventory:
                self.vel.y=self.movement
                self.photo=4
                self.image=self.game.move_down[int(self.walk_count)%4]
        if self.vel.x!=0 and self.vel.y!=0:
            self.vel*=0.7071
            if self.vel.x>0:
                if self.vel.y>0:
                    self.photo=8
                else: 
                    self.photo=5
            else:
                if self.vel.x>0:
                    self.photo=7
                else: 
                    self.photo=6
        if keys[pg.K_z]:
            #functie cu ce face z-selecteaza, loveste
            self.tasta_z()    
    def tasta_z(self):
        if not self.game.inventory:
            masa=pg.sprite.spritecollide(self,self.game.to_put,False)
            if not masa:#daca nu atinge vreo masa
                if self.game.pos_inv>=0 and self.game.pos_inv<self.game.nr_iteme and self.game.nr_iteme>0 and self.game.inventar_nume[self.game.pos_inv]==MASA_LUCRU:
                    self.game.masa_lemn_clasa=Masa_lucru(self.game,(self.tile[0] )*TILESIZE,(self.tile[1])*TILESIZE)
                    remove_inventory(self.game,MASA_LUCRU)
                elif self.game.pos_inv>=0 and self.game.pos_inv<self.game.nr_iteme and self.game.nr_iteme>0 and self.game.inventar_nume[self.game.pos_inv]==MASA_PIATRA:
                    self.game.masa_piatra_clasa=Masa_piatra(self.game,(self.tile[0] )*TILESIZE,(self.tile[1])*TILESIZE)
                    remove_inventory(self.game,MASA_PIATRA)
                elif self.game.pos_inv>=0 and self.game.pos_inv<self.game.nr_iteme and self.game.nr_iteme>0 and self.game.inventar_nume[self.game.pos_inv]==NICOVALA:
                    self.game.nicovala_clasa=Nicovala(self.game,(self.tile[0] )*TILESIZE,(self.tile[1])*TILESIZE)
                    remove_inventory(self.game,NICOVALA)
                elif self.game.pos_inv>=0 and self.game.pos_inv<self.game.nr_iteme and self.game.nr_iteme>0 and self.game.inventar_nume[self.game.pos_inv]=="MAR":
                    remove_inventory(self.game,"MAR")
                    self.health+=REGENERATE_HEALTH
                    self.health=min(self.health,FULL_HEALTH)
                hits=pg.sprite.spritecollide(self,self.game.all_sprites,False,collide_hit_rect)
                
                for hit in hits:
                    now=pg.time.get_ticks()
                    #verifica daca esti in fata hit ului
                    Ok=False
                    if isinstance(hit,Mob) or isinstance(hit,SuperMob):
                        if self.vel.x>hit.vel.x:
                            if self.photo==1:
                                Ok=True
                        if self.vel.x<hit.vel.x:
                            if self.photo==3:
                                Ok=True
                        if self.vel.y>hit.vel.y:
                            if self.photo==4:
                                Ok=True
                        if self.vel.y<hit.vel.y:
                            if self.photo==2:
                                Ok=True #daca e mob
                    if Ok:
                        if now-self.last_hit>HIT_RATE:
                            self.last_hit=now
                            damage=self.dmg_rate(hit)
                            #vezi daca are energie
                            if isinstance(hit, Mob) or (isinstance(hit, SuperMob) and self.selectat_material==SUPER_MATERIAL):
                                if self.energy>=0:
                                    hit.health-=damage
                                    hit.vel=vec(0,0)
                                    self.energy-=CONSUME_ENERGY
                                    self.game.mob_sound.stop()
                                    self.game.hit_sound.play()
                if self.game.ce_harta==1:
                    hits2=pg.sprite.spritecollide(self,self.game.obstacole,False)
                    for hit2 in hits2:
                        now=pg.time.get_ticks()
                        #daca e masa sau ceva nu se poate culege
                        if now-self.last_hit>HIT_RATE:
                            Ok=False
                            if self.rect.x<=hit2.rect.x and self.rect.y>=hit2.rect.y-32 and self.rect.y<=hit2.rect.y+32:
                                if self.photo==1:
                                    Ok=True
                            if self.rect.x>=hit2.rect.x and self.rect.y>=hit2.rect.y -32 and self.rect.y<=hit2.rect.y+32:
                                if self.photo==3:
                                    Ok=True
                            if self.rect.y>=hit2.rect.y and self.rect.x>=hit2.rect.x-32 and self.rect.x<=hit2.rect.x+32:
                                if self.photo==2:
                                    Ok=True
                            if self.rect.y<=hit2.rect.y and self.rect.x>=hit2.rect.x-32 and self.rect.x<=hit2.rect.x+32:
                                if self.photo==4:
                                    Ok=True #daca e mob
                        if Ok:
                            if now-self.last_hit>HIT_RATE:
                                self.last_hit=now
                                #vezi daca are energie
                                damage=self.dmg_rate(hit2)
                                if self.energy>=0:
                                    hit2.health-=damage
                                    self.energy-=CONSUME_ENERGY
                                    self.game.hit_sound.play()
                                    self.game.mob_sound.stop()
                elif self.game.ce_harta==2:
                    hits3=pg.sprite.spritecollide(self,self.game.obstacole_pestera,False)
                    for hit2 in hits3:
                        now=pg.time.get_ticks()
                        #daca e masa sau ceva nu se poate culege
                        if now-self.last_hit>HIT_RATE:
                            Ok=False
                            if self.rect.x<=hit2.rect.x and self.rect.y>=hit2.rect.y-32 and self.rect.y<=hit2.rect.y+32:
                                if self.photo==1:
                                    Ok=True
                            if self.rect.x>=hit2.rect.x and self.rect.y>=hit2.rect.y -32 and self.rect.y<=hit2.rect.y+32:
                                if self.photo==3:
                                    Ok=True
                            if self.rect.y>=hit2.rect.y and self.rect.x>=hit2.rect.x-32 and self.rect.x<=hit2.rect.x+32:
                                if self.photo==2:
                                    Ok=True
                            if self.rect.y<=hit2.rect.y and self.rect.x>=hit2.rect.x-32 and self.rect.x<=hit2.rect.x+32:
                                if self.photo==4:
                                    Ok=True #daca e mob
                        if Ok:
                            if now-self.last_hit>HIT_RATE:
                                self.last_hit=now
                                #vezi daca are energie
                                damage=self.dmg_rate(hit2)
                                if self.energy>=0:
                                    hit2.health-=damage
                                    self.energy-=CONSUME_ENERGY
                                    self.game.hit_sound.play()
                                    self.game.mob_sound.stop()
                self.energy+=REGENERATE_ENERGY
                self.energy-=CONSUME_ENERGY_SIMPLE            
    def tasta_x(self):
        self.game.masa_lemn=False
        self.game.masa_piatra=False
        self.game.nicovala=False
        self.game.inventory=not self.game.inventory
    def set_speed(self):
        if self.game.ce_harta==1:
            #in cazul in care intru in apa
            hits=pg.sprite.spritecollide(self,self.game.apa,False,collide_hit_rect)
            if hits:
               self.movement=SPEED_MOVEMENT_WATER
               self.speed=SPEED_FRAME_WATER
            else:
                self.movement=SPEED_MOVEMENT_TERRA
                self.speed=SPEED_FRAME_TERRA     
                #in cazul in care sunt deja in apa
            hits=pg.sprite.spritecollide(self,self.game.terra,False,collide_hit_rect)
            if not hits:
               self.movement=SPEED_MOVEMENT_WATER
               self.speed=SPEED_FRAME_WATER
            else:
                self.movement=SPEED_MOVEMENT_TERRA
                self.speed=SPEED_FRAME_TERRA   
        else:
            self.movement=SPEED_MOVEMENT_TERRA
            self.speed=SPEED_FRAME_TERRA 
    def hit_mobs(self):
        hits=pg.sprite.spritecollide(self,self.game.mobs,False,collide_hit_rect)
        for hit in hits:
             now=pg.time.get_ticks()
             if now - self.last_hit > HIT_RATE:
                self.last_hit=now
                if isinstance(hit,Mob):
                    self.health-=MOB_DMG   
                elif isinstance(hit,SuperMob) and self.game.ce_harta==2:
                    self.health-=SUPER_MOB_DMG   
    def dmg_rate(self,hit):
        damage=PLAYER_DMG_SIMPLE
        if self.selectat_material==LEMN:
            if self.selectat==TOPOR_L:
                if hit.nume==COPAC:
                    damage+=PLAYER_DMG_LEMN          
            elif self.selectat==TARNACOP_L:
                if hit.nume==PIATRA:
                    damage+=PLAYER_DMG_LEMN
            elif self.selectat==SABIE_L:
                if hit.nume==MOB:
                    damage+=PLAYER_DMG_LEMN
        elif self.selectat_material==PIATRA:
             if self.selectat==TOPOR_P:
                 if hit.nume==COPAC:
                    damage+=PLAYER_DMG_PIATRA         
             elif self.selectat==TARNACOP_P:
                 if hit.nume==PIATRA:
                    damage+=PLAYER_DMG_PIATRA
             elif self.selectat==SABIE_P:
                 if hit.nume==MOB:
                    damage+=PLAYER_DMG_PIATRA
        elif self.selectat_material==FIER:
             if self.selectat==TOPOR_F:
                 if hit.nume==COPAC:
                    damage+=PLAYER_DMG_FIER        
             elif self.selectat==TARNACOP_F:
                 if hit.nume==PIATRA:
                    damage+=PLAYER_DMG_FIER  
             elif self.selectat==SABIE_F:
                 if hit.nume==MOB:
                    damage+=PLAYER_DMG_FIER  
        elif self.selectat_material==DIAMANT:
             if self.selectat==TOPOR_D:
                 if hit.nume==COPAC:
                    damage+=PLAYER_DMG_DIAMANT        
             elif self.selectat==TARNACOP_D:
                 if hit.nume==PIATRA:
                    damage+=PLAYER_DMG_DIAMANT   
             elif self.selectat==SABIE_D:
                 if hit.nume==MOB:
                    damage+=PLAYER_DMG_DIAMANT  
        elif self.selectat_material==SUPER_MATERIAL:
            if hit.nume==MOB or hit.nume==SUPER_MOB:
                damage+=PLAYER_DMG_SUPER_ITEM
        #alte materiale
        return damage
    def increase_energy(self):
        if self.energy<FULL_ENERGY:
            self.energy+=REGENERATE_ENERGY   
    def collide_with_items(self,group):
        hits=pg.sprite.spritecollide(self,group,False,collide_hit_rect)
        for hit in hits:
           if self.rect.x>=hit.rect.x-32 and self.rect.x<=hit.rect.x+32 and self.rect.y>=hit.rect.y-32 and self.rect.y<=hit.rect.y+32:
                hit.health=0
                hit.object+=1
                add_inventory(self.game,hit.nume,1,hit.image_nume," ") 
                self.game.mob_sound.stop()
                self.game.collect_sound.play()
    def update(self):
        self.verify_move()
        self.get_keys()
        self.increase_energy()
        self.set_speed()
        self.rect.center=self.pos
        self.pos+=self.vel*self.game.dt
        self.tile_old=self.tile
        self.tile=(int(self.pos.x/TILESIZE),int(self.pos.y/TILESIZE))
        self.hit_rect.centerx=self.pos.x
        #colide_with_walls(self,self.game.walls,"x")     
        colide_with_walls(self,self.game.obstacole,"x")   
        colide_with_walls(self,self.game.obstacole_pestera,"x")   
        colide_with_walls(self,self.game.to_put,"x")
        self.hit_rect.centery=self.pos.y
        #colide_with_walls(self,self.game.walls,"y")       
        colide_with_walls(self,self.game.obstacole,"y") 
        colide_with_walls(self,self.game.obstacole_pestera,"y") 
        colide_with_walls(self,self.game.to_put,"y")
        self.rect.center=self.hit_rect.center

        self.collide_with_items(self.game.items)
        
        #cand schimbi harta pune o poza neagra, sa nu mai faca flashuri
        if self.game.in_scara==False:
            if self.game.ce_harta==1:
                if pg.sprite.spritecollide(self,self.game.scara_ob,False,collide_hit_rect):
                    self.game.in_scara=True
                    self.game.screen.blit(self.game.loading,(0,0))
                    self.game.ce_harta=2#trecem de jos in sus  si de sus in jos
                    self.game.draw_pe_ecran_h2() #desenam harta 2 ce se vede
            elif self.game.ce_harta==2:
                if pg.sprite.spritecollide(self,self.game.scara_ob,False,collide_hit_rect):
                    self.game.in_scara=True
                    self.game.screen.blit(self.game.loading,(0,0))
                    self.game.ce_harta=1
                    self.game.draw_pe_ecran_h1()#desenam harta 1 ce se vede
                    
                #    #loituri de la mob
        self.hit_mobs()
        if self.health<=0:
            #self.game.playing=False
            self.game.running=False
            self.game.game_over_bool=True       
class Mob(pg.sprite.Sprite):
     def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.walk_count=WALK_COUNT
        self.image=game.stand_mob
        self.pos=vec(x,y)
        self.vel=vec(0,0)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hit_rect=MOB_HIT_RECT.copy()
        self.hit_rect.center=self.rect.center
        self.acc=vec(0,0)
        self.rot=0
        self.health=MOB_HEALTH
        self.change_dir=RANDOM_STEP
        self.movement=SPEED_MOVEMENT_MOB
        self.speed=SPEED_FRAME
        self.nume=MOB
     def verify_move(self):
          self.walk_count+=SPEED_FRAME
          if self.walk_count>=20:
            self.walk_count=0
     def colide_with_water(self,group):
         #if not pg.sprite.spritecollide(self,self.game.apa,False,collide_hit_rect):
         if not pg.sprite.spritecollide(self,group,False,collide_hit_rect) and self.game.ce_harta==1:
            if not self.raza<RAZA:
                dist=15
                self.acc=vec(0,0)
                self.vel=vec(0,0)  
                if self.rot>45 and self.rot<135:
                    self.pos.y+=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
                elif self.rot>135 or self.rot<-135:
                    self.pos.x+=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot<45 and self.rot>-45:
                    self.pos.x-=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot>-135 and self.rot<-45:
                    self.pos.y-=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
            else:
                dist=15
                self.acc-=self.vel*-1.5
                self.vel=vec(0,0)
                if self.rot>45 and self.rot<135:
                    self.pos.y+=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
                elif self.rot>135 or self.rot<-135:
                    self.pos.x+=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot<45 and self.rot>-45:
                    self.pos.x-=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot>-135 and self.rot<-45:
                    self.pos.y-=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
     def set_speed(self):#true daca atinge pamantul
         if self.game.ce_harta==1:
            hits=pg.sprite.spritecollide(self,self.game.terra,False)
            if hits:
                return True
            return False
         elif self.game.ce_harta==2:
            return True
     def move(self):
         if self.rot>45 and self.rot<135:
            self.image=self.game.mob_move_up[int(self.walk_count)%4].copy()
         elif self.rot>135 or self.rot<-135:
            self.image=self.game.mob_move_left[int(self.walk_count)%4].copy()
         elif self.rot<45 and self.rot>-45:
            self.image=self.game.mob_move_right[int(self.walk_count)%4].copy()
         elif self.rot>-135 and self.rot<-45:
            self.image=self.game.mob_move_down[int(self.walk_count)%4].copy()
     def draw_health(self):
        if self.health<0:
            self.health=0
        fill=(self.health*BAR_LENGHT_MOB/MOB_HEALTH)
        out_rect=pg.Rect(0,0,BAR_LENGHT_MOB,BAR_WIDTH_MOB)
        fill_rect=pg.Rect(0,0,fill,BAR_WIDTH_MOB)
        col=GREEN
        if self.health > 70/100*MOB_HEALTH:
            col = GREEN
        elif self.health > 30/100*MOB_HEALTH:
            col = YELLOW
        elif self.health>0:
            col = RED
        if self.health<MOB_HEALTH:
            pg.draw.rect(self.image,DARKGREY,out_rect)
            pg.draw.rect(self.image,col,fill_rect)       
     def update(self):       
        if not self.game.inventory:            
            self.hit_rect.x=self.pos.x
            colide_with_walls(self,self.game.obstacole,"x")
            colide_with_walls(self,self.game.obstacole_pestera,"x")
            colide_with_walls(self,self.game.apa,"x")
            colide_with_walls(self,self.game.to_put,"x")
            self.hit_rect.y=self.pos.y
            colide_with_walls(self,self.game.obstacole,"y")
            colide_with_walls(self,self.game.obstacole_pestera,"y")
            colide_with_walls(self,self.game.apa,"y")
            colide_with_walls(self,self.game.to_put,"y")
            self.rect.center = self.hit_rect.center
            self.verify_move()
            #calculare distanta pana la player       
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            self.raza=(self.game.player.pos - self.pos).x**2+(self.game.player.pos - self.pos).y**2
            self.raza=math.sqrt(self.raza)
            self.colide_with_water(self.game.terra)
            if self.raza<RAZA:
               # if randrange(0,10,1)<1:
                self.game.mob_sound.play()
                self.move()#roteste poza
                self.acc=vec(self.movement,0).rotate(-self.rot)                
                self.acc+=self.vel*-1.5
                self.vel+=self.acc*self.game.dt
                self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2 #teorema miscarii  
            else:
                
                if self.change_dir%10==0:
                    self.rot=randrange(-180,180)
                    self.move()
                    self.acc=vec(self.movement,0).rotate(-self.rot)
                self.acc+=self.vel*-0.5
                self.vel+=self.acc*self.game.dt
                self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2 #teorema miscarii 
            self.change_dir+=1        
            #lovire de chestii           
            if self.health<=0:
                self.kill()
                self.game.mob_sound.stop()
                self.game.mob_dead.play()
                #self.game.map.data[int(self.rect.centerx/TILESIZE)] = replace(self.game.map.data[int(self.rect.centerx/TILESIZE)], int(self.rect.centery/TILESIZE),'3')
                nr_item=random.choice(RANDOM_LIST_MEDIUM)
                for i in range(nr_item):
                    self.game.mob_dead.play()
                    After_Mobs(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
                nr_item=random.choice(RANDOM_LIST_SMALL)
                for i in range(nr_item):
                    self.game.mob_dead.play()
                    After_Mobs2(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
class SuperMob(pg.sprite.Sprite):
     def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.walk_count=WALK_COUNT
        self.image=game.super_stand_mob
        self.pos=vec(x,y)
        self.vel=vec(0,0)
        self.rect=pg.Rect(0,0,SP_SIZE,SP_SIZE)
        self.rect.center=(x+150,y+300)
        self.hit_rect=SUPER_MOB_HIT_RECT.copy()
        self.hit_rect.center=self.rect.center
        self.acc=vec(0,0)
        self.rot=0
        self.health=SUPER_MOB_HEALTH
        self.change_dir=RANDOM_STEP
        self.movement=SPEED_MOVEMENT_MOB
        self.speed=SPEED_FRAME
        self.nume=SUPER_MOB
     def verify_move(self):
          self.walk_count+=SPEED_FRAME
          if self.walk_count>=20:
            self.walk_count=0
     def colide_with_water(self,group):
         #if not pg.sprite.spritecollide(self,self.game.apa,False,collide_hit_rect):
         if not pg.sprite.spritecollide(self,group,False,collide_hit_rect)and self.game.ce_harta==1:
            if not self.raza<SP_RAZA and self.game.ce_harta==2:
                dist=15
                self.acc=vec(0,0)
                self.vel=vec(0,0)  
                if self.rot>45 and self.rot<135:
                    self.pos.y+=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
                elif self.rot>135 or self.rot<-135:
                    self.pos.x+=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot<45 and self.rot>-45:
                    self.pos.x-=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot>-135 and self.rot<-45:
                    self.pos.y-=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
            else:
                dist=15
                self.acc-=self.vel*-1.5
                self.vel=vec(0,0)
                if self.rot>45 and self.rot<135:
                    self.pos.y+=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
                elif self.rot>135 or self.rot<-135:
                    self.pos.x+=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot<45 and self.rot>-45:
                    self.pos.x-=dist
                    self.vel.x=0
                    self.hit_rect.centerx=self.pos.x
                elif self.rot>-135 and self.rot<-45:
                    self.pos.y-=dist
                    self.vel.y=0
                    self.hit_rect.centery=self.pos.y
     def set_speed(self):#true daca atinge pamantul
         if self.game.ce_harta:
            hits=pg.sprite.spritecollide(self,self.game.terra,False)
            if hits:
                return True
            return False
         elif self.game.ce_harta==2:
             return True
     def move(self):
         if self.rot>45 and self.rot<135:
            self.image=self.game.super_mob_move_up[int(self.walk_count)%4].copy()
         elif self.rot>135 or self.rot<-135:
            self.image=self.game.super_mob_move_left[int(self.walk_count)%4].copy()
         elif self.rot<45 and self.rot>-45:
            self.image=self.game.super_mob_move_right[int(self.walk_count)%4].copy()
         elif self.rot>-135 and self.rot<-45:
            self.image=self.game.super_mob_move_down[int(self.walk_count)%4].copy()
     def draw_health(self):#modifica cu mob health super
        if self.health<0:
            self.health=0
        fill=(self.health*RAP*BAR_LENGHT_MOB/SUPER_MOB_HEALTH)
        out_rect=pg.Rect(0,0,RAP*BAR_LENGHT_MOB,RAP*BAR_WIDTH_MOB)
        fill_rect=pg.Rect(0,0,fill,RAP*BAR_WIDTH_MOB)
        col=GREEN
        if self.health > 70/100*SUPER_MOB_HEALTH:
            col = GREEN
        elif self.health > 30/100*SUPER_MOB_HEALTH:
            col = YELLOW
        elif self.health>0:
            col = RED
        if self.health<SUPER_MOB_HEALTH:
            pg.draw.rect(self.image,DARKGREY,out_rect)
            pg.draw.rect(self.image,col,fill_rect)       
     def update(self):       
        if not self.game.inventory:           
            self.hit_rect.x=self.pos.x
            colide_with_walls(self,self.game.apa,"x")
            self.hit_rect.y=self.pos.y
            colide_with_walls(self,self.game.apa,"y")
            self.rect.center = self.hit_rect.center
            self.verify_move()
            #calculare distanta pana la player      
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            self.raza=(self.game.player.pos - self.pos).x**2+(self.game.player.pos - self.pos).y**2
            self.raza=math.sqrt(self.raza)
            self.colide_with_water(self.game.terra)
            if self.raza<SP_RAZA and self.game.ce_harta==2:#alta raza
               # if randrange(0,10,1)<1:
                self.game.mob_sound.play()
                self.move()#roteste poza
                self.acc=vec(self.movement,0).rotate(-self.rot)              
                self.acc+=self.vel*-1.5
                self.vel+=self.acc*self.game.dt
                self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2 #teorema miscarii  
            else:
                
                if self.change_dir%10==0:
                    self.rot=randrange(-180,180)
                    self.move()
                    self.acc=vec(self.movement,0).rotate(-self.rot)
                self.acc+=self.vel*-0.5
                self.vel+=self.acc*self.game.dt
                self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2 #teorema miscarii 
            self.change_dir+=1      
            #lovire de chestii           
            if self.health<=0:
                self.kill()#castigi nu iti da nimic
                self.game.mob_sound.stop()
                self.game.mob_dead.play()
                self.game.winner_bool=True
                self.game.time_after_win=pg.time.get_ticks()
                nr_item=random.choice(RANDOM_LIST_MEDIUM)
                for i in range(nr_item):
                    self.game.mob_dead.play()
                    After_Mobs(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))
                nr_item=random.choice(RANDOM_LIST_SMALL)
                for i in range(nr_item):
                    self.game.mob_dead.play()
                    After_Mobs2(self.game,self.rect.centerx+random.choice(RANDOM_POS),self.rect.centery+random.choice(RANDOM_POS))

                
    
    
            
        
       
        

