#이중 for문을 이용한 구구단 출력
for i in range(2, 10):
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, (i*j)))

# 리스트 컴프리헨션으로 구구단 출력
result = ["{} * {} = {}".format(i, j, (i*j)) for i in range(2, 10) for j in range(1, 10)]
print(result)