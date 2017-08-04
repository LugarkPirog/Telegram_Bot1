import requests
import numpy as np
import json
from time import time, sleep
import datetime

token = "411994147:AAH731qEte9GlKpImQzYlfzY3Gc_ijjam38"

class Bot:
    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot{}/".format(token)

    def getUpdatesJson(self, offset=None, timeout=200):
        params = {"timeout": timeout,"offset": offset}
        response = requests.get(self.url + "getUpdates", params)
        return response.json()['result']

    def getLastUpd(self, data):
        result = self.getUpdatesJson()
        if len(result) > 0:
            last_update = result[-1]
        else:
            last_update = result[len(result)]
        return last_update

    def getChatId(self, upd):
        chatId = upd['message']['chat']['id']
        return  chatId

    def sendMsg(self, chat, text):
        params = {"chat_id": chat, "text": text}
        query = self.url + "sendMessage"
        response = requests.post(query, data=params)
        return response

bot = Bot(token)
now = datetime.datetime.now()
def main():
	new_offset = None
	
	while True:
		updates = bot.getUpdatesJson(new_offset)
		last_upd = bot.getLastUpd(updates)
		print('hello')
		sleep(1)
# chatId = getChatId(getLastUpd(getUpdatesJson()))
# print(chatId)
# response = sendMsg(chatId, "Test message. Hope it will work")
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()