import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3 # block detector
import time
from random import *
import csv
import pandas as pd

mc = minecraft.Minecraft.create()

old_Questions = {}
this_Question = {}
q = 1

#Ransom and Rhys's question boi
def Question():
    global old_Questions, q
    Location = r'JEOPARDY_CSV.csv'
    df = pd.read_csv(Location)
    x = random.randint(0, 216930)
    for questions in old_Questions:
        if questions != x:
            this_Question['question'] = df['Question'].iloc[int(x)]
            this_Question['category'] = df['Category'].iloc[int(x)]
            this_Question['answer'] = df['Answer'].iloc[int(x)]
            print("Question" + str(q))
            time.sleep(4)
            print(str(this_Question['question']))
            q += 1
#Question()


BlockOrder = [[0, 0, 0],  # the original grid
              [0, 0, 0],
              [0, 0, 0]]


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
    mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y, z + 1, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)
    mc.setBlocks(midx - 1, y, z, midx + 1, y + 3, z, block.AIR.id)
    mc.setBlocks(x + 3, y + SIZE - 3, z, midx - 3, z, block.GLASS.id)
    mc.setBlocks(midx + 3, y + SIZE - 3, z, x + SIZE, z, block.GLASS.id)
    mc.setBlocks(x, y + SIZE - 1, z, x + SIZE, y + SIZE - 1, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y - 1, z + 1, x + SIZE - 2, y - 1, z + SIZE - 2, block.GLASS.id, )
glasshouse()









def anitblock_breaker():
    for r in range(1, 9):  # how big it scans the blocks
        BlockOrder2 = getBlocks(Vec3)  # scans the block to see if it's in the original grid
        if not BlockOrder == BlockOrder2:  # if they are not then it places the original grid
            mc.setBlocks(BlockOrder, block.# house.id) #placing blocks of the original grid









