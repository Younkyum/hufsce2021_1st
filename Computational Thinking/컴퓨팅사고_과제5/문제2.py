class Calc:
    def __init__(self, value = 0):
        self.result = value
    def add(self, value):
        self.result = self.result + value
    def minus(self, value):
        self.result = self.result - value
    def print(self):
        print(self.result)
    def setvalue(self, value):
        self.result = value
    def getvalue(self):
        return self.result

cal1 = Calc() # 객체 생성
cal2 = Calc(5) # 5 를 초기화하여 객체 생성
cal1.setvalue(10) # 10 설정
cal1.add(20) # 20 더하기
cal1.minus(5) # 5 빼기
cal1.print() # 값 표시하기
cal2.add(cal1.getvalue()) # cal1의 값을 cal2에 더하기
cal2.print() # 값 표시하기