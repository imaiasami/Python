# 문자열 슬라이싱
# print([:])         # 처음부터 끝까지 출력
# print([start:])    # start 부터 끝까지
# print([:end])      # 처음부터 end - 1 까지
# print([start:end])    # start 부터 end - 1 까지
# print([start:end:step])    # start 부터 end - 1 까지 step만큼 건너뛴다.
# print([start:end])    # start 부터 end - 1 까지
# print(find())         # index 값을 리턴해준다.


a = "abcd"
print(a)
a = 'abcd'
print(a)
a = "abcd 가나다라마바사"
print(a)
print(a[2])
print(a[:])         # 처음부터 끝까지 출력
print(a[5:])
print(a[:4])
print(a[::2])
# find() 는 index 값을 리턴해준다.
print(a.find("가"))
# find() 는 없는 값이면 -1의 index값을 리턴해준다.
print(a.find("아"))
# index() 는 index 값을 리턴해준다.
print(a.index("나"))
# index() 는 없는 값을 찾으면 전체 에러가 발생한다.
# print(a.index("아"))

path = "c:\\test\\abcd\\abcde.jpg"      # \ 역슬러쉬 하나는 이스케이프 문자 \t는 tab
print(path)
print(path.find("\\"))      # 왼쪽에서 오른쪽으로 찾는다
print(path.rfind("\\"))     # 오른쪽에서 왼쪽으로 찾는다.

# 경로를 제외한 파일명을 찾아서 출력
print(path[path.rfind("\\")+1:])

# split(기준 문자열) : 기준 문자열 기준으로 잘라서 리스트 형식으로 반환해준다.
print(path.split("\\"))
print(type(path.split("\\")))

# replace(대상 문자열, 변경 문자열)
a = "Hello"
print(a)
print(a.replace("Hello", "안녕"))

# strip() : 양쪽의 공백을 제거
a = "       Hello    "
print(a)
print(a.strip())

# upper() : 소문자를 대문자로 변환
a = "abcd"
print(a.upper())

# lower() : 대문자를 소문자로 변환
a = "ABCD"
print(a.lower())

a = "aaaaaaabbbbbbbbbbccccccccccdddddddddd"
print(a.count("a"))     # a 가 포함된 문자열의 갯수를 반환
print(len(a))           # 문자열의 길이값을 리턴

print(a.isalpha())      # 알파벳이면 True
a = "1234"
print(a.isalpha())      # 알파벳이 아니면 False

a = "abcd"
print(a.islower())      # a 가 소문자이냐? 소문자이면 True

a = "ABCD"
print(a.isupper())      # a 가 대문자이냐? 대문자이면 True

a = "abCD"
print(a.islower())

a = "abCD"
print(a.isupper())

a = "1234"
print(a.isdecimal())    # 10진수인지 검사, 10진수이면 True

a = "1234"
print(a.isdigit())      # 문자가 아라비아 숫자인지 검사, 아라비아 숫자이면 True

a = "1234"
print(a.isnumeric())      # 문자가 숫자인지 검사, 숫자이면 True

a = "1234"
print(dir(str))         # str 클래스의 함수 목록 보기