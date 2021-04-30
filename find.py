from json import dump,load
import nltk
import telebot
import time 

voizy = {}

bot = telebot.TeleBot("1242724893:AAFDauEH7EOOAQLEojulFOtH0hW6NkRomGM", parse_mode=None)




def filter(text):
    text = text.lower()
    text = [c for c in text if c in '1234567890abdefghijklmnopqrstuwvxzйцукенгшщзхъфывапролджэячсмитьбюё -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    return text



def find_link(intent,item):
    indeks = []
    for i,x in enumerate(voizy[intent]["names"]):
        x = filter(x)
        if x == item:
            print(voizy[intent]["links"][i])
            indeks.append(voizy[intent]["links"][i])
    return indeks


def file_open():
    global voizy
    with open('texts.json','r',encoding='UTF8') as f:
        voizy = load(f)
        


def find_in_voizy(text):
    global voizy
    file_open()
    text = filter(text)
    for find,value in voizy.items():
           for item in value["names"]:
               item = filter(item)
               
               if (len(item) > 0):
                   distance = nltk.edit_distance(text,item)/len(item)
                          
               if (item == text or distance <= 0.3):
                   print(f' siz izlagan suz {text} manashu url da {find} va shu item - {item} va shuncha yaqinlikda {distance}')
                   return find_link(find,item)
                   

def send_audio(mid,link):
    bot.send_audio(mid,link)   


                    
@bot.message_handler(content_types=['text'])

def answer_by_text(message):
    links = []
    links = find_in_voizy(message.text)
    print(links)
    for link in links:
        #audio = open(link, 'rb')
        send_audio(message.chat.id,link)
        time.sleep(5)
         
        
    
    
    




bot.polling()







