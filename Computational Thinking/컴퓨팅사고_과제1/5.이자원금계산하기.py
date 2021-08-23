pri = int(input("원금을 입력하세요(원). "))
rest = int(input("금리를 입력하세요(%). "))
print("원금 ",pri,"원  ","금리 ",rest,"% 입니다.",sep='')
print("기간      합계")
for i in range(1,21):
    print(i,"년   ",sep='',end='')
    pri = pri*rest/100+pri
    print(int(pri*10)/10)