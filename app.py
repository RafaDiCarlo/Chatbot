import os, requests
import json
from flask import Flask, render_template, request
from reader import verify_token, access_token
#from button_builder import saludo, buttons
from pymessenger import Bot, Button
app = Flask(__name__)

PAGE_ACCESS_TOKEN = access_token

bot = Bot(PAGE_ACCESS_TOKEN)

b = open("Botones.txt", "r", encoding='utf-8')
if b.mode == "r":
    content = b.readlines()
    content = [x.strip() for x in content]
    b.close()
else:
	b.close()

i = open("BotonExtra.txt", "r", encoding='utf-8')
if i.mode == "r":
    BotonExtraContent = i.readlines()
    BotonExtraContent = [x.strip() for x in content]
    i.close()
else:
	i.close()

#Botones Default
saludo = content[0]
titulo0 = content[2]
respuesta0 = content[4]
titulo1 = content[6]
respuesta1 = content[8]
titulo2 = content[10]
link = content[12]
vuelto0 = content[14]
vuelto1 = content[15]

#Botón Extra
BotonExtra = BotonExtraContent[0]
BEtitulo = BotonExtraContent[2]
BErespuesta = BotonExtraContent[4]
BEvuelto = BotonExtraContent[6]


##def process_message(text):
    #formatted_message = text.lower()
    #if formatted_message == titulo0:
    #    response = respuesta0
    #elif formatted_message == titulo1:
    #    response = respuesta1
    #else:
    #    response = saludo
    #return response

buttons = []
button = Button(type="postback", title=titulo0, payload=vuelto0)
buttons.append(button)
button = Button(type="postback", title=titulo1, payload=vuelto1)
buttons.append(button)
button = Button(type="web_url", url=link, title=titulo2) ## BOTÓN URL ##
buttons.append(button)




@app.route('/', methods=["get"])
def webhook():
    if verify_token == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return ':)'

@app.route('/', methods=["POST"])
def webhook_handle():
    payload = request.get_json()
    with open("FB_MSN.json", "w", encoding="utf-8") as xd:
        json.dump(payload, xd , indent=2, sort_keys=True)
    xd.close()
    event = payload['entry'][0]['messaging']
    sender_id = payload['entry'][0]['messaging'][0]['sender']['id']
    try:
        postback = payload['entry'][0]['messaging'][0]['postback']['payload']
    except:
        postback = None
    response = saludo
    if postback == vuelto0:
        response = respuesta0
        bot.send_text_message(sender_id, response)
    elif postback == vuelto1:
        response = respuesta1
        bot.send_text_message(sender_id, response)
    elif postback == BEvuelto:
    	response = BErespuesta
    	bot.send_text_message(sender_id, response)
    else:
        bot.send_button_message(sender_id, response, buttons)


    return "Mensaje Recibido."
    return "200"




if __name__ == "__main__":
    app.run(threaded=True, port=5000)
