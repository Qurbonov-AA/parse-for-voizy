from bs4 import BeautifulSoup
import requests as r
import json
texts = []
link = []
voizy = {}

# file save or update
def file_save(url):
    global link
    global texts
    global voizy
    voizy[url] = {"links" : [], "names" : []}
    for item in link:
        voizy[url]["links"].append(item)
    for item in texts:
        voizy[url]["names"].append(item)
    with open('texts.json','w',encoding="utf-8") as f:
        json.dump(voizy,f)        
    link = []
    texts = []

# open file 
def file_open():
    with open('texts.json','r',encoding="utf-8") as f:
        voizy = json.load(f)
        print(voizy.keys())

#get link for mp3 in site
def find_link(slink):
    global link 
    if (len(slink) > 0):
        for item in slink:
            sitem  = str(item)
            lindex  = sitem.find("play")
            nindex =int(lindex)+6
            link.append('https://www.myinstants.com'+sitem[nindex:-10])
    

# get text for search        
def get_names(names):
    global texts
    if (len(names) > 0):
        for item in names:
            texts.append(item.getText())
    
    
        

# get url adres site 
def get_urls():
    for item in range(1,300):
        html = r.get('https://www.myinstants.com/index/us/?page='+str(item))
        soup = BeautifulSoup(html.text,'html.parser')
        error = soup.find("div",{"id" : "instants_container"})
        #print(error)
        if (error != None):
            divs = soup.find("div",{"id" : "instants_container"})
            names = divs.find_all("a" , {"class" : "instant-link"})
            links = divs.find_all("div", {"class" : "small-button"})
            find_link(links)
            get_names(names)
            file_save('https://www.myinstants.com/index/us/?page='+str(item))
            
        else:
            break

#html = r.get('https://www.myinstants.com/categories/games/')



#file_open()
get_urls()


