from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
import sys
import traceback
import time
import random
import re
api_id = 000000  # API ID
api_hash = ''  #API HASH
phone = '+'  #NUMBER WITH COUNTRY CODE
timer = 2 #TIME TO WAIT BEFORE NEXT SENDING
msgtosend = "test" #MESSAGE TO SEND
username1 = "testchannal121" #USERNAME OF CHANNEL
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
chats = []
last_date = None
chunk_size = 10
groups=[]
result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:    
    try:    
        msg = client.send_message(username1, msgtosend)
        print("Send Complete!!, Waiting for " + str(timer) + " seconds")
        msgdel = msg.id - 1
        client.delete_messages(username1, msgdel)
        time.sleep(timer)
    except: 
        continue
