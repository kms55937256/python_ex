#4.5
num = int(input("숫자를 입력하세요: "))

if num > 1:  
    for i in range(2, num):
        if num % i == 0:  
            print(f"{num}은 소수가 아닙니다.")
            break
    else:
        print(f"{num}은 소수입니다.")  
else:
    print(f"{num}은 소수가 아닙니다.")