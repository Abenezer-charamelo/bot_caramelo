        # imports important module
import requests
import json
import update as upp
import sendmessage
import bridge
        # declaration of important variables
            # the offset is set to read from external file named update.txt
            # timeout is the time to wait until message arrived if not retry again
            # message is empty first
            # token is our bot unique key botfather given
            # r is the variable where we put the update page requested
offset=upp.rd_updd("update.txt")
timeout="99999999"
message=""
token = "https://api.telegram.org/bot*******************************************/getupdates?"
r = None
cus_array=None
        # this function edits the url and request update page and store it in r
def requ():
    global r
    global token
    url=token+"offset={}".format(offset)+"&timeout={}".format(timeout)
    r = requests.get(url)

def info():
        global cus_array
        name = cus_array["result"][0]["message"]["from"]["first_name"]
        text= cus_array["result"][0]["message"]["text"]
        if cus_array["result"][0]["message"]["chat"]["type"]=="private":
            id = cus_array["result"][0]["message"]["from"]["id"]
        elif cus_array["result"][0]["message"]["chat"]["type"]=="group":
            id = cus_array["result"][0]["message"]["chat"]["id"]
        info =[id,name,text]
        return info

def accept():
    global cus_array
    print("\tmessage arrived !!!!!")
    wrr()
    logs()
    infoo = info()
    print ("\t\t\tMessage:      {}".format(infoo[2]))
    print ("\t\t\tSender :      {}".format(infoo[1]))
    print ("\t\t\tID     :      {}".format(infoo[0]))
    print("\tReplaying........")
    playee()

def wrr():
    file=open("message.txt","a")
    file.write(message)
    file.write("\n")
    file.close()

def logs():
    global offset
    upp.loging("botlog.txt","update.txt")
    offset = str(int(offset)+1)
    upp.wr_updd("update.txt",offset)

def logg_user(id,name,txt,replay):
    file = open("users_log.txt","a")
    file.write("=====================================\n")
    file.write("User-name: {}\n".format(name))
    file.write("Chat-id: {}\n".format(id))
    file.write("Message: {}\n".format(txt))
    file.write("Replay: {}\n".format(replay))
    file.write("=====================================\n")
    file.close()

def playee():
        global message
        global cus_array
        #print(info[0],info[1],info[2],sep="    ")
        #print("play 6 success full")
        infoo = info()
        bridge.checkmsg(infoo[2])
        replay=bridge.replay(bridge.flag,infoo[0],infoo[1],infoo[2])
        logg_user(infoo[0],infoo[1],infoo[2],replay)


""" this is the main function where:
                    you request the page with some offset
                    change the content of the page in to a multidimessional list
                    try extracting the message or retry the whole function again
                    if successful write message in external file named message.txt
                    log the current update id
                    increase the update id by 1
                    print out the message """

def get_message():
    global cus_array
    global message
    global offset
    print("\t***************************************************************************************")
    print("\tRequesting url .......")
    print ("\tPlease wait until message arives (offset={})........".format(offset))
    requ()
    cus_array=json.loads(r.content)
    try:
        message=cus_array["result"][0]["message"]["text"]
        if message is not "":
            accept()
            print("\n\t***************************************************************************************")
    except:
        print("\n\tRetrying ..........")
        get_message()

def fuu():
    while True:
        try:
            get_message()
        except:
            fuu()
fuu()
