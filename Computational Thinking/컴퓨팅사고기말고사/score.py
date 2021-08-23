def total(student):
    return student[1] + student[2] + student[3]

def ave(student):
    return student[4]/3

def grade(student):
    if student[5] >= 90:
        return 'A'
    elif student[5] < 90 and student[5] >= 80:
        return 'B'
    elif student[5] < 80 and student[5] >= 70:
        return 'C'
    elif student[5] < 70 and student[5] >= 60:
        return 'D'
    else:
        return 'F'

def output(student):
    print(student[0], end=': ')
    print("국어:", student[1], end=' ')
    print("수학:", student[2], end=' ')
    print("영어:", student[3], end=' ')
    print("총점:", student[4], end=' ')
    print("평균:", int(student[5]*100)/100, end=' ')
    print("학점:", student[6])


def max_student(*students):
    max_index = 0
    i = 0
    for student in students:
        if student[4] >= students[max_index][4]:
            max_index = i
        i = i + 1
    return students[max_index]