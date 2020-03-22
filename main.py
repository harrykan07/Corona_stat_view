from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notMe(title , msg):
    notification.notify(
        title = title,
        message = msg,
        app_icon = '/media/harish/my files/TIme pass folder/CORONA_PY/icon.png',
        timeout = 6
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    myHtmlData = getData('https://www.mohfw.gov.in/')
    #print(myHtmlData)
    soup=BeautifulSoup(myHtmlData ,'html.parser') # parsing html
    #print(soup.prettify()) # to show pretty data
    mydata=""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        mydata += tr.get_text()
    
    mydata=mydata[1:]

    iteml = mydata.split("\n\n")

    states = ['Maharashtra' , 'Kerala' , 'Andhra Pradesh' , 'Telengana']

    for i in iteml[:23]:
        dl = i.split('\n')
        if dl[1] in states:
            nTitle = "Cases of Novel Covid-19"
            nText = f"{dl[1].upper()} ---\n\tIndian Cases : {dl[2]}\n\tForeign Cases : {dl[3]}\n\tCured : {dl[4]}\n\tDeath : {dl[5]}"
            notMe(nTitle , nText)
            time.sleep(5)
    v=iteml[23].split('\n')[1]
    k=iteml[26] 
    te = f"Total number of cases in India : {v}\nDeath Toll : {k}"
    notMe("Overall Statistics",te)

