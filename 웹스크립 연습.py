import requests # requests라는 라이브러리 이용(패키지 설치해야 가능)
from bs4 import BeautifulSoup # beautifulsoup4라는 라이브러리 이용


# indeed 웹페이지 링크 정의
# requests.get이라는 함수 사용
indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")

# indeed 웹페이지의 HTML 정보를 긁어오는 단계- text를 붙여준다.
# print(indeed_result.text)

# 긁어온 HTML에서 정보를 가져와야 한다.(페이지 숫자들): beautifulsoup 패키지 다운(완료)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})

# print(pagination)

pages = pagination.find_all('a')

# print(pages)

spans = []
for page in pages:
  spans.append(page.find("span"))
print(spans[:-1]) # 마지막 요소를 제외(슬라이싱) 