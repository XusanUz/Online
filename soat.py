from pyrogram import Client
from pyrogram.raw import functions
from time import sleep

api_id = '2487143' #my.telegram.org,dan olgan api_id yozing.

api_hash = "9ce7e7964886e49c1df2cba1bf9bd8a2" # my.telegram.org,dan olgan api_hash yozing.

a =  Client("test",api_id,api_hash)
a.start()
@a.on_message()
def _(c,m):
 a.read_history(m.chat.id)
while True:
 a.send(functions.account.UpdateStatus(offline=False))
 sleep(1)