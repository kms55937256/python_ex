#4.2
multiples = []
for num in range(1, 101):
    if num % 3 == 0:
        multiples.append(num)

print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {sum(multiples)}")
print(f"3의 배수의 개수: {len(multiples)}개")