a = "hello python"
print(a)
print(type(a))

b = """hello
python"""
print(b)

a = "hello"
b = "python"
print(a + b)
print(a + "\t" + b)
print("*" * 40)

age = 30
a = "제 나이는 %d살 입니다."%age
print(a)
height = 170.4
a = "제 나이는 %d살 이고, 키는 %6.1fcm 입니다."%(age, height)
print(a)