import random

'''
''.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element
들을 합쳐서 str로 합쳐주는 method
'''
# temp = ['배', '고', '프', '다']
# feeling = ''.join(temp)
# print(temp)
# print(feeling)
# result = ''

# for letter in temp:
#     result += letter
#  print(result)

# feeling2 = '/'.join(temp)
# print(feeling2)
'''
이상의 예시는 display를 다시 재조합하여 str로 바꿀때 사용할 겁니다.
'''
#todo - 1 : 비어있는 list인 display를 선언하시오
word_list = ['apple', 'banna', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
# temp = ['배', '고', '프', '다']
# feeling = ''.join(temp)
# print(temp)
# print(feeling)
# result = ''

#todo - 2: chosen_word의 문자 개수만큼 '_'를 display에 추가하시오

for letter in chosen_word:
    display.append('_')

#todo - 3 : 사용자가 추측을 반복할 수 있도록 while 반복문을 작성해야 함 사용자가 chosen_word의 모든 문자열들을 맞추었을때, 즉 display

print(display)
#
# num = 0
# while display != chosen_word:
#     guess = input('알파벳을 하나를 추측해서 입력하세요 >> ').lower()

#     if chosen_word[num] == guess:
#         display[num] = guess
#         num += 1
#         print(display)
#
#     if display == chosen_word:
#         break

while '_' in display:
    guess = input('알파벳을 하나를 추측해서 입력하세요 >> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print("정답입니다!")

print(' '.join(display))