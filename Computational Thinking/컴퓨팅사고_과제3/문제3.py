
def month_counter(n):
    if n == 1: return 31
    elif n == 2: return 28
    elif n == 3: return 31
    elif n == 4: return 30
    elif n == 5: return 31
    elif n == 6: return 30
    elif n == 7: return 31
    elif n == 8: return 31
    elif n == 9: return 30
    elif n == 10: return 31
    elif n == 11: return 30
    else : return 31

def date_figure(year, month):
    during_year = year - 1921
    younyear = 0
    for k in range(1921, year):
        if k%4 ==0:
            younyear = younyear + 1
    date = during_year*365 + younyear
    if year % 4 == 0 and month > 2:
        date = date + 1
        for i in range(1,month):
            date = date + month_counter(i)
    else:
        for j in range(1,month):
            date = date + month_counter(j)
    return date

while True:
    raw = input("달력? ").split(' ')
    year = int(raw[0])
    month = int(raw[1])
    a = 0
    c = 0
    first_day_of_month = date_figure(year, month)
    firstday = first_day_of_month % 7
    if year % 4 == 0 and month == 2:
        monthcount =  29
    else:
        monthcount = month_counter(month)
    print("SUN MON TUE WED THU FRI SAT")
    a = a - firstday -6
    if a<=-7:
        a = a +7
    while True:
        for i in range(7):
            a = a + 1
            if a > monthcount:
                c = 1
                break
            if a > 0:
                print("%3d" % a,end = ' ')
            else:
                print("   ", end=' ')
        print('')
        if c == 1:
            break
