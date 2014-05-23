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
import subprocess
import ConfigParser

def startgae():
    subprocess.Popen(goagentPath + "\\local\\goagent.exe")
#3.check goagent update using proxy
#3.1 visit goagent site via proxy
def getGAE():
    #proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    #opener = urllib2.build_opener(proxy)
    #urllib2.install_opener(opener)
    link = urllib2.urlopen('https://goagent.googlecode.com/archive/3.0.zip')
    import cgi
    _, params = cgi.parse_header(link.headers.get('Content-Disposition', ''))
    filename = params['filename']
    import urllib
    print "Save goagent pack in "+localpath+filename
    urllib.urlretrieve('https://goagent.googlecode.com/archive/3.0.zip', localpath+filename)
    return localpath+filename


#print link.read()
#3.2 get local goagent version
def getLocalGAEVersion(path):
    filepath = path + "\\local\\proxy.py"
    versionlinePattern = re.compile("__version__ = \'.+\'")
    with open(filepath) as file:
        for line in file:
            if versionlinePattern.match(line) is not None:
                return line.replace('__version__ = \'','').replace('\'','')

def getremoteversion():
    goagenturl="https://code.google.com/p/goagent/"
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    link = urllib2.urlopen(goagenturl)
    html= link.read()
    pattern = re.compile('goagent \d+.\d+.\d+')
    resultstr= pattern.search(html).group()
    if resultstr is not None:
        return resultstr.replace('goagent','').lstrip()

#3.3 get remote goagent version


#3.4 if new version released goto update
#4. do update
def updateGAE(oldpath, newpath):
    if checkGAERunning():
        info = checkGAERunning()
        info.kill()
    return


def getGAEconf(path):
    file = open(path + "//local//proxy.ini",'r')
    for line in file:
        match = re.compile("appid =.+").match(line)
        if match:
            return match.group().replace("appid =","")



def versioncmp(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return cmp(normalize(version1), normalize(version2))

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
    goagentFolderPattern = "goagent-[^zip]+"
    pattern = re.compile(goagentFolderPattern)
    for filename in os.listdir(path):
        if pattern.match(filename) is not None:
            if '.' not in filename:
                return  localpath + filename

def appid2conf(ids,path):
    with open(path+"\\local\\proxy.ini","r+") as file:
        content = file.read()
        content= content.replace("appid = goagent","appid ="+ids)
        print content
        file.seek(0)
        file.write(content)

def initConfig(gaepath):
    config = ConfigParser.RawConfigParser()
    config.add_section('BaseSetting')
    config.set('BaseSetting', 'gaepath', gaepath)
    with open(os.path.expanduser("~")+'//gae.cfg', 'wb') as configfile:
        config.write(configfile)


#1.get local goagent path
localpath = os.path.expanduser("~")
logging.warning('goagent path is ' + localpath)
goagentPath = findgaepath(localpath)
if goagentPath is not None:
    print "Find Goagent in path "+goagentPath

localversion = getLocalGAEVersion(goagentPath)
print "Local Version is "+localversion

remoteversion = getremoteversion()
print "Remote Version is "+remoteversion
#2.check if goagent runing

retry=0
if versioncmp(localversion,remoteversion):
    print "New version detected"
    while retry <10:
        retry+=1
        try:
           newgaefile=getGAE()
           break
        except:
            print "Download error, retry "+str(retry)+" times."
            continue
    subprocess.call("7za x "+newgaefile+" -o"+localpath)
else:
    print "exit"
    exit()

newversionpath = localpath+newgaefile.split(".")[0].split("\\")[-1]

appids = getGAEconf(localversion)
print "local appids is "+appids
appid2conf(appids,newversionpath)

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


