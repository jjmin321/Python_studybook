#키와 몸무게를 입력받아 비만도를 구하고 결과를 출력하세요
# 표준체중(kg) = (신장(cm)-100) x 0.85
# 비만도(%) = 현재체중/표준체중(%) x 100

# 비만도가 90%이하 --> 저체중
# 비만도가 90%초과 ~ 110% --> 정상
# 비만도가 110%초과 ~ 120% --> 과체중
# 비만도가 120%초과 --> 비만

height = int(input('키를 입력하세요 : '))
weight = int(input('몸무게를 입력하세요 : '))
def obesity(height, weight):
    standard_weight = int((height - 100) * 0.85)
    obesity = float(weight / standard_weight * 100)
    if obesity <= 90:
        print("당신의 키와 몸무게는 {0}, {1}이며 표준 체중은 {2}, 비만도는 {3}입니다 <{4}>".format(height, weight, standard_weight, obesity, "저체중!!!"))
    elif obesity > 90 and obesity <= 110:
        print("당신의 키와 몸무게는 {0}, {1}이며 표준 체중은 {2}, 비만도는 {3}입니다 <{4}>".format(height, weight, standard_weight, obesity, "정상"))
    elif obesity > 110 and obesity <= 120:
        print("당신의 키와 몸무게는 {0}, {1}이며 표준 체중은 {2}, 비만도는 {3}입니다 <{4}>".format(height, weight, standard_weight, obesity, "과체중!"))
    elif obesity > 120:
        print("당신의 키와 몸무게는 {0}, {1}이며 표준 체중은 {2}, 비만도는 {3}입니다 <{4}>".format(height, weight, standard_weight, obesity, "비만 운동좀해!!!"))
    else :
        print("오류입니다. 다시 입력해주세요")
obesity(height, weight)

