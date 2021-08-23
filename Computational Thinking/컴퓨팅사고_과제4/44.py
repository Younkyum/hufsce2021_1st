f = open("Weather.csv")
while True:
    v = f.readline()
    if v == '': break
    v = v[:-1]
    s = v.split(',')
    print(s)
f.close()