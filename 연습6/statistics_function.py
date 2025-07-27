#6.4
import math

def statistics(lst):
    avg = sum(lst) / len(lst)
    mx = max(lst)
    mn = min(lst)
    var = sum((x - avg) ** 2 for x in lst) / (len(lst) - 1)  # 표본 표준편차
    std = math.sqrt(var)
    return avg, mx, mn, std

num = [10, 20, 30, 40, 50]
avg, mx, mn, std = statistics(num)

print(f"숫자들: {num}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {mx}")
print(f"최솟값: {mn}")
print(f"표준편차: {std:.2f}")