import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
import time
from random import *
import csv

mc = minecraft.Minecraft.create()

old_Questions = {}

#Ransom and Rhys's question boi
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





spawn_answer()


SIZE = 30
pos = mc.player.getTilePos()
x =pos.x+5
y = pos.y
z = pos.z
midx = x + SIZE/2
midy = y + SIZE/2
mc.setBlocks(x, y, z, x+SIZE+4, y+SIZE, z+SIZE, block.EMERALD_BLOCK.id)
mc.setBlocks(x, y, z, x+SIZE/2, y+10, z+SIZE/2, block.GLASS.id)
mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)

def glasshouse():
    SIZE = 10
    pos = mc.player.getTilePos()
    x = pos.x + 5
    y = pos.y
    z = pos.z
    midx = x + SIZE / 2
    midy = y + SIZE / 2
    mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y, z + 1, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)
    mc.setBlocks(midx - 1, y, z, midx + 1, y + 3, z, block.AIR.id)
    mc.setBlocks(x + 3, y + SIZE - 3, z, midx - 3, z, block.GLASS.id)
    mc.setBlocks(midx + 3, y + SIZE - 3, z, x + SIZE, z, block.GLASS.id)
    mc.setBlocks(x, y + SIZE - 1, z, x + SIZE, y + SIZE - 1, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y - 1, z + 1, x + SIZE - 2, y - 1, z + SIZE - 2, block.GLASS.id, )
glasshouse()
