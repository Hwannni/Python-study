import os
os.system('cls')

# 주어진 리스트에서 각 아이템이 몇개씩 등장했는지 세는 함수를 구현하려고 합니다.
# 이 함수는 리스트 변수를 입력으로 받고 딕셔너리를 출력하는데, 
# 딕셔너리의 각 쌍의 키는 아이템이고 값은 해당 아이템이 출현한 횟수입니다.
# 파이썬의 기본 기능 외의 라이브러리를 쓰지 않고 구현해 주세요.


def count(data):
#   raise NotImplementedError # 이 부분을 구현해 주세요.
    count_data = {}
    for new_data in data:
        if new_data not in count_data:
            count_data[new_data] = 1
        else:
            count_data[new_data] += 1
            # print(count_data)
  
    return count_data



# 데이터와 테스트 코드는 수정하지 마세요.

assert count(["A", "B", "C"]) == {"A": 1, "B": 1, "C": 1}
assert count(["A", "A", "B", "C", "C", "C"]) == {"A": 2, "B": 1, "C": 3}
assert count(["D", "A", "D", "B", "C", "A", "C"]) == {"A": 2, "B": 1, "C": 2, "D": 2}