# balance : 초기 잔액을 설정하는 변수를 초기화해 주세요
balance = 10000

# 사용자로부터 atm 기계의 사용 목적에 맞는 기능을 선택할 수 있도록 
# 기능 입력을 받는 기능을 구현해 주세요(입금, 출금, 종료, 입출금 내역 영수증)


# 무한루프? while vs for


while True:
    num = input("사용하실 기능의 번호를 선택해 주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    if num == '4': #4번은 종료
        break 

    if num == "1":
        pass

    if num == "2":
        pass

    if num == "3":
        pass

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원입니다.')
