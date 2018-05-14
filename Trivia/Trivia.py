import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
import time
import random
import csv

mc = minecraft.Minecraft.create()

def Question():
    open("JEOPARDY_CSV.csv", "r")
