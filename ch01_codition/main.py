'''
1. if 문
    if 문은 조건이 참일때만 해당 블록의 코드 실행
2. if-else 문
    if는 조건이 참일 때 실행 / false 일 때는 else 부분 실행
3. if-elif -else 문
'''

# age = 21
# if age > 20:
#     print('성인 입니다.')
# elif age <=20 and age > 13:
#     print('청소 입니다.')
# else :
#     print('미자 입니다.')

'''
if 조건문의 전체 형식 :
if 조건식1 :
    실행문1
(elif 조건식2 :)
    (실행문2)
(elif 조건식3 :)
    (실행문3)
(else:)
    (실행문4)
()는 optional입니다.
'''
# age1 = input('나이를 입력하세요>>> ')
# print(age1)
# print(age1+'10')
# print(type(age1))      # 결과값 : <class 'str'>
# age2 = int(age1)
# print(age2 + 10)
'''
input() 함수의 return 자료형은 string 이다
-> 수학적인 연산을 위해서는 형변환 함수인 int() / float()을 사용
'''

# age = int(input('당신의 나이를 입력하세요'))
# input() 의 결과값이 자료형 str이고 다시 int로 바꾸는 함수가 적용되어 일종의 chaining method  처럼 사용가능
# print(f'당신의 나이는 {age} 살이고, 내년에는 {age+1}살이 됩니다.')
#
# if age > 19:
#     print('성인 입니다.')
# elif age <= 19 and age > 14:
#     print('청소 입니다.')
# elif age <= 14 and age > 5:
#     print('어린이 입니다')
# else:
#     print('응애 입니다.')

'''
중첩 if문(Nest-if문)
    조건문 내부에 다른 조건문을 사용
'''
age = 18
has_ticket = False #boolean 자료형일 때 python만 또 지혼자 대문자 시작
print(type(has_ticket)) # 결과값 : <class 'boo'>
if age >= 19:
    # 중첩 if문 적용
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요')
else :
    print('미자 입구컷')

age = float(age)            # 정수를 실수로 형변환
print(age)  #결과값 : 21.0

'''
논리 연산자 :
    1) and : A and B -> A와 B가 모두 참일때 실행                 &&
    2) or : A or B -> A 혹은 B 중에 하나가 참이면 실행문 실행      ||
    3) not : if not A -> A가 false일 때 실행문 실행              !
leap_year 패키지 -> main
'''

