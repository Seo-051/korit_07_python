from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? ({menu.get_items()}) >>> ')

    if choice == 'off':
        is_on = False
        print(f'자판기가 종료되었습니다.')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        if drink == None:           # choice에 오타가 있을경우 None이 반환되기 때문에 고전적 예외 처리
            continue                # continue가 실행되면 이 이하의 코드라인은 실행되지 않고,
                                    # while 반복문의 가장 앞부분으로 돌아가서 다음 반복이 실행됨
        # 음료 이름을 입력 받은 시점부터의 프로세스를 떠올려서 코드를 작성해야만합니다.
        #  이때 고려해야할 것은 절차지향 방식으로 코딩했을 때의 과정과, 현재 참조해야하는 파이썬 모듈을
        # pop version의 함수 작성 순서대로 저희가 작동하도록 했습니다.
        # is_resources_enough(order_ingredient) / is_resources_sufficient(drink)
        if coffee_maker.is_resource_sufficient(drink):
            # 조건문을 이용해 process_coins()와 make_payment()를 활용하여,
            # 모든 것이 true일 때 '작동 중 입니다'를 출력할 수 있도록 작성하시오
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)



