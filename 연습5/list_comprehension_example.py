#5.2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 리스트: {numbers}")

# 짝수만 추출
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"짝수들: {even_numbers}")

# 짝수들의 제곱
squared_evens = [n ** 2 for n in even_numbers]
print(f"짝수의 제곱: {squared_evens}")