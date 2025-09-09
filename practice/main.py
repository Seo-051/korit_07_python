game_candidate = int(input('후보 게임 수를 입력하세요 >>> '))

game_list = ' '

dict = {

}

for i in range(game_candidate) :
    game_list = input(f'{i+1}번째 게임 이름을 입력하세요 >>> ')

pick = input('전체 투표 수를 입력하세요 >>> ')

for key, value in range(dict) :
    print(key, value)

