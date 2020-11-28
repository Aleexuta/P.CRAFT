import pygame as pg
from settings import *
import numpy as np
from opensimplex import OpenSimplex
import random
class GenerateMap:
    def __init__(self,nume_fisier):
        self.width=TILESIZE*NR_TILE
        self.height=TILESIZE*NR_TILE
        self.nr_tile_x=NR_TILE
        self.nr_tile_y=NR_TILE
        self.fisier=nume_fisier
        self.tiles=np.zeros((self.nr_tile_x,self.nr_tile_y))
        for i in range(CHENAR_APA,self.nr_tile_x-CHENAR_APA):
            for j in range(CHENAR_APA,self.nr_tile_y-CHENAR_APA):
                self.tiles[i][j]=self.getTile(i,j)
        self.addtext()
    def getTile(self,x,y):
        temp=OpenSimplex()        
        value=abs(temp.noise2d(x,y))*random.randrange(0,NR_TILE,1)*random.randrange(0,NR_TILE,1)/1000
        value=(value**0.40-0.3)
        elem=0
        if value<0.0001:
            elem=1
        if value <0.2:
            elem=1
        elif value <0.5:
            elem=3
            if int(value*10000 % 15)==0:
                elem=5
        elif value <0.8:
            elem=2
        else:
            elem=4
        

        return elem
    def addtext(self):
        f = open(self.fisier, "w")
        for i in range(0,self.nr_tile_y):
            for j in range(0,self.nr_tile_y):
                ts=self.tiles[i][j]
                ts=int(ts)
                f.write(str(ts))
            f.write("\n")
        f.close()

  