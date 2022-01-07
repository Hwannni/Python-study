#Python 2day-3
#2022-01-06
# 점프 투 파이썬 2장 연습문제

#1. 홍길동 씨의 평균 점수를 구해보자.
a = 80
b = 75
c = 55
print((a+b+c)/3)

#2. 슬라이싱 활용
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd) # 881120 출력
print(num) # 1068234 출력

#3. 인덱싱 활용
pin = "881120-1068234"
print(pin[7])

#4. replece 활용
a = "a:b:c:d"
b = a.replace("a:b:c:d", "a#b#c#d")
# b = a.replace(":", "#") 사용 가능
print(b)

#5. 내장 함수 사용
a = [1, 3, 5, 4 ,2]
a.sort()
print(a)
a.reverse()
print(a)

#6. join 사용
a = ['Life', 'is', 'too', 'short']
result= " ".join(a) # " "를 넣어야지 각 문자열마다 공백이 생긴다.
print(result)

#7. 더하기 사용
a = (1,2,3)
a = a + (4,)
print(a)

#8. 딕셔너리 pop함수
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') # pop으로 B의 value를 추출
print(a)
print(result)

#9. 중복 숫자 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)