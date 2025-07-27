#5.8
# 1. 튜플 언패킹
x, y = (10, 20)
print(f"좌표: x={x}, y={y}")

# 2. 리스트 언패킹
a, b, c = [1, 2, 3]
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# 3. 가변 인수 (*args)
print(f"가변 인수의 합: {sum((10, 20, 30))}")

# 4. 키워드 인수 (**kwargs)
print("키워드 인수들:", ", ".join(f"{k}={v}" for k, v in {"name":"김철수", "age":25, "city":"서울"}.items()))