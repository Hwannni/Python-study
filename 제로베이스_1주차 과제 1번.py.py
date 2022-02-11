import os
os.system('cls')

def process_data(data):
#   raise NotImplementedError # 이 부분을 작성해 주세요.
    data_list = []
    for new_data in data:
        weather_data = new_data[:-8]
        # print(weather)
        date_data = new_data[-8:]
        # print(date)
        dict_data= {'weather': weather_data, 'date': date_data}
        data_list.append(dict_data)
        print(data_list)
    return data_list


# 데이터와 테스트 코드는 수정하지 마세요.
raw_data = ['Sunny20210101', 'Rainy20210102', 'Cloudy20210103']
processed_data = [{'weather': 'Sunny', 'date': '20210101'}, {'weather': 'Rainy', 'date': '20210102'}, {'weather': 'Cloudy', 'date': '20210103'}]

assert process_data(raw_data) == processed_data