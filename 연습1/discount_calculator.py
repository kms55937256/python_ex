price = int(input("상품 가격을 입력하세요: "))
rate = int(input("할인율을 입력하세요(%): "))
discount = price * rate // 100
final = price - discount

print(f"원래 가격: {price}원")
print(f"할인율: {rate}%")
print(f"할인 금액: {discount}원")
print(f"최종 가격: {final}원")