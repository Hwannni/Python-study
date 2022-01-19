import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def main_alba_company():
  alba_result = requests.get(alba_url)
  alba_soup = BeautifulSoup(alba_result.text, "html.parser")
  pagination = alba_soup.find("div", {"id" : "MainSuperBrand"}).find("ul", {"class":"goodsBox"})
  pages = pagination.find_all("li", {"class":"impact"})

  for page in pages:
    page.get_text()

    company_url = page.find("a", {"class": "goodsBox-info"})['href']
    if "www" not in company_url:
      company_url = company_url + "job/brand/"
    print(company_url)
    company_name = page.find("span", {"class":"company"}).string
    
    print(company_name)
    company = {"url" : company_url, "name" : company_name}
  
    # print(company)
  
    extract_alba_jobs(company)
    view_company(company)
#     # print (type(company))
    

def extract_alba_jobs(company):
  # print(company)
  result = requests.get(company["url"])
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("body").find("tbody").find_all("tr")
  
  jobs = []
  for tr_result in results:
    
    td_result = tr_result.find_all("td", recursive=False)
    if (len(td_result) != 5):
      continue

    place, title, time, pay, date = td_result
    place = place.text.strip().replace('/', '')
    title = title.find("span", {"class": "company"}).text.strip().replace('/', ' ')
    time = time.text
    pay_result = pay.find_all("span")
    pay = pay_result[0].text + " " + pay_result[1].text
    date = date.text

    jobs.append({"place" : place, "title" : title, "time" : time, "pay" : pay, "date" : date,})

  company["jobs"] = jobs
    # print (td_result)
  
  # print(results)

def view_company(company):
  file = open(f"{company['name'].replace('/', ' ')}.csv", mode="w")
  # print(company['name'])
  # return
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  
  for job in company["jobs"]:
    writer.writerow(list(job.values()))

main_alba_company()
