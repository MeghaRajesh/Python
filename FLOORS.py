import math
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    if(x!=y):
        floorX=math.ceil(x/10)
        floorY=math.ceil(y/10)
        if(floorX>floorY):
            print(floorX-floorY)
        else:
            print(floorY-floorX)
