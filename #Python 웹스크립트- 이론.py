#Python 웹스크립트- 이론
#2022-01-10

# Python Course 첫 번째 과제
# 7가지 함수 만들기
# plus, minus, times, division, negation, power, reminder

def plus(a, b): 
  return (int(a) + int(b))
def minus(a, b):
  return (int(a) - int(b))
def times(a, b):
  return (int(a) * int(b))
def division(a, b):
  return (float(a) / float(b))
def negation(a):
  return (int(-a))
def power(a, b):
  return (float(a) ** float(b))
def reminder(a, b):
  return (float(a) % float(b))

print(plus(240,500))
print(minus(240,"500"))
print(times(240,500))
print(division(240,500))
print(negation(240))
print(power(2,5))
print(reminder("240","500"))

### 인자들에게 int, float를 붙여줌으로써 문자열이 들어가도 숫자형으로 변형되어 계산되게끔 설계.

# input을 이용한 더 깔끔한 계산기
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

def Cal(a, b):
  return a+b, a-b, a*b, a/b, -a, a**b, a%b

print(Cal(a,b))

# 음주가 가능한 나이 if, elif, else 사용
def age_check(age): # agd를 인자로 넣음
  print(f"you are {age}") # 먼저 you are {age}를 프린트
  if age < 18:
    print("you can't drink") # age값이 18 미만이면 you can't drink를 출력
  elif age == 18: #else if
    print("you are new to this!") # age값이 18면 you are new to this!를 출력
  elif age > 20 and age < 25:
    print("you are still kind of young") # age값이 20 초과 25 미만이면 you are still kind of young를 출력
  else:
    print("enjoy you are drink") # 위의 조건들이 모두 False 라면 else구문 수행


age_check(23) # age인자에 23이라는 값을 넣었기 때문에 you are still kind of young 출력