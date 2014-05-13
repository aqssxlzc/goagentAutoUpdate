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

import urllib2
import psutil
import logging
import os
import re


def startgae():
    import subprocess
    subprocess.Popen(goagentPath + "\\local\\goagent.exe")
#3.check goagent update using proxy
#3.1 visit goagent site via proxy
def getGAE():
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    link = urllib2.urlopen('https://goagent.googlecode.com/archive/3.0.zip')
    import cgi
    _, params = cgi.parse_header(link.headers.get('Content-Disposition', ''))
    filename = params['filename']
    import urllib
    urllib.urlretrieve('https://goagent.googlecode.com/archive/3.0.zip', filename)


#print link.read()
#3.2 get local goagent version
def getLocalGAEVersion(path):
    filepath = path + "\\local\\proxy.py"
    versionlinePattern = re.compile("__version__ = \'.+\'")
    with open(filepath) as file:
        for line in file:
            if versionlinePattern.match(line) is not None:
                return line


#3.3 get remote goagent version
def getRemoteGAEVersion():
    return ""


#3.4 if new version released goto update
#4. do update
def updateGAE(oldpath, newpath):
    if checkGAERunning():
        info = checkGAERunning()
        info.kill()
    return


def getGAEconf(path):
    file = open(path + "//local//proxy.ini")
    return


def checkGAERunning():
    for pid in psutil.pids():
        try:
            info = psutil.Process(pid)
            if info.name() == 'goagent.exe':
                return info
                break
        except:
            pass
    return False

def findgaepath(path):
    goagentFolderPattern = "goagent-"
    pattern = re.compile(goagentFolderPattern)
    for filename in os.listdir(path):
        if pattern.match(filename) is not None:
            return  localpath + "\\" + filename

#1.get local goagent path
localpath = "C:\\Users\\Administrator"
logging.warning('goagent path is ' + localpath)
goagentPath = findgaepath(localpath)


#2.check if goagent runing

#2.1 if not running then start local goagent
if checkGAERunning() is False and goagentPath != "":
    startgae()


#4.1 download goagent package via proxy
#4.2 extract downloaded package
#4.3 get local goagent config info
#4.4 immigrate local info to new package
#4.5 stop running goagent
#4.6 start new goagent
#4.7 delete old goagent


