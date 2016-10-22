from bs4 import BeautifulSoup
import urllib2
from itertools import izip
import sys
url1='http://www.espncricinfo.com/ci/engine/match/index.html?view=live'


def check_internet():
    try:
        response=urlib2.urlopen(url1,timeout=20)
        return true
    except urlib2.URLError as err: pass
    return false

def crickinfo():
    res=check_internet()
    if(!res):
        print("Please check the internet connection. Either slow or not connected")
        return
    cricfile=urllib2.urlopen(url1)
    crichtm=cricfile.read()
    cricfile.close()
    soup=BeautifulSoup(crichtm,'html.parser')
    a=soup.find_all('div',attrs={'class':'innings-info-1'})
    b=soup.find_all('div',attrs={'class':'innings-info-2'})
    m=[]
    for result in a:
        m.append(result.text)
    n=[]
    for res in b:
        n.append(res.text)
    matches=dict(izip(m,n))
    print("{" + "\n".join("{} {}".format(k.strip(), v.strip()) for k, v in matches.items()) + "}")
    return "{" + "\n".join("{} {}".format(k.strip(), v.strip()) for k, v in matches.items()) + "}"

def footballinfo():
    res=check_internet()
    if(!res):
        print("Please check the internet connection. Either slow or not connected")
        return
    goalfile=urllib2.urlopen('http://www.livegoals.com/')
    goalhtm=goalfile.read()
    goalfile.close()
    soup=BeautifulSoup(goalhtm,'html.parser')
    score=soup.find_all('div',{'class':'score-bullet'})
    sc=[]
    for i in score:
        sc.append(i.text)
    home=soup.find_all('a',{'class':'home-name'})
    h=[]
    for j in home:
        h.append(j.text)
    aw=[]
    away=soup.find_all('a',{'class':'away-name'})
    for k in away:
        aw.append(k.text)
    print("{" + "\n".join("{} {} {}".format(i,j,k) for i,j,k in zip(sc,h,aw)) + "}") 
    #print ["{"+"\n".join("{}" "{}" "{}".format(str(i),str(j),str(k)) for i,j,k in zip(sc,h,aw))+ "}"]    
    return "{" + "\n".join("{} {} {}".format(i,j,k) for i,j,k in zip(sc,h,aw)) + "}"
    
def main():
    arguments=sys.argv[1]
    if (arguments) == 'c':
        crickinfo()
    if (arguments) == 'f':
        footballinfo()

if __name__ == '__main__':
    main()
        
        
    
