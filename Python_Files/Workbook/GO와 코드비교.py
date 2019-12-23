# GO 원넓이구하기 코드

# package main
#
# import "fmt"
#
# const (
# 	circumference = 3.14
# )
#
# type circle struct {
# 	radius float64
# }
#
# func (c circle) calculate() {
# 	fmt.Printf("반지름(Radius) : %0.3f 넓이(Weight) : %0.3f", c.radius, c.radius*c.radius*circumference)
# }
#
# func main() {
# 	a := circle{1.5}
#   a.calculate()
# }

# Python 원넓이구하기 코드

circumference = 3.14

class Calculate:
    def circle(self, value):
        self.value = value
    def calculate(self):
        print("반지름(Radius) : {} 넓이(Weight) : {}".format(self.value, self.value*self.value*circumference))

a = Calculate()
a.circle(1.5)
a.calculate()

# GO 삼각형 넓이 계산하는 코드(밑변과 높이 변경할 메소드 포함)

# package main
#
# import "fmt"
#
# type Wide struct {
# 	bottom, height float32
# }
#
# func main() {
# 	a := Wide{3, 4}
# 	a.change()
# 	fmt.Print(a.triangle())
# }
#
# func (a Wide) triangle() float32 {
# 	return a.bottom * a.height / 2
# }
#
# func (a *Wide) change() { //(a *Wide)는 pointer receiver로 구조체의 값을 변경할 수 있음 (pointer로 접근했을 때만 구조체의 값 변경 가능)
# 	a.bottom = 12
# 	a.height = 12
# }

# Python 삼각형 넓이 계산하는 코드(밑변과 높이 변경할 메소드 포함)

class Triangle:
    def __init__(self):
        self.bottom = 3
        self.height = 4
    def triangle(self):
        return self.bottom * self.height / 2
    def change(self, bottom, height):
        self.bottom = bottom
        self.height = height

a = Triangle()
a.change(12, 12)
print(a.triangle())