####Birth Day###

from datetime import datetime
from datetime import date
import time
today = date.today()
def user_birthday():
    year = int(input('Enter Your Birthday[YY] '))
    month = int(input('Enter Your Birthday[MM] '))
    day = int(input('Enter Your Birthday [DD] '))
    birthday = datetime(year, month, day)
    return birthday

def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday


bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
h = int(days)*24
print(f"The Next Birthday is in {days} days, {h} hours and {h*60} minutes {h*60*60} seconds left")


#####Output###

Enter Your Birthday[YY] 1999
Enter Your Birthday[MM] 08
Enter Your Birthday [DD] 19
The Next Birthday is in 305 days, 7320 hours and 439200 minutes 26352000 seconds left


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
