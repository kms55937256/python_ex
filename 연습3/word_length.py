#3.7
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

long_word = max(words, key=len)
short_word = min(words, key=len)

print("단어 목록:", words)
print(f"가장 긴 단어: {long_word} ({len(long_word)}글자)")
print(f"가장 짧은 단어: {short_word} ({len(short_word)}글자)")