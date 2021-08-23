while True:
    f = open("dict_test.TXT",'r')
    w = 0
    search = input("단어? ")
    while 1:
        line = f.readline()
        if not line:
            if w == 1:
                w = 0
                break
            else:
                print("없는 단어입니다.")
                break
        fw = line.split(":")
        fwe = fw[0].rstrip()
        if search == fwe:
            print(line, end ='')
            w = 1