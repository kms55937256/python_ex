#5.10
score = 85
print(f"점수: {score}, 결과: {'합격' if score >= 80 else '불합격'}")

age = 17
print(f"나이: {age}, 상태: {'성인' if age >= 18 else '미성년자'}")

num = [5, 12, 8, 23, 42]
print(f"숫자들의 최대값: {max(num) if num else None}")

num2 = [-3, 5, -1, 12, 8, -7, 23]
print(f"양수들: {[n for n in num2 if n > 0]}")