# 날짜 별, 지역 별 매출 데이터가 있습니다.
# 그런데 매출의 데이터 형식이 문자열로 들어가 있고, 중간에 빠진 값이 있습니다. 
# 매출의 데이터 형식을 숫자형으로 바꾸고 결측치를 제외한 지역 별 평균 매출을 구해보세요.
# Hint: 판다스의 groupby를 사용해 보세요

import pandas as pd
import os
os.system('cls')

def average_by_region(data):
  # raise NotImplementedError # 이 부분을 작성해 주세요.
  data["매출"] = pd.to_numeric(data["매출"])# 데이터프레임에 있는 매출을 숫자형으로 변형
  # pd.to_numeric() : 판다스에서 문자열 칼럼의 숫자형 변환 함수이다.
  new_data = data.groupby("지역").mean().dropna()
  print(new_data)
  
  return new_data["매출"]

  
# 데이터와 테스트 코드는 수정하지 마세요.

raw_data = pd.DataFrame(
    [{"날짜": "20210101", "지역": "서울", "매출": "10"},
     {"날짜": "20210101", "지역": "부산", "매출": "20"},
     {"날짜": "20210101", "지역": "제주", "매출": "8"},
     {"날짜": "20210102", "지역": "서울", "매출": "15"},
     {"날짜": "20210102", "지역": "부산", "매출": None},
     {"날짜": "20210102", "지역": "제주", "매출": "10"}]
  )

result = pd.Series([20.0, 12.5, 9.0], index=['부산', '서울', '제주'])

assert average_by_region(raw_data).equals(result)
 # 판다스 시리즈(Series)의 equals는 두 시리즈의 내용이 같은지 검사한다.