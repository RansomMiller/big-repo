import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
import time
from random import *
import csv

mc = minecraft.Minecraft.create()

old_Questions = {}

#Ransom and Ryhs's question boi
#def Question():
    #csvreader = csv.reader(open("JEOPARDY_CSV.csv"))
    #x = random.randint(0, 216931)
    #for row in csvreader:
        #if row == x:




#Matt's question block placement
def spawn_answer():
    x = 0
    placement = 1
    for r in range(0,4):
        mc.setBlock(pos.x+2, pos.y,  pos.z, block.WOOL, 3)
        #pos.z +=
        pos.x += 2





spawn_answer()s