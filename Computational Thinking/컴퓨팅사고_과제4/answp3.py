location = []
year = [2016, 2017, 2018, 2019, 2020]
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
w = 0
f = open("Weather.csv")
while True:
    v = f.readline()
    if v == '':
        break
    v = v[:-1]
    s = v.split(',')
    if s[1] in location:
        location.pop(0)
        break
    else:
        location.append(s[1])

print("도시를 선택하세요 (", end='')
for i in location:
    w = w + 1
    print(w, ":", i, sep='', end=', ')
choose = int(input(")"))
chooselocation = location[choose-1]
print(chooselocation, "기후분석   평균기온   월별 강수량(mm)")

for i in year:
    for j in month:
        f.close()
        f = open("Weather.csv", 'r')
        tsum = 0
        water = 0
        count = 0
        while True:
            k = f.readline()
            if k == '':
                break
            k = k[:-1]
            zlist = k.split(',')
            zdate = zlist[2].split('-')
            try:
                zmonth = int(zdate[1])
                zyear = int(zdate[0])
                if zyear == i and zmonth == j and chooselocation == zlist[1]:
                    count = count + 1
                    tsum = tsum + float(zlist[3])
                    water = water + float(zlist[6])
            except:
                continue
        try:
            print("%d년 %2d월 %9.2f %10.2f" % (i, j, tsum/count, water))
        except:
            continue