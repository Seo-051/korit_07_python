import random

logo = '''
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'
'''
print(logo)

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

word_list = ['apple', 'banna', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
end_of_game = False
display = []
lives = 6

for _ in range(len(chosen_word)):
    display.append('_')

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

    if lives == 0 or '_' not in display:
        print(f'기회를 소진하였습니다. 정답은 {chosen_word} 입니다.')
        end_of_game = True
