# calculator.py
# Python_Files/Studybook/call_calculator에서 사용할 모듈
# 모듈은 항상 PycharmProjects/.../module 이렇게 배치해야 한다.
# 단축키
# Command + '/' : 주석문 설정/해제
# Tab : 들여쓰기
# Shift + Tab : 들여쓰기 해제

# Ctrl + Option + R : 최초 작성 코드의 실행
# Ctrl + R : 마지막에 실행했던 코드를 다시 실행
# Ctrl + Shift + R : 지금 코드를 실행

def add(a,b):
    c = a + b
    return c

def subtract(a,b):
    c = a-b
    return c

def multiply(a,b):
    c = a * b
    return c

def divide(a,b):
    c = a/b
    return c

# Python에는 main문이 없기 때문에 설정을 해줘야 된다!(와우!)
# 만약 main문이라면(남이 사용할 모듈이 아닌 메인 모듈이라면) print를 다 실행함! 남이 사용할 모듈이라면 실행 안 함!
# 최상위 모듈일 경우 main, 다른 곳에서 사용할 모듈일 경우 calculator모듈이라고 불린다.
if __name__ == '__main__':
    print(add(10,20))
    print(subtract(30,10))
    print(multiply(3,5))
    print(divide(30,3))
