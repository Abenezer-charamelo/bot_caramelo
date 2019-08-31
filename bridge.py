import sendmessage
flag=None
tee=""
onn=""
count = 1
greet_eng = ["hello","hi","good afternoon","good evening","how are you",]
greet_sp = ["hola","bueno dias","como estas"]
ask=["help","info","tell me about you"]
myself=["who are you","what is your name","who is talking","do you have a name","nice to meet you","it is a great pleasure to meet you"]
creator=["who is your boss","who is your creator","who is anon","who is your god","who do you worship","who is your king","who do you love"]
chat_id_request = ["what is my chat id","what is my chat id caramelo"]
"""def info():
    name = cus_array["result"][0]["message"]["from"]["first_name"]
    text= cus_array["result"][0]["message"]["text"]
    if cus_array["result"][0]["message"]["chat"]["type"]=="private":
        id = cus_array["result"][0]["message"]["from"]["id"]
    elif cus_array["result"][0]["message"]["chat"]["type"]=="group":
        id = cus_array["result"][0]["message"]["chat"]["id"]
    info =[id,name,text]
    return info"""

def a(strr):
    global tee
    global count
    for i in range (len(strr)):
        tee = tee + "{}. {}\n".format(count,strr[i])
        count = count + 1
def onnn():
    global onn
    online = open("online.txt","r")
    O_flag= online.read(1)
    online.close()
    if O_flag=="abc":
        onn=input("please replay to {} :----------  ".format(name))
def replay(flag,id,name,txet):
    if flag == 1 :
        txt="{} {}".format(txet,name)
        txt2="{} puedo hablar espanol?".format(name)
        sendmessage.send(id,txt)
        sendmessage.send(id,txt2)
    elif flag == 11 :
        txt ="{} {}".format(txet,name)
        sendmessage.send(id,txt)
    elif flag == 2:
        txt = "I am a bot who serves my user, You !!!!!!!"
        sendmessage.send(id,txt)
    elif flag == 4444:
        ind=txet.index("is")+2
        if txet[-1] in "?./!@#$%^&*():|{}?><":
            txt = "{} Sorry I did not learn that. But I am curious and I want to know What{} is.".format(name,txet[ind:-1])
        else:
            txt = "{} Sorry I did not learn that. But I am curious and I want to know What{} is.".format(name,txet[ind:])
        txt2= "In addition my module to fetch data from google is being developed.... "
        sendmessage.send(id,txt)
        sendmessage.send(id,txt2)
    elif flag == 3 :
        intro = "Type /commands to know the commands I learn till now."
        txt = "Welcome {}".format(name)
        txt2="Nice to meet you"
        sendmessage.send(id,intro)
        sendmessage.send(id,txt)
        sendmessage.send(id,txt2)
    elif flag ==4 :
        txt = "My creator is @csojj.\nHe is my God.\nI worship him every day because I love him very much !!!!!!!!!!"
        sendmessage.send(id,txt)
    elif flag == 0:
        txt = "Sorry I don't understand what you said.\n I am under development, so soon I can understand Most words and punctuation marks too.\nIf you want to support for my development in any way contact my creator @csojj.\nHe will give you my source code for you to edit it."
        if onnn():
            sendmessage.send(id,onn)
        else:
            sendmessage.send(id,txt)
    elif flag == 5:
        txt = "My name is Caramelo, spanish word meaning \"Candy\".\nIt is a great pleasure to meet you {}.\nI hope we will have a great time.".format(name)
        sendmessage.send(id,txt)
    elif flag == 6:
        txt = "Dear {}, your chat id is: {}".format(name,id)
        sendmessage.send(id,txt)
    elif flag == 7:
        a(greet_eng)
        a(greet_sp)
        a(ask)
        a(myself)
        a(creator)
        a(chat_id_request)
        txt = "Additionally you can ask me definition of word like \"Caramelo what is.....?\" if Iknow I will answer it"
        sendmessage.send(id,tee)
        sendmessage.send(id,txt)
    elif flag==8 :
        txt = "it is awesome. Yo tambien puedo hablar pero no mucho...."
        sendmessage.send(id,txt)
    else:
        online = open("online.txt","r")
        O_flag= online.read(1)
        online.close()
        try :
            if O_flag==1 or O_flag=="1":
                txt=input("please replay to {} :----------  ".format(name))
            else:
                txt = "my boss is offline you will get replay as soon as he is back..."
        except:
            txt = "my boss is offline you will get replay as soon as he is back..."
        sendmessage.send(id,txt)
    return txt


def checkmsg(var):
    global flag
    if len(var) > 8 and  var[0:8].lower()=="caramelo":
        flag = 4444
    elif var.lower() in greet_sp:
        flag = 1
    elif var.lower() in ask:
        flag = 2
    elif var=="/start":
        flag = 3
    elif var.lower() in creator:
        flag = 4
    elif var.lower() in myself:
        flag = 5
    elif var.lower() in chat_id_request:
        flag = 6
    elif var == "/commands":
        flag = 7
    elif len(var) > 4 and  var[0:4].lower()=="what":
        flag = 4444
    elif var.lower() in greet_eng:
        flag = 11
    elif var.lower()=="yes" or var.lower()=="si" or var.lower() == "si puedo":
        flag = 8
    else:
        flag = 0
def cust_replay():
    print()

