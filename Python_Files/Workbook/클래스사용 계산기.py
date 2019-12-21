# 1. 사칙연산 프로그램 구현( 클래스 작성)
# 사용자 선택 입력값 --> ( 1:'+', 2:'-', 3:'*', 4:'/', 0:end )
# 두개의 수를 입력
class Calculator:
    def __init__(self):
        self.instance = {
            0 : 'end',
            1 : '+',
            2 : '-',
            3 : '*',
            4 : '/',
        }
    def calculate(self, num1, num2, operator):
        return eval(num1+self.instance[operator]+num2)

class ControlCalculator:
    def __init__(self):
        self.c = Calculator()
    def calculate(self, num1, num2, operator):
        return self.c.calculate(num1, num2, operator)

class ViewCalculator:
    def __init__(self):
        self.v = ControlCalculator()
        self.num1 = 0
        self.num2 = 0
        self.operator = 0
    def DisplayCalculator(self):
        while True:
            self.num1 = input('첫 번째 정수 입력 : ')
            self.num2 = input('두 번째 정수 입력 : ')
            self.operator = int(input('연산자 입력 : '))
            if self.operator == 0:
                break
            print(self.v.calculate(self.num1,self.num2,self.operator))

if __name__ == '__main__':
    viewCalculator = ViewCalculator()
    viewCalculator.DisplayCalculator()
