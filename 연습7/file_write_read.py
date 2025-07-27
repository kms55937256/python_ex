#7.1
lines = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

# 파일에 쓰기
with open("sample.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

# 파일에서 읽기
print("파일에서 읽어온 내용:")
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content.strip())