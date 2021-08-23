# 202103378 진윤겸
import numpy as np

case = np.random.normal(50, 15, 100)
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in case:
    if i >=90:
        counter[9] += 1
    elif i < 90 and i >= 80:
        counter[8] += 1
    elif i < 80 and i >= 70:
        counter[7] += 1
    elif i < 70 and i >= 60:
        counter[6] += 1
    elif i < 60 and i >= 50:
        counter[5] += 1
    elif i < 50 and i >= 40:
        counter[4] += 1
    elif i < 40 and i >= 30:
        counter[3] += 1
    elif i < 30 and i >= 20:
        counter[2] += 1
    elif i < 20 and i >= 10:
        counter[1] += 1
    else:
        counter[0] += 1

for i in range(10):
    print(0 + 10*i, "~", 10 + 10*i, ":", end=' ')
    for j in range(counter[i]):
        print("*", end='')
    print()