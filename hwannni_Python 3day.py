#Python 3day
#2022-01-07

# 조건문(if문)
money = True # 만약 False라면 else구문이 시행
if money: # 판단할 조건- ':'을 꼭 써줘야 한다.
    print("택시를 타고 가라")
else:
     print("걸어 가라")
# if문 에서 중요한 것은 들여쓰기(tab)다.
# 비교 연산자를 사용한 예시
a = 1
b = 2
if a< b:
    print("참")
else:
    print("거짓")

# if문 다른 예시
money = 2000
card = 1 # 1은 참이다.
if money >= 3000 or card: # money는 False지만 card가 1이므로 True의 값이 나온다.
    print("지하철을 타고 가라")
else:
    print("걸어가라")
# 조건문에서 아무 일도 하지 않게 설정하려면?: pass를 넣으면 된다.

#다중 조건 판단: elif (다른 언어에서는 else if를 사용)
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("자전거를 타고 가라")
else:
    print("걸어가라")

# 조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
#위의 식을 조건부 표현식을 통해 한줄로 표현 가능
message = "success" if score >= 60 else "failure"
print(message)

# 반복문(while문)
treeHit = 0
while treeHit < 10: # False가 나올때까지 반복
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee: # not coffee 이므로 coffee의 숫자가 다 떨어져야 True로 인식되어 print문으로 진행된다.
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # money에는 아직 돈이 들어있지만 break로 인해 while문을 빠져나간다.

# continue
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: # 짝수 확인 조건문
        continue # continue를 만나게 되면 아래로 가지 않고 while문으로 되돌아간다.
    print(a) # 즉, 홀수만 출력된다.

# 무한루프
#while True: # True가 입력되고 break가 없으면 무한대로 반복된다.
    print("안녕하세요")
# Ctrl+c 를 눌러서 정지할 수 있다.

# 반복문(for문)
test_list = ['one', 'two', 'three']
for i in test_list: # 리스트에 있는 요소들을 하나씩 꺼내 변수 i에 넣고 print 한다.
    print(i)

# 다양한 예시
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
# continue는 while문과 동일한 개념: continue를 만나면 아래로 내려가지 않고 for문으로 되돌아간다.
# break도 동일하다

# range 함수
sum = 0
for i in range(1,11): # 1 이상 11 미만을 의미
    sum = sum + i
print(sum)

# 구구단(이중 for문)
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('') 