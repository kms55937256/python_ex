#7.5
logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:00:00 - INFO - 사용자 로그인 성공",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

# 로그 파일 생성
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(logs))

print("로그 파일이 생성되었습니다.\n")

# 로그 파일 읽기
with open("log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 특정 레벨 로그 필터링 함수
def filter_logs(lines, level):
    return [line.strip() for line in lines if f" - {level} -" in line]

# ERROR 로그 출력
print("ERROR 레벨 로그들:")
for log in filter_logs(lines, "ERROR"):
    print(log)

print("\nWARNING 레벨 로그들:")
for log in filter_logs(lines, "WARNING"):
    print(log)
