# [클래스 실습과제]
# 1. Car class를 만들고 다음 멤버와 메서드를 구현하고
# 호출하는 코드를 구현해보세요
# 클래스의 인스턴스 객체 sonata 를 만든다
# 클래스의 모든 메서드를 호출해서 동작을 확인해본다

class Car:
    def __init__(self) :
        print("생성자 호출")
        self.car_name = "소나타"
        self.car_drv = "전륜"
        self.car_speed = 0
        self.car_direction = "앞쪽"
        self.car_fuel = "휘발유"
        self.car_state = "정상"
    def set_car_name(self, name):
        print("차종이 [{0}]로 변경되었습니다.".format(name))
        self.car_name = name
    def get_car_name(self):
        return self.car_name
    def set_car_drv(self, drv):
        print("차의 구동 방식 [{0}]로 변경되었습니다.".format(drv))
        self.car_drv = drv
    def get_car_drv(self):
        return self.car_drv
    def set_car_fuel(self, fuel):
        print("차의 연료 방식이 [{0}]로 변경되었습니다.".format(fuel))
        self.car_fuel = fuel
    def get_car_fuel(self):
        return self.car_fuel
    def set_car_state(self, state):
        print("차의 상태 [{0}]으로 변경되었습니다.".format(state))
        self.car_state = state
    def get_car_state(self):
        return self.car_state
    def set_speed(self, speed):
        print("자동차의 속력이 시속 [{0}]km로 변경되었습니다.".format(speed))
        self.car_speed = speed
    def get_speed(self):
        return self.car_speed
    def turn(self, turn):
        print("자동차 방향 [{0}]로 변경되었습니다.".format(turn))
        self.car_direction = turn
    def stop(self):
        self.car_direction = "정지"
    def start(self):
        print("자동차가 시동이 걸렸습니다")
    def move_forward(self):
        self.car_speed = 100
        self.car_direction = "앞쪽"
        print("자동차가 [전진]합니다. 속도는 [{0}]km입니다".format(self.car_speed))
    def move_backward(self):
        self.car_speed = 100
        self.car_direction = "뒤쪽"
        print("자동차가 [후진]합니다. 속도는 [{0}]km입니다".format(self.car_speed))
    def __del__(self):
        print("{0} 자동차가 제거되었습니다".format(self.car_name))

sonata = Car()
sonata.set_car_name('산타페')
sonata.get_car_name()
sonata.set_car_drv('4륜')
sonata.get_car_drv()
sonata.set_car_fuel('전기')
sonata.get_car_fuel()
sonata.set_car_state('브레이크고장')
sonata.get_car_state()
sonata.set_speed(100)
sonata.get_speed()
sonata.turn('오른쪽')
sonata.stop()
sonata.start()
sonata.move_forward()
sonata.move_backward()
sonata.__del__()