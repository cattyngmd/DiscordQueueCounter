import discord
import colorama
import requests
import time
import json

cl = discord.Client()
debug = False
token = ""
queueId = 0
prioqId = 0

@cl.event
async def on_ready():
    print(f"{colorama.Fore.MAGENTA}QueueCounter v0.1{colorama.Fore.WHITE}")
    while True:
        prioq = json.loads(requests.get("https://api.2b2t.dev/prioq").text)
        regularq = json.loads(requests.get("https://2b2t.io/api/queue?last=true").text)
        if debug:
            print(str(prioq[1]) + " " + str(regularq[0][1]))
        await cl.get_channel(prioqId).edit(name=f"Priority queue: {prioq[1]}")
        await cl.get_channel(queueId).edit(name=f"Normal queue: {regularq[0][1]}")
        time.sleep(5)

if __name__ == '__main__':
    colorama.init()
    cl.run(token)