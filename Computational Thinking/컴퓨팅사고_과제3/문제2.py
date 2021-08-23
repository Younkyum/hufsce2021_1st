import random

def lotto_generator( ):
    num = []
    while len(num) < 6 :
        a = random.randrange(1, 45)
        if a in num:
            continue
        else:
            num.append(a)
    return num


a = int(input("몇 번째 로또 번호를 고를까요?"))
for i in range(a):
    selectednum = lotto_generator()
    print(i+1, "회 : ", selectednum)
# 앞쪽 로또 번호는 버리고 마지막 로또 번호만 남는다.
print("이번주의 로또 번호입니다." , end ='')
for i in selectednum:
    print(i, end =' ')
print()
print("이 번호가 맞으면 교수님과 50:50")