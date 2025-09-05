# '''
#
# 아까 전에는 일종의 setter를 활용하여 속성에 속성값을 넣어줬습니다.
# 그럼 Java에서 수업한 것 처럼 속성값이 대입되지 않은 객체를 생성한 다음에 속성값을 집어 넣어주는 과정을 거침
#
# 근데 매개변수 생성자를 정의해버리면 객체 생성시에 속성값을 넣을 수 있겠네요
# '''
# # 클래스 정의
# class Candy:
#     def set_info(self shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은{self.shape}이고, 색깔은{self.color}입니다.')
#
# # 객체 생성 (빈 객체 -> 속성값 대입 -> 속성값 출력
# satang = Candy()
# satang.set_info('구형')
#
# class Candy2():
#     def __init__ (self, shape, color):
#         self.shape = shape
#         self.color = color
#     def show_info(self):
#         print(f'사탕의 모양은{self.shape}이고, 색깔은{self.color}입니다.')
#
# # 객체 생성 방식에서의 차이가 있습니다.
# satang2 = Candy2('정육면체', '흰색')
# satang2.show_info()
#
# class Sample:
#     #생성자 정의
#     def __init__(self):
#         print('인스턴스가 생성되었습니다')
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# # 객체 생성
# sample = Sample()
# print()
# # 객체 소멸자 호출 방법
# del sample      # del 객체명
# print('객체 지운 후의 코드라인 입니다.')
#
# '''
# 굳이 소멸자를 학습하는 이유는 -> 객체가 생성되면 메모리 공간을 차지해서, 객체가 호출될 대마다 그곳에
# 서 불러 나오게 됩니다.
#
# 하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에
# 소멸자를 통해서 갈제로 객체를 삭제해주면 메모리 관리가 편하겠네요
# '''
#
# class USB :
#     def __init__(self, capacity):
#         self.capacity = capacity
#         print('usb 객체가 생성되었습니다.')
#
#     def get_info(self):
#         print(f'{self.capacity}GB USB')
#
# usb = USB(64)
# usb.get_info()

'''
'''
from ch07_classes.main import Person


# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} is born')
#
#     def __del__(self):
#         print(f'{self.name} is dead')
#
# man = Person('james')
# woman = Person('emaily')
# del man

class Student:
    # getter 예시
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score


    # setter 예시
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_score(self, score):
        self.score = score



student1 = Student()
student1.set_name('김일')
student1.set_age(20)
student1.set_score(4.5)
print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()}살이고 과목 점수는 {student1.get_score()}')

'''
지시 사항 age / address / score 속성을 setter를 통해서 추가하시오
이상의 속성에 맞는 getter도 추가하시오

student1 객체를 생성하고ㅡ
김일, 20, 4.5를 각각 이름/ 나이 / 점수에 대입하시오

getter만을 활용하여
김일 학생의 나이는 20살로, 파이썬 과목의 점수는 4.5점 입니다.
'''


