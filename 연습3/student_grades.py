#3.3
grades = {'김철수': 85, '이영희': 92, '박민수': 78, '최수진': 95}

print("학생 성적:")
for student in grades:
    print(f"{student}: {grades[student]}점")

print(f"평균 점수: {sum(grades.values()) / len(grades):.1f}점")