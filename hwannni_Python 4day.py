#Python 4day
#2022-01-08

# 함수 : def로 정의한다.
def sum(a, b): # 인자로 a, b 2개를 넣어줬다.
    result = a + b
    return result # return이 출력
print(sum(1, 2)) # a, b 인자에 1, 2 를 넣어준다.

# 입력값이 없는 함수: 함수 인자에 값이 없음
def say():
    return 'Hi'
print(say())
# 결과값이 없는 함수: return이 없음
def sum(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
print(sum(3, 5)) # 결과값이 없어서 none이 나온다.

# 여러 개의 입력값
def sum_many(*args): # *args를 사용하면 여러 개의 인자를 이용할 수 있다.
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3,4,5)) # *args를 사용했기 때문에 여러 개를 넣어도 가능하다.

# 함수의 결과값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b, a*b, a-b # 리턴값이 세개지만 튜플 형식으로 하나로 묶여 나온다.
print(sum_and_mul(1,2))

# 매개 변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): # True라는 기본값을 미리 설정한 것이다.
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("최민환", 20, False) # 위에서 기본값으로 man=True를 설정했기 때문에 인자에 False를 넣으면 자동적으로 "여자입니다."가 출력된다.
# 초깃값 설정 시 주의할 사항: 인자의 입력 순서가 중요!, 초깃값을 설정한 인자는 무조건 맨 뒤로 가야한다.

# 함수 안에서 선언된 변수의 효력 범위
a = 1
def vartest(a): # 지역 변수의 경우 함수 밖의 값에는 영향을 주지 못한다.
    a = a + 1
    return a # return을 해야 a의 값이 지역을 벗어나서 영향을 줄 수 있다.

a= vartest(a) # return 받은 값이 나와서 vartest(a)의 값으로 들어간다.
print(a)
# return 말고도 global 이라는 명령을 통해 지역 변수를 전역 변수의 값으로 통하게 할 수 있다.

# Lambda: 함수를 간단하게 만들어주는 코드
add = lambda a, b: a + b
print(add(1, 3))
# 다른 예시: 리스트
myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](100,200)) # myList에서의 첫 번째 값([0])을 가져와 실행시킨다.

# 사용자 입력과 출력
a = input() # input, print 같은 경우는 내장 함수
print(a) # input은 C언어에서의 scanf와 같은 기능, 값을 입력받을 수 있음 
# 다른 예시
number = input("숫자를 입력하세요: ") # str형 매개변수를 넣음
print(number)

# print문의 심화
print("life" "is" "too short") # ,(콤마)도 없음
print("life", "is", "too short") # ,(콤마)를 넣으면 띄어쓰기가 작동됨

#  파일 읽고 쓰기
# f = open("새파일.txt", 'w') # 'w'는 쓰기 모드
# f.close()
#  이걸 실행시키면 좌측에 새로운 파일(새파일)이 생성된다.
# 예시(파일이 만들어지는 것을 방지해 전부 주석처리)
# f = open("C:\hwannniPY/새파일.txt", 'w', encoding="UTF-8") # C:\hwannniPY로 절대 경로로 만듦, encoding="UTF-8: 한글이 안깨짐
# for i in range(1, 11):
#     data = "%d번재 줄입니다. \n" % i
#     f.write(data) # f이라는 변수에 write이라는 함수를 적용
# f.close()

# 읽기모드: readline
# f = open("새파일.txt", 'r', encoding="UTF-8")
# line = f.readlint() # 파일을 한 줄을 읽어와서 변수 line에 넣어준다.
# print(line)
# f.close
# # 모든 줄을 읽기 위해선
# f = open("새파일.txt", 'r', encoding="UTF-8")
# while True: # while문을 통해 readline이 한 줄이 아닌 모든 줄을 읽게 한다.
#     line = f.readline()
#     if not line: break # not line: 라인이 없으면 break!
#     print(line)
# f.close()
# readline이 아닌 readlines를 이용해서 모든 줄을 읽을 수도 있다.
# 읽기모드: read (readline이랑 다른거!) read는 통째로 읽는 것
# f = open("새파일, txt", 'r', encoding="UTF-8")
# data = f.read()
# print(data)
# f.close()

# 추가모드: 'a'- 기존의 내용은 그대로 놔두고 새로운 내용을 추가할때 사용한다.
# f = open("새파일.txt", 'a', encoding="UTF-8") 
# for i in range(11, 20): # 아까 있던 range(1,11) 이후에 range(11,20,) 내용이 추가된다.
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 매번 close 하지 않는 방법: with문과 함께 사용하기
# with open("foo.txt", "w") as f: # with~as 를 통해 f에 넣는다는 의미
#     f.write("Life is too short, you need python")
# 지역 변수의 개념이 적용되서 별도의 close 없이 자동으로 닫힌다.