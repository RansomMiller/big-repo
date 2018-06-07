import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3 # block detector
import time
from random import *
import csv

mc = minecraft.Minecraft.create()

Category = []
Question = []
Answer = []
q = 1
Question_number=0
Answer_list=[]
#Ransom and Rhys's question boi
def GenerateQuestionlists():
    global Category, Question, Answer, q
    f = open('JEOPARDY_CSV.csv', 'r')
    read = csv.DictReader(f)
    for row in read:
        if "www." not in str(row['Question']):
            Category.append(str(row['Category']))
            Question.append(str(row['Question']))
            Answer.append(str(row["Answer"]))

def nextQuestion():
    global Category, Question, Answer, Question_number
    Category_answers=[]
    wrong_answers=[]
    Question_number = randint(0,111131)
    mc.postToChat(Question[Question_number])
    Real_Answer=(Answer[Question_number])
    for items in Category:
        if items == Category[Question_number]:
            Category_answers.append(Answer[Category.index(items)])
    #for i in range(3):
        #wrong_answers.append(Category_answers(randint(0,len(Category_answers))))


GenerateQuestionlists()
nextQuestion()

BlockOrder = [[0, 0, 0],  # the original grid
              [0, 0, 0],
              [0, 0, 0]]


#Matt's question block placement
def spawn_answer():
    pos = mc.player.getTilePos()
    x = 0
    placement = 1
    for r in range(0,4):
        mc.setBlock(pos.x-1, pos.y,  pos.z+2, block.WOOL.id, 1+x)
        pos.z += 3
        #pos.x += 3
        x += 1


def location():
    SIZE = 30
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    midx = x + SIZE / 2
    midy = y + SIZE / 2
    mc.setBlocks(x - 10, y - 1, z - 10, x + SIZE + 4, y + SIZE, z + SIZE, block.BEACON.id)
    mc.setBlocks(x - 10, y, z - 10, x + SIZE / 2, y + 10, z + SIZE / 2, block.GLASS.id)
    mc.setBlocks(x - 9, y, z - 9, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)
    SIZE = 10
    x = pos.x + 5
    y = pos.y
    z = pos.z
    mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y, z + 1, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)
    mc.setBlocks(midx - 1, y, z, midx + 1, y + 3, z, block.AIR.id)
    mc.setBlocks(x + 3, y + SIZE - 3, z, midx - 3, y, z, block.GLASS.id)
    mc.setBlocks(midx + 3, y + SIZE - 3, z, x + SIZE, y, z, block.GLASS.id)
    mc.setBlocks(x, y + SIZE - 1, z, x + SIZE, y + SIZE - 1, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y - 1, z + 1, x + SIZE - 2, y - 1, z + SIZE - 2, block.GLASS.id, )
location()
spawn_answer()











    #def anitblock_breaker():
    #for r in range(1, 9):  # how big it scans the blocks
        #BlockOrder2 = getBlocks(Vec3)  # scans the block to see if it's in the original grid
        #if not BlockOrder == BlockOrder2:  # if they are not then it places the original grid
            #mc.setBlocks(BlockOrder, block.# house.id) #placing blocks of the original grid