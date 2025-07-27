#5.5
sq = {x: x**2 for x in range(1, 6)}
print(f"1부터 5까지의 제곱 딕셔너리: {sq}")

even_sq = {x: x**2 for x in range(2, 11) if x % 2 == 0}
print(f"짝수만의 제곱 딕셔너리: {even_sq}")