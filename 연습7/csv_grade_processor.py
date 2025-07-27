#7.2
grades = [("김철수", 85), ("이영희", 92), ("박민수", 78), ("최수진", 95)]

# 파일 저장
with open("grades.csv", "w", encoding="utf-8") as f:
    f.write("이름,점수\n")
    for n, s in grades:
        f.write(f"{n},{s}\n")

print("학생 성적이 grades.csv에 저장되었습니다.\n")

# 파일 읽기 + 평균 계산
print("성적 분석 결과:")
total = 0
with open("grades.csv", "r", encoding="utf-8") as f:
    next(f)  # 헤더 건너뛰기
    for line in f:
        n, s = line.strip().split(",")
        s = int(s)
        print(f"{n}: {s}점")
        total += s

print(f"전체 평균: {total / len(grades):.1f}점")