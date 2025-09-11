'''
ch11_exception
main

1. 예외 처리의 필요성
    1) 예외(exception) : 개발자가 직접처리할 수 있는 문제
    2) 오류(error) : 개발자가 처리할 수 없는 문제

    3) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해주는것이 아니라, 발생된 문제로
        인해 프로그램이 비정상적으로 종료되는 것을 막고, 사용자에게 발생한 문제에 대해
        정보를 전달하기 위함.

2. 예외 처리
    1) 고전적 예외 처리
'''
from logging import exception

from prettytable import PrettyTable
#
# a = int(input('나누는 수(제수)를 입력하세요 >>> '))
# b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
# if a == 0:
#     print('0으로 나눌 수 없습니다.')
# else:
#     result = b / a
'''
근데 우리는 어제 사용해봤었습니다. coffee_machine에서
if drink == None:
    이라는 방식으로 사용함
    
어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0 을 통해 0으로 나눈것을 아예 시도 할 수 없도록 예외처리릉 함

여기서도 생각할 문제는 :
        1) 어떤 문제가 발생할지 예상할 수 있어야 미리 대비할 수 있다.
        2) 어떤 문제가 발생할지 예상할 수 있더라도 대비할 수 없는 경우가 있다.

3. 예외 처리의 종류

1. BaseException 최상위 예외 클래스
2, Exception 
3. ArithmeticError
4. AttributeError
5. EOFError
6. ModuleNotFoundError
7. FileNotFoundError
8. IndexError
9. NameError
10. SystemError
11. TypeError
12. ValueError

4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except / finally
    형식 :
try : 
    코드 작성 영역
except :
    예외 발생 시 처리 영역
finally:
    언제나 실행되는 영역

'''

exception_list = [
    (1, "BaseException" , "최상위 예외 클래스"),
    (2, "Exception" , "대부분 예외 클래스의 슈퍼 클래스"),
    (3, "ArithmeticError" , "산술 연산에 문제가 있을 때"),
    (4, "AttributeError" , "잘못된 속성을 참조할 때"),
    (5, "EOFError" , "파일에서 더 이상 읽어 들일 데이터가 없을때"),
    (6, "ModuleNotFoundError" , "import할 모듈이 없을때"),
    (7, "FileNotFoundError" , "존재하지 않는 파일일 때"),
    (8, "IndexError" , "잘못된 인덱스를 사용할 때"),
    (9, "NameError" , "잘못된 이름(변수)을 사용할 때"),
    (10, "SystemError" , "문법이 틀렸을때 "),
    (11, "TypeError" , "계산하려는 데이터의 유형이 잘못되었을 때"),
    (12, "ValueError" , "계산하려는 데이터의 값이 잘못되었을 때"),
]

# table = PrettyTable()
# table.field_names = ['순번', '예외 클래스', '의미']
# table.add_rows(exception_list)
#
# print(" 예외 클래스 종류 및 설명:")
# print(table)
#
# try :
#     a = int(input('나누는수를 입력하세여 >>> '))
#     b = int(input('나누어지는 수를 입력하세요 >>> '))
#     print(f'b / a = {b / a}')
# except :
#     print('예외가 발생했습니다,')
#
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try / except 문을 사용하여 '예외가 발생했습니다.'를 출력할 수 있도록 작성하세요
'''
#
# try :
#     height = input('키를 입력하세요>>> ')
#     height = round(height)
#     print(f'입력하신 키 {height}cm로 처리됩니다.')
# except :
#     print('예외가 발생했습니다.')

'''
    1) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가
        처리됨. 하지만 이상에서 본 것 처럼, 0으로 나누는 경우와, str 자료형을 실수로
        바꾸고자 하는 경우에 서로 다른 메시지를 출력해줄 수 있다면, 개발자에게
        예외를 처리할 수 있을만한 추가적인 정보를 제공할 수 있음.
        
    1)-1. 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
    1)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
    등으로 특정 예외에 따른 서로 다른 안내문을 제시한다고 하면,
    :except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''
#
# try :
#     a = int(input('나누는 수를 입력하시오 >>> '))
#     b = input('나누어지는 수를 입력하시오')
#     print(f'b/a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력할 수 있다')
#
# try :
#     a = int(input('나누는 수를 입력하시오 >>> '))
#     b = input('나누어지는 수를 입력하시오')
#     print(f'b/a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')

'''
    거의 모든 예외는 Exception 클래스의 서브 클래스에 해당함. 따라서 모든 예외는 Exception의
    인스턴스가 됩니다. 다음과 같이 except의 마지막에 Exception을 명시하면 예상하자 못한 예외들도 웬만하면
    
try :
    코드 작성 영역
except 예외클래스1:
    예외 메시지1
except 예외클래스2:
    예외 메시지2
'''
'''
except Exception:
    예외 메시지n
finally:
    항시 실행되는 코드 영역

Java에서와 동일하게 Exception이 가장 상위에 있는 
'''
#
# z = [10, 20, 30, 40, 50]
#
# try :
#     print(z[10])
# except : IndexError as e:
# print(e)

'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데,
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계 없이 맨 마지막에 항상 처리되는 구문
'''
#
# try :
#     a = int(input('나누는 수를 정수로 입력하세요'))
#     b = int(input('나누어지는 수를 정수로 입력하시오'))
#     result = b / a      # 예외가 발생할 수 있는 구간이 try 문 내에 있어야만 합니다.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f'b/a = { result }')
# finally:
#     print('프로그램종료')


'''
5. 강제로 예외를 발생기키기
    어던 사람이 나이를 정수로 입력 받는 프로그램을 사용한다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지
    않습니다.(그래서 우리는 0미만 
    하지만 -1000살이 되는 것이 불가능하기 때문에 조건문이 아니라 직접 예외를 발생시켜서 처리하는 방법을 학습했습니다. -> raise문

형식 : 
raise 예외 클래스()

또는 
raise 예외 클래스(예외메세지)

raise의 경우 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception입니다.
'''

# age = int(input('나이를 입력하시오 >> '))     -1000 입력해도ㅓ 예외발생 안함
# print(f'당신의 나이는 {age} 살입니다.

try :
    age  = int(input('나이를 입력하세요>> '))
    if age < 0 or age > 200:
        raise Exception('강제로 발생시킨 예외입니다.')
except Exception as e:
    print('발생한 예외 메세지는 다음과 같습ㄴ;다.')
    print(e)
'''
    이상은 특정 예외가 아니라 212번으로 넘어가기만하면 바로 예외가 발생함
    즉 age에 가능한 정수값을 넣더라도ㅓ 예외가 발생하기 때문에 단도ㅓㄱ으로 처리가 안되는거임
    이부분에서 조건뭉르 이용해서 특정 조건일때만 예오ㅣ로 넘기는 추가코드가 필요함

'''# 사용자 정의 예외 클래스
# class ScoreOutOfRange(Exception):
#     pass
#
# try:
#     score = int(input('점수를 입력하세요 (0~100): '))
#     if score > 100 or score < 0:
#         raise ScoreOutOfRange('점수는 0 이상 100 이하만 가능합니다.')
# except ScoreOutOfRange as e:
#     print(e)
# except ValueError as e:
#     print('숫자만 입력해야 합니다.', e)
# except Exception as e:
#     print('알 수 없는 예외 발생:', e)
# else:
#     if score >= 80:
#         print(' 합격입니다!')
#     else:
#         print('불합격입니다.')
# finally:
#     print(' 프로그램이 종료되었습니다.')

score = input('점수 >>> ')
if score < 80:
    print('test')
