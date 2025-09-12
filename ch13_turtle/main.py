from random import Random
from turtle import Turtle, Screen
# turtle 모듈에서 Turtle, Screen 클래스를 import해왔습니다.

t = Turtle()        # 터틀 객체를 생성했고, 객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것입니다.

t.shape('turtle')           # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')
screen.bgcolor('black')

# 이상을 일반화 시키기 위해서 알 수 있는 것은
'''
삼각형일 때 120
사각형일 때 90
오각형일 때 72
육각형일 때 60

십각형일 때 36
'''

random = Random()
colors=[
    'dark red',
]
# n = int(input('몇각형을 만드시겠습니까? >>> '))
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)


for i in range(3, 11):
    for _ in range(i):
        t.forward(100)
        t.left(360 / i)




screen.exitonclick()