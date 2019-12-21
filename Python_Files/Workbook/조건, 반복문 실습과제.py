# 1. -999가 입력될 때까지 정수를 입력 받은 후 양수/음수의 개수와 양수일 때 짝수/홀수의 개수를 출력하는 프로그램
positive_cnt, negative_cnt, even_cnt, odd_cnt = 0, 0, 0, 0
while True:
    num1 = int(input('정수를 입력하세요 : '))
    if num1 == -999:
        break
    elif num1 > 0:
        positive_cnt += 1
        if num1 % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    else:
        negative_cnt += 1
print("{0}{1} {2}{3} {4}{5} {6}{7}".format('양수 개수 : ', positive_cnt, '음수 개수 : ', negative_cnt, '짝수 개수 : ', even_cnt, '홀수 개수 : ', odd_cnt))