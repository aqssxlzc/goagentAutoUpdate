import urllib2
import psutil
import logging
import os
#1.get local goagent path
#2.check if goagent runing
#2.1 if not running then start local goagent 
#3.check goagent update using proxy
#3.1 visit goagent site via proxy
#3.2 get local goagent version
#3.3 get remote goagent version
#3.4 if new version released goto update
#4. do update
#4.1 download goagent package via proxy
#4.2 extract downloaded package
#4.3 get local goagent config info
#4.4 immigrate local info to new package
#4.5 stop running goagent
#4.6 start new goagent
#4.7 delete old goagent


#1.get local goagent path
localpath="C:\\Users\\Administrator"
logging.warning('goagent path is '+localpath)
for filename in os.listdir(localpath):
    print  filename
#2.check if goagent runing
hasGoagent=False;
for pid in psutil.pids():
	try:
		info = psutil.Process(pid)
		if info.name()=='goagent.exe':
			hasGoagent=True
			logging.warning('running goagent detected')
			break
	except:
		pass

#2.1 if not running then start local goagent 
#3.check goagent update using proxy
#3.1 visit goagent site via proxy
#3.2 get local goagent version
#3.3 get remote goagent version
#3.4 if new version released goto update
#4. do update
#4.1 download goagent package via proxy
#4.2 extract downloaded package
#4.3 get local goagent config info
#4.4 immigrate local info to new package
#4.5 stop running goagent
#4.6 start new goagent
#4.7 delete old goagent


