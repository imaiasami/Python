# 내장 함수
print(int("100"))
print(int("100", 16))
print(int("100", 8))
print(int("100", 2))

print(float("3.1"))

# 사용자 함수
# 함수 정의
def 함수명():
    print("함수 호출")
    return True

a = 함수명()
print(a)

# 위치 인자를 이용한 함수의 호출
def restaurant(food, drink, dessert):
    return {"food":food, "drink":drink, "dessert": dessert}

a = restaurant("스테이크", "와인", "케이크")
print(a)
print(type(a))

# 매개변수의 이름을 함께 지정해서 순서에 관계없이 호출 가능
b = restaurant(drink="막걸리", dessert="파전", food="잔치국수")
print(b)

# 매개변수의 초기값을 지정할 수 있다.
def rest(food="초밥", drink="사케", dessert="아이스크림"):
    return {"food":food, "drink":drink, "dessert": dessert}
print(rest())
print(rest("가츠동"))
print(rest("돈가스", "맥주"))
print(rest("피자", "소주", "과일"))
