#Python 5day
#2022-01-09

# 클래스: 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀
# 클래스를 이용한 계산기
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator() # 클래스를 변수에 넣는다.
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(5))
print(cal2.add(3))
print(cal2.add(100))

# 클래스를 이용한 계산기
class FourCal:
    #생성자: __init__
    def __init__(self, first, second): # __init__: 클래스를 처음 만들때 무조건 처음으로 수행하게 됨.
        self.first = first
        self.second = second
    def setdata(self, first, second): # setdata라는 함수를 FourCal이라는 클래스에 설계
        self.first = first
        self.second = second
    def add(self): # add라는 함수를 FourCal이라는 클래스에 설계
        result = self.first + self.second # setdata 함수에 first와 second를 정의 시켰고, 그 식을 add에서 그대로 이어받아 사용함.
        return result # 윗줄 first와 second를 더하는 result의 값을 return 시킨다.

# a = FourCal(1, 2) # __init__으로 인해 first에는 1, second에는 2가 코드 실행시 생성자로 삽입되고 시작한다.

# 상속: 기존 만들어놓은 클래스에 추가 기능을 넣어서 새로이 만드는 것
# ex. 기본 계산기에 상속을 하여 공학용 기능을 만들 수도 있다.
# 상속의 예
class MoreFourCal(FourCal): # 괄호 안에 부모클래스(FourCal)를 넣으면 그 부모클래스의 기능을 그대로 사용하면서 상속받은 자식클래스는 만들게 된다.
    pass # 상속의 예시를 위해 별다른 기능 추가없이 pass 사용

a = MoreFourCal(4, 2)
print(a.add())
# 부모클래스인 FourCal의 기능을 그대로 상속받은 MoreFourCal은 클래스 선언 후 pass만 했지만
# 부모클래스의 기능을 그대로 수행할 수 있어 4 + 2 = 6이 나오게 된다.

