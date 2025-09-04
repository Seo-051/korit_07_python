import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있습니다.
'''
#todo - 1: 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화 하세요
lives = 6

#todo - 2: hangman03을 참조하여 while 반복문 바깥을 완성하시오
word_list = ['apple', 'banna', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display.append('_')
# print(display)
#
# while '_' in display:
#     guess = input('알파벳을 하나를 추측해서 입력하세요 >> ').lower()
#
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display[i] = guess
#     print(display)
#
# print("정답입니다!")
#
# print(' '.join(display))

#todo - 3: while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 작성
end_of_game = False

while not end_of_game:
    guess = input('알파벳을 하나를 추측해서 입력하세요 >> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives} 번 남았습니다')

    print(stages[lives])
    print(' '.join(display))
        # else :
        #     lives -= 1
        #     if lives == 0:
        #         print('모든 기회를 잃었습니다.')
        #         print(stages[lives])
        #         end_of_game = True
        # 라고 작성하면 안됨. 반복문 내부에서 guess가 일치하는 여부를 따라지는 중입니다.
        # 예를 들어 chosen_word가 apple이고, guess가 a라고 가정했을때
    if lives == 0 or '_' not in display:
        print(f'기회를 소진하였습니다. 정답은 {chosen_word} 입니다.')
        end_of_game = True




#todo - 4: lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때 마다 올바른 stages의 element가 출력될 수 있도록 작성하시오