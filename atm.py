# balance : 초기 잔액을 설정하는 변수를 초기화해 주세요
balance = 10000

# 사용자로부터 atm 기계의 사용 목적에 맞는 기능을 선택할 수 있도록 
# 기능 입력을 받는 기능을 구현해 주세요(입금, 출금, 종료, 입출금 내역 영수증)


# 무한루프? while vs for

while True:
    num = input("사용하실 기능의 번호를 선택해 주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    if num == '4': #4번은 종료
        break 

    if num == "1": #입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input("입금할 금액을 입력해주세요: ")) #str "5000" -> int로 형변환
        balance += deposit_amount #balance(15000) = balance(10000) += deposit_amount(5000)
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원입니다.')

    if num == "2":
        pass

    if num == "3":
        pass

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원입니다.')
