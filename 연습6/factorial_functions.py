#6.2
def fact_r(n):
    if n <= 1:
        return 1
    return n * fact_r(n - 1)

def fact_i(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for value in (5, 7):
    print(f"{value}! (재귀) = {fact_r(value)}")
    print(f"{value}! (반복) = {fact_i(value)}")