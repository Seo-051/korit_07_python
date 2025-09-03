print("Hello World")

# 주석(comment) - 한 줄 주석 / 파이썬 인터프리터가 코드로 인식하지 않음.

# 사후 주석 -> ctrl + /

'''
다중 주석 처리
'''

print(1)            # 숫자 자료형
print('1')          # 문자열 자료형

print(1+2)          # 결과값 : 3
print('1'+'2')      # 결과값 : 12

print(type('1'))    # 결과값 : <class 'str'>
print(type(1))      # 결과값 : <class 'int'>
print(type(1.1))    # 결과값 : <class 'float'>

'''
print() : 콘솔에 출력하는 '함수'
type() : 소괄호 내에 있는 데이터(argument) 가 어떤 자료형인지 알려주는 명령어
        -JS에어는 typeof가 함수가 아니라 연산자임
'''
print('python 수업을 시작하겠습니다')
print('''
이렇게 다중으로 작성가능
java에서는 줄 넘어갈 때 마다 + 로 연결해줘야 했는데 좀 더 편함
''')

'''
이상에서 알 수 있는 점은 print()가 System.out.println() 처럼 자동 개행이 된다는 점

변수(Variable) : 데이터를 저장하는 바구니
'''
# 변수 선언 및 초기화
# 변수명 = 데이터
name = '김일'
age = 20
print('안녕하세요 제 이름은' + name + ' 입니다. 나이는' + str(age) + ' 살입니다.')

'''
python은 좀 까탈스러워서 Java 나 JS할때 처럼 str이면 뒤의 int/float을
알아서 바꾸어주는 짓을 안함

그때 사용하는 형변환 함수가 있음

str() : 다른 데이터를 문자열 자료형으로 바꿔주는 함수
int()  : 문자열/ 실수 자료형을 정수형으로 바꿔주는 함수 / java : (int)"1.3";
float() : 실수 자료형으로 바꿔주는 함수

귀찮아서 f-string 개념 도임
'''
print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}입니다.')

'''
JS에서 비슷한 개념을 배움
console.log(`안녕하세요, 제 이름은 ${name}이고, 나이는 ${age}살 입니다.`);의 python판 이라고 생각하면 됨.

Java에서의 Scanner 같은 기능을 하는 함수 : input()
'''
name2 = input('이름을 입력하세여 >> ')
print(name2)