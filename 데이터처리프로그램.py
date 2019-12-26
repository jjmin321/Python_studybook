import matplotlib.pyplot as plt
from openpyxl import load_workbook
import sys

class Grade:
    def __init__(self):
        print("프로그램 시작")
        self.subject = []   #과목명
        self.data = []  #성적
        self.vs_data = [] #꺾은선그래프 비교대상의 성적
        self.person = 'opponent' #꺾은선그래프 비교대상의 이름
        self.width = 0.5 #막대차트 차트넓이
        self.color = 'black' #막대차트 차트색깔
        self.whoiswinner = 'You Win!' #꺾은선그래프 나와 비교대상의 성적 비교
    def my_grade(self):
        plt.title('Bar_chart')
        plt.xlabel('Score')
        plt.ylabel('Subject')
        plt.legend('My score')
        plt.bar(self.subject, self.data, width=self.width, color=self.color)
        plt.show()
    def vs_grade(self):
        plt.title(self.whoiswinner)
        plt.plot(self.subject, self.data)
        plt.xlabel('Score')
        plt.ylabel('Subject')
        plt.plot(self.subject, self.vs_data)
        plt.legend(['My score', self.person])
        plt.show()
    def set_subject(self):
        while True:
            for k in range(0, 10):
                a = input('과목을 입력해주세요(모두 입력했다면 end를 입력해주세요) : ')
                if a == 'end':
                    break
                # self.subject[k] = a
                self.subject.insert(k, a)
            break
    def set_data(self):
        for k in range(0, len(self.subject)):
            # print(self.subject)
            # print(self.data)
            a = float(input('성적을 입력해주세요(입력하신 과목 수만큼 입력할 수 있습니다) : '))
            self.data.insert(k, a)
    def set_vs_data(self):
        for k in range(0, len(self.subject)):
            a = float(input('비교할 사람의 성적을 입력해주세요(입력하신 과목 수만큼 입력할 수 있습니다) : '))
            self.vs_data.insert(k, a)
    def set_person(self):
        a = input('비교할 사람의 이름을 입력해주세요 : ')
        self.person = a
    def set_width(self):
        while True:
            a = float(input('막대 그래프의 넓이를 설정해주세요(0.1 ~ 0.9 사이로 입력해주세요) : '))
            if a < 0.1 or a > 0.9:
                pass
            else:
                self.width = a
                break
    def set_color(self):
        a = input('막대그래프에 색깔을 입혀주세요! : ')
        self.color = a
    def start(self):
        a = int(input('그래프 종류를 선택해주세요 : [1] 내 성적 막대 차트 , [2] 성적 비교 꺾은선 그래프 [3] 엑셀 예시 파일 읽어오기 : '))
        if a == 1:
            Grade.bar_chart(self)
        elif a == 2:
            Grade.line_graph(self)
        elif a == 3:
            Grade.read_xlsx(self)
        else:
            print('1번 2번 3번 중에 선택해주세요')
            sys.exit()
    def sort(self):
        while True:
            a = int(input('정렬 종류를 선택해주세요 : [1] 오름차순 , [2] 내림차 : [3] 입력 데이터 유지 : '))
            if a == 1:
                self.data.sort()
                break
            elif a == 2:
                self.data.sort(reverse=True)
                break
            elif a == 3:
                break
            else:
                print("다시 입력해주세요")
    def bar_average(self):
        self.subject.append('Average')
        self.data.append(sum(self.data) / len(self.data))
    def line_average(self):
        self.subject.append('Average')
        self.data.append(sum(self.data) / len(self.data))
        self.vs_data.append(sum(self.vs_data) / len(self.vs_data))
        if sum(self.vs_data) > sum(self.data):
            self.whoiswinner = self.person+" Win!"
        elif sum(self.vs_data) == sum(self.data):
            self.whoiswinner = "Draw!"
        else:
            pass
    def bar_chart(self):
        Grade.set_subject(self)
        Grade.set_data(self)
        Grade.set_width(self)
        Grade.set_color(self)
        Grade.bar_average(self)
        Grade.sort(self)
        Grade.my_grade(self)
    def line_graph(self):
        Grade.set_subject(self)
        Grade.set_data(self)
        Grade.set_vs_data(self)
        Grade.set_person(self)
        Grade.line_average(self)
        Grade.vs_grade(self)
    def read_xlsx(self):
        load_wb = load_workbook("/Users/jejeongmin/pycharmprojects/python_lab/data_example.xlsx", data_only=True)
        load_ws = load_wb['Sheet1']
        all_values = []
        for row in load_ws.rows: #모든 행을 순회하는 코드
            row_value = []
            for cell in row: #각 행을 순회하는 코드
                row_value.append(cell.value)
            all_values.append(row_value)
        self.subject = all_values[0][1:]
        self.data = all_values[1][1:]
        self.vs_data = all_values[2][1:]
        self.person = all_values[2][0]
        self.subject.append('Average')
        self.data.append(sum(self.data)/len(self.data))
        self.vs_data.append(sum(self.vs_data)/len(self.vs_data))
        Grade.vs_grade(self)
grade = Grade()
grade.start()


