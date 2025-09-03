'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실해문이 반복됨(조건문이
    false가 될때까지
형식 :
while 조건식1:
    반복실행문

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해야함

'''
from itertools import count

# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1     # python에는 ++ 이 없습
#
# '''
# 기본 예제
# 10부터 1까지 역순으로 출력하시오
# '''
# n2 = 10
# while n2 > 0:
#     print(n2)
#     n2 -= 1
'''
중첩 while문 (while문 뿐 아니라 내부에 if문을 쓸 수도 있음)
중첩 while 및 f-string을 활용하여
'''

dan = 1

while dan < 10:
    number = 1
    while number < 10:
        print(f'{dan} x {number} = {dan * number}')
        number += 1
    dan += 1

print(number) # 추후 설명 예정
