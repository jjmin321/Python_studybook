#  연산자 기호를 사전(dict)에 넣어 두고 두 개의 정수를 입력 받아서 사칙 연산하는 계산기 프로그램
# (계산방식은 1이면 '+', 2이면 '-', 3이면 '*', 4이면 '/', eval()함수를 사용)

a = {
    1 : '+',
    2 : '-',
    3 : '*',
    4 : '/'
}

num1 = input('첫 번째 정수를 입력하세요 : ')
num2 = input('두 번째 정수를 입력하세요 : ')
operator = int(input('연산자를 숫자로 입력하세요 : '))
print(eval(num1 + a[operator] + num2))