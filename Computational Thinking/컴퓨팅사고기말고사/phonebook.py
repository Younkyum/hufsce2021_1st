# 202103378 진윤겸
class Phone:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def printPerson(self):
        print(self.name, self.num)


class PhoneBook:
    def __init__(self):
        self.book = []

    def addPerson(self, a):
        self.book.append(a)

    def getBookCount(self):
        return len(self.book)

    def getBook(self, num):
        return self.book[num]
