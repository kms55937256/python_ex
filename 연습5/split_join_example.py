#5.1
text = "Python is awesome programming language"
print(f"원본 문자열: {text}")

# 문자열을 공백 기준으로 분리
words = text.split()
print(f"분리된 단어들: {words}")

# 하이픈(-)으로 단어를 연결
print(f"하이픈으로 연결: {'-'.join(words)}")

# 대문자로 변환 후 공백으로 다시 연결
print(f"대문자로 변환 후 공백으로 연결: {' '.join(words).upper()}")