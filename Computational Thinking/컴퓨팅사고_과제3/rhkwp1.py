import time
import random
all_score = []
while True:
    for i in range(10):
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        score = 0
        print(i+1,") ",a ," * ",b ," = ", sep='', end='')
        answer = a * b
        take = time.time()
        useranswer = int(input())
        end = time.time()
        howlong = int((end - take) * 1000)
        if useranswer == answer and howlong <= 3000 :
            score = score + 3000 - int(howlong)
            print("(맞았습니다.) ", howlong/1000,"초 소요 ", "score = ", score,sep = '')
        elif useranswer == answer and howlong > 3000:
            print("(제한시간이 지났습니다.) ", howlong/1000,"초 소요", "score = ", score,sep = '')
        else :
            print("(틀렸습니다.) ", howlong/1000,"초 소요", "score = ", score,sep = '')
    all_score.append(score)
    all_score.sort(reverse=True)
    print("최고점수 : ", all_score[0],sep='')
    input("진행하려면 엔터를 누르시오.")