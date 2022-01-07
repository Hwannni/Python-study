#Python 1day
#2022-01-05

# 숫자형- 사칙연산: +, -, *, %, / 등...
a = 3
b = 4
print(a+b)
print(a-b)
print(a*b)
# *가 2번 연속되면 제곱 연산
print(a**b)
print(a%b)
print(a/b)
print(a//b)

# 문자열 자료형
# 문자열에 작은따옴표(') 포함시키기: ""로 둘러싸기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰따옴표(") 포함시키기: ''로 둘러싸기
say = '"Python is very easy." he says.'
print(say)

# 줄을 바꿀때는 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short \nYou need python"
print(multiline)

# 문자열 연산: +, *
head = "Python"
tail = "is fun!"
print(head + tail) # head와 tail이 연결된다.
print(head * 3) # head의 값이 3번 나오게 된다.

# 문자열 인덱싱과 슬라이싱
a = "Life is too short, you need python"
print(a[3]) # a라는 문자열의 네 번째 문자 e가 출력된다.
print(a[0:4]) # a라는 문자열의 0이상 4미만의 문자가 전부 출력된다.

# 문자열 포매팅
a = "I eat %d apples." % 3 # 숫자 바로 대입
b = "I eat %s apples." % "five" # 문자열 바로 대입
print(a, b)

# 문자열 관련 함수
# count
count = "apple"
print(count.count('p')) # 문자열 중 문자 p의 개수 출력
# find
find = "Python is the best choice"
print(find.find('b')) # 문자열 중 문자 b가 처음으로 나온 위치
# join
print(",".join('abcd')) # 각각의 문자 사이에 ','를 삽입
# upper와 lower
a = "hi"
b = "HI"
print(a.upper()) # a를 전부 대문자로 바꿔줌
print(b.lower()) # b를 전부 소문자로 바꿔줌

# 공백 지우기
Kim = " Hi  " # 왼쪽 공백 지우기
print(Kim.lstrip())

Min = " Hi  " # 오른쪽 공백 지우기
print(Kim.rstrip())

Yon = " Hi  " # 양쪽 공백 지우기
print(Kim.strip())

# 문자열 바꾸기(replace)와 나누기(split)
Jhon = "Life is too short" # Life가 Your leg로 바뀜
print(Jhon.replace("Life", "Your leg"))

Bin = "Life is too short" # 공백을 기준으로 나눔
print(Bin.split())