import math
for i in range(28):
    th = math.radians(15*i)
    a = int(math.sin(th)* 10 + 10)
    for j in range(a+1):
        if a == j:
            print("*")
        else :
            print(" ",end='')
