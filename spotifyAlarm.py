from datetime import datetime
from threading import Timer
from os import system
import webbrowser
new = 2 # open in a new tab, if possible



x=datetime.today()
y=x.replace(day=x.day+1, hour=7, minute=30, second=0, microsecond=0)
delta_t=y-x

	
secs=delta_t.seconds+1
while 1:
	print "Enter URL to open at", str(y),
	url = raw_input(":")
	confirm = raw_input("Please enter 'confirm' to confirm URL: ")
	if confirm.upper() == "CONFIRM":
		break
def alarm():
	system("cls")
	print "The time is", str(y) + ". Opening", url, "..."
	webbrowser.open(url,new=new)
	raw_input("Press ENTER to close program. Built by Alex Dawkins")

t = Timer(secs, alarm)
t.start()
system("cls")
print "Alarm Set.\n\n" +  url, "will open at", str(y)
