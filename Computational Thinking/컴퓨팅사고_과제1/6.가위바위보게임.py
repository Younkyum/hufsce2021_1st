import random

comwin = 0
manwin = 0
roundnum = 1
while True:
    print("컴퓨터 : ",comwin,"승",manwin,"패","당신 : ", manwin,"승",comwin,"패")
    print("(라운드",roundnum,")",sep='')
    print("컴퓨터가 결정했습니다.")
    manum = input("무엇을 내시겠습니까? (가위, 바위, 보) ")
    if manum == "가위":
        if random.choice(["가위", "바위", "보"]) == "바위":
            print("컴퓨터는 바위, 당신은 가위. 컴퓨터가 이겼습니다.")
            comwin = comwin+1
        elif random.choice(["가위", "바위", "보"]) == "가위":
            print("컴퓨터는 가위, 당신은 가위. 비겼습니다.")
        else:
            print("컴퓨터는 보, 당신은 가위. 당신이 이겼습니다.")
            manwin = manwin +1
    if manum == "바위":
        if random.choice(["가위", "바위", "보"]) == "보":
            print("컴퓨터는 보, 당신은 바위. 컴퓨터가 이겼습니다.")
            comwin = comwin+1
        elif random.choice(["가위", "바위", "보"]) == "바위":
            print("컴퓨터는 바위, 당신은 바위. 비겼습니다.")
        else:
            print("컴퓨터는 가위, 당신은 바위. 당신이 이겼습니다.")
            manwin = manwin +1
    if manum == "보":
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("컴퓨터는 가위, 당신은 보. 컴퓨터가 이겼습니다.")
            comwin = comwin+1
        elif random.choice(["가위", "바위", "보"]) == "보":
            print("컴퓨터는 보, 당신은 보. 비겼습니다.")
        else:
            print("컴퓨터는 바위, 당신은 보. 당신이 이겼습니다.")
            manwin = manwin +1
    if comwin == 3:
        print("게임이 종료되었습니다. 컴퓨터가 승리했습니다.")
        break
    if manwin == 3:
        print("게임이 종료되었습니다. 당신이 승리했습니다.")
        break
    roundnum = roundnum+1