# 논리형 (bool) : Ture, False
a = True
print(a)
b = False
print(type(b))
a = bool(True)
print(a)
a = bool(0)         # 0이면 False, 0이 아닌 값은 True
print(a)
a = bool(2)         # 0이면 False, 0이 아닌 값은 True
print(a)

# 정수형
a = 5
print(type(a))
a = int(10)
print(a)

# 실수형(float)
a = 3.1
print(type(a))
print(a)

# 산술 연산자
a = 10
b = 3
print(a+b)          # 13
print(a-b)          # 7
print(a*b)          # 30
print(a/b)          # 3.3333333333333335, 실수로 나온다.
print(a//b)         # 3, 몫을 구하는 문법, 3이 출력된다.
print(a%b)          # 1, 나머지 연산자
print(a**b)         # 1000, 10의 3승, 거듭제곱(누승)

# 복소수(Complex)
a = 2 + 3j
print(a)            # (2 + 3j)
print(type(a))      # <class 'complex'>

