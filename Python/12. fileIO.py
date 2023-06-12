# 파이썬에서 파일 읽고 쓰기

# File Open
# 변수 = open(파일 이름, 파일 열기 모드)

# File Open Mode
# r(읽기 모드) : 파일을 읽기 전용으로 open 할 때 사용,
# 모드를 생략하면 기본으로 r 모드로 설정
# w(쓰기 모드) : 파일에 내용을 쓸 때, 쓰기 모드로 열게되면 해당 파일이
# 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
# a(추가 모드) : 파일의 마지막 부분에 새로운 내용을 추가한다.

# file = open("sample.txt", mode="w", encoding = "utf-8")
# file.write("안녕하세요")
# file.close()

# readFile = open("sample.txt", mode="r", encoding="utf-8")

# 파일 내용 전체 읽기
# content = readFile.read()
# print(content)

# 파일 내용 한 줄 씩 읽기
# for s in readFile:
#     print(s)
# readFile.close()

# with : with 라인이 끝나면 자동으로 자원을 반환한다.
with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())

# 실습문제
# for문을 이용해서 아래 score 변수의 데이터를 파일로 저장하는 프로그램을 작성하세요
# 파일명 : score.txt
score = ("홍길동" : 100, "김개똥":80, "이말똥": 90)
