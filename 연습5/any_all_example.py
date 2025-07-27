#5.6
num1 = [2, 4, 6, 8, 10]
num2 = [1, 3, 5, 7, 12]

print(f"숫자 리스트: {num1}")
print(f"모든 수가 짝수인가? {all(x % 2 == 0 for x in num1)}")
print(f"하나라도 10보다 큰 수가 있는가? {any(x > 10 for x in num1)}\n")

print(f"숫자 리스트2: {num2}")
print(f"모든 수가 짝수인가? {all(x % 2 == 0 for x in num2)}")
print(f"하나라도 10보다 큰 수가 있는가? {any(x > 10 for x in num2)}")