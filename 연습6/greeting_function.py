#6.3
def greet(name, lang="ko", msg=""):
    if lang == "ko":
        text = f"안녕하세요, {name}님! {msg}".strip()
    else:
        text = f"Hello, {name}! {msg}".strip()
    return text

print(greet("김철수"))
print(greet("John", "en"))
print(greet("이영희", msg="좋은 하루 되세요!"))