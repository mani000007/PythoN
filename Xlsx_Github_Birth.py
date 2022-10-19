####Birth Day###


from datetime import datetime
from datetime import date
import time
today = date.today()


def user_birthday():
    year = int(input("Year[YY]: "))
    month = int(input("Month[MM]: "))
    day = int(input("Day[DD]: "))
    birthday = datetime(year, month, day)
    return birthday


def calculate_dates(birthday):
    today = date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1,day=birthday.day+1)
        return birthday
    elif birthday == today:
        birthday = birthday.replace(year=today.year, day=birthday.day)
        return birthday
    elif birthday > today:
        birthday = birthday.replace(year=today.year, day=birthday.day-1)
        return birthday

    else:
        return birthday


Birthday = user_birthday()
t = calculate_dates(Birthday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
current_time = datetime.now()
present = current_time.hour
hours = (24 - present)
m = current_time.minute
s = current_time.second
minutes = 60 - m
seconds = 60 * 60 - s
print(f"The Next Birthday is in {days} days {hours} hours {minutes} minutes and {seconds} Seconds")

#####Output###

Year[YY]: 1999
Month[MM]: 08
Day[DD]: 19
The Next Birthday is in 305 days 8 hours 30 minutes and 3588 Seconds



#####---GITHUB API---#####



import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint

username = input("Enter the github username:")

g = Github()
user = g.get_user(username)

for repo in user.get_repos():
    print(repo)

request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0, len(json)):
  print("Project Number:", i+1)
  print("Project Name:", json[i]['name'])
  print("Project URL:", json[i]['svn_url'], "\n")

    
   
####---OUTPUT---####

E:\mani>python main.py
Enter the github username:mani000007
Repository(full_name="mani000007/All_in_one")
Repository(full_name="mani000007/example-voting-app-kubernetes")
Repository(full_name="mani000007/gith")
Repository(full_name="mani000007/git_files")
Repository(full_name="mani000007/ignorefiles")
Repository(full_name="mani000007/mani")
Repository(full_name="mani000007/manik")
Repository(full_name="mani000007/manimk")
Repository(full_name="mani000007/Mconflict")
Repository(full_name="mani000007/mgit")
Repository(full_name="mani000007/mkr")
Repository(full_name="mani000007/myPython")
Repository(full_name="mani000007/play-with-docker")
Repository(full_name="mani000007/pull-request-demo")
Repository(full_name="mani000007/pyPrograms")
Repository(full_name="mani000007/Rebase")
Repository(full_name="mani000007/reponew")
Repository(full_name="mani000007/revertgit")


Project Number: 1
Project Name: All_in_one
Project URL: https://github.com/mani000007/All_in_one

Project Number: 2
Project Name: example-voting-app-kubernetes
Project URL: https://github.com/mani000007/example-voting-app-kubernetes

Project Number: 3
Project Name: gith
Project URL: https://github.com/mani000007/gith

Project Number: 4
Project Name: git_files
Project URL: https://github.com/mani000007/git_files

Project Number: 5
Project Name: ignorefiles
Project URL: https://github.com/mani000007/ignorefiles

Project Number: 6
Project Name: mani
Project URL: https://github.com/mani000007/mani

Project Number: 7
Project Name: manik
Project URL: https://github.com/mani000007/manik

Project Number: 8
Project Name: manimk
Project URL: https://github.com/mani000007/manimk

Project Number: 9
Project Name: Mconflict
Project URL: https://github.com/mani000007/Mconflict

Project Number: 10
Project Name: mgit
Project URL: https://github.com/mani000007/mgit

Project Number: 11
Project Name: mkr
Project URL: https://github.com/mani000007/mkr

Project Number: 12
Project Name: myPython
Project URL: https://github.com/mani000007/myPython

Project Number: 13
Project Name: play-with-docker
Project URL: https://github.com/mani000007/play-with-docker

Project Number: 14
Project Name: pull-request-demo
Project URL: https://github.com/mani000007/pull-request-demo

Project Number: 15
Project Name: pyPrograms
Project URL: https://github.com/mani000007/pyPrograms

Project Number: 16
Project Name: Rebase
Project URL: https://github.com/mani000007/Rebase

Project Number: 17
Project Name: reponew
Project URL: https://github.com/mani000007/reponew

Project Number: 18
Project Name: revertgit
Project URL: https://github.com/mani000007/revertgit
