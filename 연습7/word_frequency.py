#7.3
from collections import Counter

# 샘플 텍스트 파일 생성
text = "파이썬 프로그래밍 언어 파이썬 배우기 쉬운 강력한 프로그래밍 언어 파이썬"
with open("words.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 파일 읽기
with open("words.txt", "r", encoding="utf-8") as f:
    content = f.read().strip()

words = content.split()  
freq = Counter(words)    

print("단어 빈도 분석 결과:")
for w, c in freq.items():
    print(f"{w}: {c}번")
