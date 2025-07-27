#6.5
students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print(f"학생 정보: {students}")

# 이름순 정렬
by_name = sorted(students, key=lambda x: x[0])
print(f"이름순 정렬: {by_name}")

# 점수 오름차순 정렬
by_score = sorted(students, key=lambda x: x[1])
print(f"점수순 정렬: {by_score}")

# 점수 내림차순 정렬
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"점수 내림차순: {by_score_desc}")