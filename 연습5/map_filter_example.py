#5.7
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 숫자: {num}")

# 모든 수의 제곱
squared = list(map(lambda x: x**2, num))
print(f"모든 수의 제곱: {squared}")

# 5보다 큰 수들
greater_than_5 = list(filter(lambda x: x > 5, num))
print(f"5보다 큰 수들: {greater_than_5}")

# 5보다 큰 수들의 제곱
squared_gt5 = list(map(lambda x: x**2, filter(lambda x: x > 5, num)))
print(f"5보다 큰 수들의 제곱: {squared_gt5}")