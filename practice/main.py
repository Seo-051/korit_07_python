game_candidate = int(input('후보 게임 수를 입력하세요 >>> '))

game_list = []

votes_dict = {

}

for i in range(game_candidate) :
    game_name = input(f'{i+1}번째 게임 이름을 입력하세요 >>> ')
    game_list.append(game_name)

pick = input('전체 투표 수를 입력하세요 >>> ')
game_options = ', '.join([f'{i+1}: {name}' for i, name in enumerate(game_list)])
print(game_options)

for key, value in votes_dict.items():
        print(key, value)


