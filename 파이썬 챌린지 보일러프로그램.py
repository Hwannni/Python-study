import requests
import os

print ("Welcome to My_replit_page.py!\nPlease write a URLs you want to check. (separated by comma)")


while True:
  User_URL = input()
  split_url = User_URL.split(",")
  # print(a)
  for url in split_url:
    url = url.strip()
    url = url.lower()

    if ".com" not in url and ".co.kr" not in url and ".net" not in url and ".org" not in url and ".io"not in url:
      print(f"{url} is not vaild")
      continue

    if "http://" not in url and "https://" not in url:
      url = "http://" + url

    

    try:
      result = requests.get(url)
      URL_status = result.status_code
      if URL_status == 200:
        print(f"{url} is up!")
    except requests.exceptions.HTTPError:
      print(f"{url} is down!")
    except requests.exceptions.ConnectionError:
      print(f"{url} is down!")
    except requests.exceptions.Timeout:
      print(f"{url} is down!")
    except requests.exceptions.RequestExecption:
      print(f"{url} is down!")
    
    

  while True:
    user_say = str(input("Do you want to start over? y/n: "))
    if user_say == "y" or user_say == "n":
        break
    else:
        print("That's not a vaild answer.")
  if user_say == "y":
    os.system('clear')
    print ("Welcome to My_replit_page.py!\nPlease write a URLs you want to check. (separated by comma)")
  else:
    print("k.bye")
  
    break
