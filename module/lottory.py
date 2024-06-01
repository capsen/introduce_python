import random

def picknumbers(poolsize, ballnum):
    balls=list(range(1,poolsize+1))
    result=[]
    for i in range(ballnum):
        random.shuffle(balls)
        result.append(balls.pop())
    return result

def generatePowerball():
    print(picknumbers(35,7), picknumbers(20,1))