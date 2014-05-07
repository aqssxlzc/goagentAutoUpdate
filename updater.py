import urllib2
import psutil
import logging
import os
import re
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
goagentPath=""
goagentFolderPattern = "goagent"
pattern=re.compile(goagentFolderPattern)
for filename in os.listdir(localpath):
	if pattern.match(filename)!=None:
		goagentPath=localpath+"\\"+filename
		print  goagentPath
    
#2.check if goagent runing
hasGoagentRunning=False;
for pid in psutil.pids():
	try:
		info = psutil.Process(pid)
		if info.name()=='goagent.exe':
			hasGoagentRunning=True
			logging.warning('running goagent detected')
			break
	except:
		pass

#2.1 if not running then start local goagent 
if hasGoagentRunning==False and goagentPath!="":
	import subprocess
	subprocess.Popen(goagentPath+"\\local\\goagent.exe")
#3.check goagent update using proxy
#3.1 visit goagent site via proxy
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
link= urllib2.urlopen('https://goagent.googlecode.com/archive/3.0.zip')
#link= urllib2.urlopen('https://baidu.com')
import cgi
_, params = cgi.parse_header(link.headers.get('Content-Disposition', ''))
 
filename = params['filename']
import urllib
urllib.urlretrieve ('https://goagent.googlecode.com/archive/3.0.zip',filename)
#print link.read()
#3.2 get local goagent version
def getLocalGAEVersion(path):
	return
	
#3.3 get remote goagent version
def getRemoteGAEVersion():
    return ""
#3.4 if new version released goto update
#4. do update
def updateGAE():
    return
#4.1 download goagent package via proxy
#4.2 extract downloaded package
#4.3 get local goagent config info
#4.4 immigrate local info to new package
#4.5 stop running goagent
#4.6 start new goagent
#4.7 delete old goagent


