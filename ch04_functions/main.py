'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(methods)
    3) 사용자 정의 함수

2. 함수 용어 정의
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미

3. (사용자) 함수의 형식 :
def 함수_이름 (매개변수1, 매개변수2):
    실행문
    return 어쩌고

변수 = 함수_이름(argument1, argument2)
'''
from importlib.util import source_hash


# 함수 정의
def display_name(name):
    print(f'당신의 이름은 {name} 입니다.')

# 함수 호출
display_name('김일')

def display_name_age(name, age):
    print(f'당신의 이름은 {name} 이고, 나이는 {age}살 입니다.')

display_name_age('김이', 30)
display_name_age(age=23, name='김삼') #keyword argument

'''
우리가 예를 들어 input('이름을 입력하세요 >>> ')을 이용하여 이것을 name이라는 변수에 담았다고 가정한면,
name = input('이름을 입력하세요>>> ')이라고 작성함

그러면 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있음. 파이썬 내장 함수는 이미 정의가 되어있거,
개발자들은 함수 호출만 잘하면 됨

사용자 정의 함수의 경우 새발자 자신이 함수를 정의하고, 그 후에 호출까지 하는 것까지가 과정임

내장함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods): 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는
함수. 사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 톨해서만 호출 가능
'''

# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하시오>> ')

'''
이상의 코드는 함수 호출을 해서 그 결과 값을 eng_name이라는 변수에 담았다
'''

# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
그렇다면 eng_name.upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는 str자료
형에 종속되어있다고 볼 수 있습니다.
그리고 결과 값을 '다시' eng_name' 이라는 변수에 담았기 때문에
55번 라인의 결과값과 57번라인 결과값이 차이가 남

함수(메서드)의 유형
'''
#매개 변수 x / 리턴 x
def call1():
    print('[x | x]')

#매개 변스 o / 리턴 x
def call2(unknown_parameter):
    print('[o | x]')
    print(f'{unknown_parameter}라고 입력했음')

#매개 변수 x | 리턴 o
def call3():
    print('[x | o]')
    return 1

def call4(unknown1, unknown2):
    print('[o | o]')
    return unknown1 + unknown2

#함수 호출
call1()
call2('오늘 날씨 별로')
call2(1234)
call3()         # 결과값 : [x | o]만 나옴
print(call3())
#결과값
'''
[x | o]
1
'''
print(call4('안녕', '하세요'))
# print(call4(unknown2=1234, unknown1='56478'))

# def vending_machine(money):
#     count = 0
#
#     while(money > 0) :
#         print(f'음료수 = {count}개, 잔돈 = {money}원')
#         count += 1
#         money -= 700
#
# vending_machine(3000)
# //==============
# def vending_machine():
#     money = int(input("투입 금액을 입력하세요: "))
#     count = 0
#
#     while money >= 700:
#         print(f'음료수 = {count}개, 잔돈 = {money}원')
#         count += 1
#         money -= 700
#
#     print(f'음료수 = {count}개, 잔돈 = {money}원')

# vending_machine()

# 풀이!!!
#
# print(5 // 2) # 결과 값: 2
# print(5 % 2)  # 결과 값 : 1
#
# 일단 메인에서 굴려보고 함수 작성
my_money = 3000
drink_price = 700

# # 1 for문으로 작성
# change = my_money - (drink_price * 음료개수)
# my_money를 기준으로 음료수 살 수 있는 경우의 수를 고려했을때 0~4까지 반복문이 5번 돌아산다
# for i in range(my_money // drink_price + 1):
#     print(f'음료 개수 = {i}개, 잔돈 = {my_money - (drink_price*i)}')
#
# # # 2 while 문으로 작성
# num = 0
# while my_money >= 0:
#     print(f'음료수 개수 = {num}개, 잔돈 = {my_money-(drink_price*num)}')
#     num += 1

# for문 기준 함수화
def vending_machine(my_money):
    drink_price=700
    for i in range(my_money // drink_price + 1):
        print(f'음료수 개수 = {i}개, 잔돈 = {my_money - (drink_price * i)}')

vending_machine(3000)

'''
함수 정의 : 
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수호출:
multiply(dan)       

실행 예
몇 단을 출력하시겠습니까>>>3
3 x 1 = 3
...

3 x 9 = 27
'''
#
# def multiply(n) :
#     for i in range(1, n+1):
#         for j in range(1, 10):
#             print(f'{i} x {j} = {i * j}')
#
# dan = int(input('몇 단을 출력하시겠습니까>>>'))
#
# multiply(dan)

'''
range() 함수의 parameter 적용 순서
1 개만 있을 때 : 한계값
2 개만 있을 때 : 시작값, 한계값
3 개만 있을 때 : 시작값, 한계값, 증감값 순서입니다.

그럼 현재 multiply를 call2() 유형으로 정의 했다고 볼 수 있습니다

multiply2()를 call1() 유형으로 정의 했을 때

실행 예 
몇 단을 출력 하시겠습니까? >> 5

'''
def multiply2() :
    dan = int(input('몇 단을 출력하시겠습니까>>>'))

    for j in range(1, 10):
        print(f'{dan} x {j} = {dan * j}')

multiply2()

