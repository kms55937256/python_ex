#8.2
import datetime
import random
import calendar

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일')} {calendar.day_name[now.weekday()]}")

print(f"임의의 숫자: {random.randint(1, 10)}")
print(f"임의의 실수: {round(random.uniform(1, 5), 2)}")

fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
print(f"임의의 리스트 요소: {random.choice(fruits)}")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")
