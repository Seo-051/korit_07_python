'''
주어진 해가 윤년인지 아닌지 계산하는 프로그램을 작성합니다.
일반적으로 1년은 365일이고, 윤년은 366일로 2월에 하루가 더 있습니다.

다음은 특정 연도가 윤년인지 확인하는 방법입니다.
    1. 4로 나누어 떨어지는 해는 윤년입니다.
    2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
    3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.

ex)

    2000 / 4 = 500 이라서 윤년
    2000 / 100 = 20 이라서 윤년 x
    2000 / 400 = 5 이라서,

    최종적으로 2000년은 윤년에 해당합니다.

    2100 / 400 = 525 이라서 윤년
    2100 / 100 = 21 이라서 윤년 x
    2100 / 400 = 5.25 이라서 윤년 x

    최종적으로 2100년은 윤년이 아닙니다.

실행 예

윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2200년
2200년은 윤년이 아닙니다.

윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2000년
2000년은 윤년입니다.
'''
#
# public class Condition08 {
#     public static void main(String[] args) {
#         // Scanner import / 필요 변수 자료형 및 변수명 선언/ 안내문 / 대입
#         // 이후에 해당 year가 윤년이 맞는지 아닌지를 체크하시면 되겠네요.
#     Scanner scanner = new Scanner(System.in);
#     System.out.println("연도를 입력하세요 >>> " );
#     int year = scanner.nextInt();
#
#     if(year % 400 == 0  ) {
#         System.out.println(year + "년은 윤년입니다");
#     } else if ( year % 100 == 0 ) {
#         System.out.println(year + "년은 윤년이 아닙니다");
#     } else if ( year % 4 == 0 ) {
#         System.out.println(year + "년은 윤년입니다");
#     } else {
#         System.out.println(year + "년은 윤년이 아닙니다");
#     }

'''
논리 연산자 :
    1) and : A and B -> A와 B가 모두 참일때 실행                 &&
    2) or : A or B -> A 혹은 B 중에 하나가 참이면 실행문 실행      ||
    3) not : if not A -> A가 false일 때 실행문 실행              !
leap_year 패키지 -> main
'''
year = int(input('윤년인지 확인하고 싶은 연도를 입력하세요 >>> '))
# 방법 1
if year % 400 ==0 or year % 4 == 0 and not year % 100 == 0:
    print(f'{year} 년은 윤년 입니다.')
else : print(f'{year} 년은 윤년이 아닙니다.')

# 방법 2
if year % 400 == 0 :
    print(f'{year} 년은 윤년 입니다.')
elif  year % 100 == 0 :
    print(f'{year} 년은 윤년이 아닙니다.')
elif  year % 4 == 0 :
    print(f'{year} 년은 윤년 입니다.')
else :
   print(f'{year} 년은 윤년이 아닙니다.')

# ch02_loops -> main