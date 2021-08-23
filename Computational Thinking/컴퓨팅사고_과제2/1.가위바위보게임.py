import random
rsp = ("가위","바위","보")
comwin = 0
manwin = 0
roundnum = 1
while True:
    print("컴퓨터 : ",comwin,"승",manwin,"패","당신 : ", manwin,"승",comwin,"패")
    print("(라운드",roundnum,")",sep='')
    roundnum = roundnum +1
    computer = random.choice(rsp)
    print("컴퓨터가 결정했습니다.")
    user = input("무엇을 내시겠습니까? (가위, 바위, 보) ")
    if (user == rsp[0] and computer == rsp[0]) or (user == rsp[1] and computer == rsp[1]) or (user == rsp[2] and computer == rsp[2]) :
        print("컴퓨터는 ",computer,"당신은",user,"비겼습니다.")
    elif (user == rsp[0] and computer == rsp[2]) or (user == rsp[1] and computer == rsp[0]) or (user == rsp[2] and computer == rsp[1]) :
        print("컴퓨터는 ",computer,"당신은",user,"당신이 이겼습니다.")
        manwin = manwin +1
    else:
        print("컴퓨터는 ",computer,"당신은",user,"컴퓨터가 이겼습니다.")
        comwin = comwin +1
    if comwin == 3:
        print("컴퓨터가 이겼습니다.")
        break
    if manwin == 3:
        print("당신이 이겼습니다.")
        break