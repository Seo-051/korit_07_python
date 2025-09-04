import random

# from ch05_hangman.hangman01 import guess

word_list = ['apple', 'banna', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1: 비어있는 list인 display를 만드시오.
display = []
# print(display)
# display.append('김')
# print(display)
# display[1] = 2
# print(display)
#todo - 2: 이상의 코드라인을 참조하여 chosen_word의 각 문자 개수 마다 '_'를 추가 하시오. 예를 들어 chosen_word == 'apple'이라면 display = [ '_', '_', '_', '_', '_', ] 가 되어야 합니다.즉, chosen_word의 문자 개수 만틈 '_'가 있어야 함

for letter in chosen_word:
    display.append('_')         # 반복 실행문에서 변수 i 가 쓰이지 않아서 그냥 반복 횟수가 len(chosen_word)만큼이라는 것을 알 수 있습니다. 그 경우에는 i와 같은 특정 변수를 쓰기 보다는 _를 써서 반복횟수만 통제한다고 표시해주는 편

print(display)

#todo - 3: chosen_word의 각 문자들을 반복 시키시오. 만약 그위치의 문자 guess와 일치하면, ㅐ

guess = input('알파벳을 하나를 추측해서 입력하세요 >> ').lower()

for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
        display[letter] = guess
        print(display)



