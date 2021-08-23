location = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
total =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yesterday = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
today = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
change = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    today_1 = input().split(" ")
    if len(today_1) == 17:
        today = today_1
        print("지역   서울 부산 대구  인천 광주 대전 울산  세종 경기 강원 충북  충남 전북  전남 경북 경남 제주",end='')
        print()
        for i in range(len(today_1)):
            today[i] = int(today[i])
        for i in range(len(location)):
            change[i] = int(today[i]) - int(yesterday[i])
        print("어제 ",end ='' )
        for i in yesterday:
            print("%4s" % i,end =' ')
        print()
        yesterday = today
        print("오늘 ",end = '')
        for i in today_1:
            if i == max(today_1):
                print("(%3s)" % i, end=' ')
            else:
                print("%4s" % i,end=' ')
        print()
        for i in range(len(change)):
            if change[i] > 0:
                change[i] = "+" + str(change[i])
        print("변동 ",end='')
        for i in change:
            print("%4s" % i,end=' ')
        print()
        print("누계 " ,end = '')
        for i in range(len(total)):
            total[i] = total[i] + int(today[i])
        for i in total:
            if i == max(total):
                print("(%3s)" % i, end=' ')
            else:
                print("%4s" % i, end=' ')
        print()
    else:
        print("개수(17개)가 부족한 입력 : 총 %d개의 값이 입력되었습니다." % len(today_1))
        continue