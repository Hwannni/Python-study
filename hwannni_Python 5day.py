#Python 5day
#2022-01-09

# # 클래스: 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀
# # 클래스를 이용한 계산기
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self,num):
#         self.result += num
#         return self.result

# cal1 = Calculator() # 클래스를 변수에 넣는다.
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(5))
# print(cal2.add(3))
# print(cal2.add(100))

# 클래스를 이용한 계산기
class FourCal:
    def __init__(self, first, second): # __init__: 클래스를 처음 만들때 무조건 처음으로 수행하게 됨.
        self.first = first
        self.second = second
    def setdata(self, first, second): # setdata라는 함수를 FourCal이라는 클래스에 설계
        self.first = first
        self.second = second
    def add(self): # aㅇㅇ라는 함수를 FourCal이라는 클래스에 설계
        result = self.first + self.second # setdata 함수에 first와 second를 정의 시켰고, 그 식을 add에서 그대로 이어받아 사용함.
        return result # 윗줄 first와 second를 더하는 result의 값을 return 시킨다.

a = FourCal(1, 2)
