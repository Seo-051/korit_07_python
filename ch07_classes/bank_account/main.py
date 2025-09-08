class BankAccount:
    def __init__(self, owner, account_num, balance):
        self._owner = owner
        self._account_num = account_num
        self._balance = balance

    # Getter
    def get_owner(self):
        return self._owner

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance

    # Setter
    def set_owner(self, owner):
        self._owner = owner

    def set_account_num(self, account_num):
        self._account_num = account_num

    def set_balance(self, balance):
        self._balance = balance

    # 입금
    def deposit(self, amount):
        if amount <= 0:
            print("입금 금액은 0원보다 커야 합니다.")
        else:
            self._balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액 : {self._balance}원")

    # 출금
    def withdraw(self, amount):
        if amount <= 0:
            print("출금 금액은 0원보다 커야 합니다.")
        elif self._balance - amount < 0:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else:
            self._balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액 : {self._balance}원")

    # 계좌 정보 출력
    def print_account_info(self):
        print(f"계좌 소유자 : {self._owner}")
        print(f"계좌 번호 : {self._account_num}")
        print(f"현재 잔액 : {self._balance}원")
        print()


# 계좌 생성
account1 = BankAccount("홍길동", "123-456-789", 100000)
account2 = BankAccount("신사임당", "987-654-321", 500000)

# 초기 계좌 정보 출력
account1.print_account_info()
account2.print_account_info()

# 입금 / 출금 수행
account1.deposit(50000)         # 5만원 입금
account1.withdraw(200000)       # 20만원 출금 시도 (실패)
account1.withdraw(100000)       # 10만원 출금 (성공)

account2.withdraw(100000)       # 10만원 출금
account2.deposit(200000)        # 20만원 입금

# 최종 계좌 정보 출력
print("최종 계좌 정보")
account1.print_account_info()
account2.print_account_info()
