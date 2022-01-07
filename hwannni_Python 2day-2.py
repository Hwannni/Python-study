#Python 2day-2
#2022-01-06

# 튜플 자료형- 리스트와 거의 유사
# 튜플은 ()로 둘러싼다.
# 리스트는 그 값의 생성/삭제/수정이 가능하지만 튜플은 불가능
t = (1,2,3,4,5)
print(t)

# 튜플 인덱싱과 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[0]) # 튜플 t1의 첫 번째 값 인덱싱
print(t1[3]) # 튜플 t1의 네 번째 값 인덱싱
print(t1[1:]) # 튜플 t1[1]부터 끝까지

# 튜플 더하기, 곱하기, 길이 구하기
x = (3, 4)
y = (5 ,6)
print(x + y) # x와 y의 값이 붙어서 나온다.
print(x * 6) # x의 값이 6번 반복
print(len(y)) # y의 길이가 출력

# 딕셔너리 자료형: {}로 둘러싼다.
dic = {'name' : 'jhon', 'age' : '26', 'phone' : '010-1122-3344'}
print(dic)

# 딕셔너리 쌍 추가, 삭제하기
a = {'1': 'a'}
a['name'] = '익명' # a에 'name':'익명' 쌍이 추가됐다.
print(a)

del a['1'] # a에 '1'이라는 키값에 해당되는 쌍이 삭제
print(a)

# 딕셔너리에서 Key 사용해 Value 얻기
number = {"민우" : 100, "선호" : 999}
print(number["민우"]) # 민우가 가진 value 100이 출력된다.

# 딕셔너리에서 Key 리스트 만들기, Value 리스트 만들기
a = {'name' : 'pey', 'phone' : '010-4455-2997', 'birth' : '1115'}
print(a.keys()) # a의 key만을 모아서 객체를 돌려준다.
print(a.values()) # a의 value만을 모아서 객체를 돌려준다.

# items, clear, get 사용하기
print(a.items()) # 쌍 얻기
print(a.get('phone')) # get을 이용하여 phone의 values 얻기
a.clear() # 쌍 모두 지우기 {}이 출력된다.
print(a)

# 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
a = {'name' : 'min', 'adress' : 'Korea', 'phone' : '010-1122-3344'}
print('name' in a) # 딕셔너리 안에 name 가 있어서 True를 출력
print('birth' in a) # 딕셔너리 안에 birth가 없어서 False 출력

# 집합 자료형: set 키워드를 사용
s1 = set([1,2,3]) # set 키워드 안에 리스트 입력
print(s1)

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) # &는 교집합
print(s1 | s2) # | 는 합집합
print(s1 - s2) # - 는 차집합

# 불 자료형: True와 False를 나타내는 자료형
a = True
b = False
print(type(a)) # type을 이용하여 a가 불자료형인지 확인
print(1 == 1) # 1과 1이 같은가? 라는 조건문은 참이므로 True 출력
print(2 < 1) # 2는 1보다 작은가? 라는 조건문은 거짓이므로 False가 출력

# 변수: 자료형 값을 저장하는 공간
a = 1 
b = "python"
c = [1,2,3]
# '=' 기호를 사용하여 변수를 만든다.

a = [1,2,3]
b = a
print(id(a))
print(id(b)) # 변수 b에 변수 a를 대입했고 id 함수를 통해 id(a)와 id(b)의 값이 같다는 것을 확인
print(a is b) # 즉, a와 가 같다.

# 여기서 a의 요소를 바꾸면 b는 어떻게 될까?
a[1] = 4
print(a)
print(b) # a의 요소를 바꿨는데 b의 요소도 바뀌었다.
# a와 b가 같은 주소를 가리키기 때문에 이와 같은 일이 발생
# 그렇다면 다른 주소를 가르키도록 하는 방법이 있는가?
# [:] 사용, copy 모듈 사용이 있다
a = [1,2,3]
b = a[:] # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a)
print(b) # 변수 b의 값은 변하지 않은 것을 볼 수 있다.

from copy import copy
a = [1,2,3]
b = copy(a)
print(b is a) # b is  a의 값이 위와 다르게 False가 나왔다. 
# b와 a가 가르키는 객체가 서로 다르다는 것을 의미