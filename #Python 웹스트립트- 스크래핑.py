#Python 웹스트립트- 스크래핑
#2022-01-10

import requests

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=100&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")
print(indeed_result)