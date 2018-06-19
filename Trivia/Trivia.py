import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3 # block detector
import time
from random import *
from random import shuffle
import csv

mc = minecraft.Minecraft.create()

Category = []
Question = []
Answer = []
q = 0
Question_number=0
treasure = 0
WIN=10
treasure = 2
Answer_list=[]
Carl = True
Jefferson = False
thompson = False

#Ransom and Rhys's question boi
def GenerateQuestionlists():
    global Category, Question, Answer, q
    f = open('JEOPARDY_CSV.csv', 'r')
    read = csv.DictReader(f)
    for row in read:
        if "www." not in str(row['Question']):
            q += 1
            Category.append(str(row['Category']))
            Question.append(str(row['Question']))
            Answer.append(str(row["Answer"]))

def nextQuestion():
    global Category, Question, Answer, Question_number, Real_Answer, Answer_Blocks, optional_answers, Jefferson, thompson, Carl
    Category_answers=[]
    optional_answers=[]
    Question_number = randint(1,q-1)
    mc.postToChat(Question[Question_number])
    Real_Category = Category[Question_number]
    Real_Answer = Answer[Question_number]
    print(Real_Answer)
    for index in range(len(Category)):
        if Category[index] == Real_Category:
            if index != Question_number:
                Category_answers.append(Answer[index])
    print(Category_answers)
    if len(Category_answers) < 3:
        t = len(Category_answers)
    else:
        t = 3
    for i in range(t):
        x = randint(0,(len(Category_answers)-1))
        optional_answers.append(Category_answers[x])
        del Category_answers[x]
    optional_answers.append(Real_Answer)
    shuffle(optional_answers)
    print(optional_answers)
    mc.postToChat("Orange answer is " + optional_answers[0])
    time.sleep(1)
    mc.postToChat("Purple answer is " + optional_answers[1])
    time.sleep(1)
    mc.postToChat("Blue answer is " + optional_answers[2])
    time.sleep(1)
    mc.postToChat("Yellow answer is " + optional_answers[3])
    Jefferson = True
    thompson = False
    Carl = False

def checkAnswer():
    global Category, Question, Answer, Question_number, Real_Answer, Answer_Blocks, optional_answers, treasure, WIN, thompson, treasure
    SIZE = 10
    list = []
    events = mc.events.pollBlockHits()
    for e in events:  # checks what player has done
        pos = e.pos
        for items in Answer_Blocks:
            if items == pos:
                x = Answer_Blocks.index(items)
                if optional_answers[x] == Real_Answer:
                    treasure += 1
                    if treasure == WIN:
                        mc.postToChat("CORRECT, YOU WIN!")
                        Replay()
                    else:
                        mc.postToChat("Correct! You have " + str(treasure) + " treasure remaining "
                                  "You need " + str(WIN) + " treasure to win. Next Question...")
                        time.sleep(3)
                        thompson = True
                    #mc.getBlocks(pos.x-1, pos.y, pos.z-1, pos.x + SIZE-1, pos.y + SIZE-1, pos.z + SIZE-1)
                else:
                    treasure -= 1
                    if treasure == 0:
                        mc.postToChat("Incorrect. The real answer was " + str(Real_Answer) + " You have no treasure remaining.")
                        mc.postToChat("YOU LOSE")
                        Replay()
                    else:
                        mc.postToChat("Incorrect. The real answer was " + str(Real_Answer) + " You have "
                                        + str(treasure) + " remaining. Next Question...")
                        time.sleep(3)
                        thompson = True


def clear_area():
    SIZE = 50
    pos = mc.player.getTilePos()
    x = pos.x
    y= pos.y
    z = pos.z
    mc.setBlocks(x - SIZE, y, z - SIZE, x + SIZE, y + SIZE, z + SIZE, block.AIR.id)


BlockOrder = [[0, 0, 0],  # the original grid
              [0, 0, 0],
              [0, 0, 0]]

#Matt's question block placement
def spawn_answer(intake):
    global Answer_Blocks
    Answer_Blocks = []
    pos = mc.player.getTilePos()
    x = 0
    placement = 1
    for r in range(0,intake):
        mc.setBlock(pos.x-1, pos.y,  pos.z+2, block.WOOL.id, 1+x)
        coordinate = Vec3(pos.x-1, pos.y,  pos.z+2)
        Answer_Blocks.append(coordinate)
        pos.z += 3
        #pos.x += 3
        x += 1


def Replay():
    global Answer_Blocks,  Jefferson, Stephen
    Jefferson = False
    clear_area()
    spawn_answer(2)
    mc.postToChat("Press the orange block to replay. "
                  " Press the purple block to quit the game.")
    Stephen = True
    while Stephen:
        replay_Rumble()

def replay_Rumble():
    global Carl, Stephen
    events = mc.events.pollBlockHits()
    for e in events:  # checks what player has done
        pos = e.pos
        for items in Answer_Blocks:
            if items == pos:
                if Answer_Blocks.index(items) == 0:
                    Carl = True
                    Stephen = False
                else:
                    clear_area()
                    mc.postToChat("Thanks for playing!")
                    Stephen = False


def beacon_Home():
    SIZE = 30
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x - 10, y - 1, z - 10, x + SIZE + 4, y + SIZE, z + SIZE, block.BEACON.id)
    mc.setBlocks(x - 10, y, z - 10, x + SIZE / 2, y + 10, z + SIZE / 2, block.GLASS.id)
    mc.setBlocks(x - 9, y, z - 9, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)

def glass_house():
    pos = mc.player.getTilePos()
    SIZE = 10
    x = pos.x + 5
    y = pos.y
    z = pos.z
    midx = x + SIZE / 2
    mc.setBlocks(x, y, z, x + SIZE, y + SIZE, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y, z + 1, x + SIZE - 2, y + SIZE - 1, z + SIZE - 2, block.AIR.id)
    mc.setBlocks(midx - 1, y, z, midx + 1, y + 3, z, block.AIR.id)
    mc.setBlocks(x + 3, y + SIZE - 3, z, midx - 3, y, z, block.GLASS.id)
    mc.setBlocks(midx + 3, y + SIZE - 3, z, x + SIZE, y, z, block.GLASS.id)
    mc.setBlocks(x, y + SIZE - 1, z, x + SIZE, y + SIZE - 1, z + SIZE, block.GLASS.id)
    mc.setBlocks(x + 1, y - 1, z + 1, x + SIZE - 2, y - 1, z + SIZE - 2, block.GLASS.id, )

if Carl:
    clear_area()
    beacon_Home()
    glass_house()
    spawn_answer(4)
    GenerateQuestionlists()
    nextQuestion()

while Jefferson:
    checkAnswer()
    if thompson:
        nextQuestion()










    #def anitblock_breaker():
    #for r in range(1, 9):  # how big it scans the blocks
        #BlockOrder2 = getBlocks(Vec3)  # scans the block to see if it's in the original grid
        #if not BlockOrder == BlockOrder2:  # if they are not then it places the original grid
            #mc.setBlocks(BlockOrder, block.# house.id) #placing blocks of the original grid