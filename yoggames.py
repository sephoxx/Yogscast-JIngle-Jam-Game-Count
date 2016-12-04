import requests
from bs4 import BeautifulSoup
from datetime import datetime


class bcolors:
	OKBLUE = '\033[94m'
	ENDC = '\033[0m'

def TimePrint(c_time, t_left):
	print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]"
	print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]TIME UNTIL NEXT GAME(S) UNLOCKS: "+ bcolors.OKBLUE + "%s"%(t_left) + bcolors.ENDC +" hours and "+ bcolors.OKBLUE + "%s"%(60 - c_time.minute) + bcolors.ENDC +" minutes"
	print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]"

url = 'http://www.humblebundle.com/yogscast-jingle-jam'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

links = soup.find_all("span",{"class":"game-box"})

i = 0

print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]GAMES CURRENTLY IN THE YOGSCAST JINGLE JAM:"
print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]"

for link in links:
	child = str(links[i])
	child = BeautifulSoup(child, 'lxml')
	if child.find_all("img"):
		for kid in child.find_all("img"):
			if kid.get("alt") != "":
				i += 1
				print "["+ bcolors.OKBLUE + "*" + bcolors.ENDC +"]%s. %s" %(i, kid.get("alt") )
	else:
		i += 1


current_time = datetime.utcnow().time()
if current_time.hour >= 17:
	time_left = (24+16) - current_time.hour
	TimePrint(current_time, time_left)
else :
	time_left = 17 - current_time.hour
	TimePrint(current_time, time_left)
