from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()
# score = 0

GAP = block.AIR.id
WALL = block.COBBLESTONE.id
FLOOR = block.GRASS.id
# TREASURE = block.MOSS_STONE.id

x1 = pos.x + 1
y = pos.y
z1 = pos.z + 1

FILENAME = "maze.csv"
f = open(FILENAME, 'r')

z = z1
for line in f.readlines():
    data = line.split(",")
    x = x1
    for cell in data:
        a = FLOOR
        b = GAP
        
        mc.setBlock(x, y, z, b)
        mc.setBlock(x, y+1, z, b)
        mc.setBlock(x, y-1, z, a)
        x += 1
    z += 1

z2 = z
x2 = x

# mc.player.setPos(x, y)
