import requests
from time import time, sleep
import datetime
# import asyncio
# import collections

token = "411994147:AAH731qEte9GlKpImQzYlfzY3Gc_ijjam38"


class Bot:
    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates_json(self, offset=None, timeout=200):
        params = {"timeout": timeout,"offset": offset}
        response = requests.get(self.url + "getUpdates", params)
        return response.json()['result']

    def get_last_upd(self, data):
        result = self.get_updates_json()
        if len(result) > 0:
            last_update = result[-1]
        else:
            last_update = result[len(result)]
        return last_update

    def get_chat_id(self, upd):
        chat_id = upd['message']['chat']['id']
        return chat_id

    def send_msg(self, chat, text):
        params = {"chat_id": chat, "text": text}
        query = self.url + "sendMessage"
        response = requests.post(query, data=params)
        return response

bot = Bot(token)
now = datetime.datetime.now()

#
# def tick(delay, count):
#     for i in range(count):
#         print("dsd")
#         yield i


def main():
    new_offset = None
    i = 0
    while True:
        updates = bot.get_updates_json(new_offset)
        last_upd = bot.get_last_upd(updates)
        chat_id = bot.get_chat_id(last_upd)
        txt = last_upd['message']['text']
        if i > 0:
            t = i ** 2
            bot.send_msg(chat_id, t)
            i -= 1
        elif txt.isdigit():
            i = int(txt)
            t = i ** 2
            bot.send_msg(chat_id, t)
            i -= 1
        sleep(5)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
