from pymessenger import Button

b = open("Mensaje.txt", "r", encoding='utf-8')
if b.mode == "r":
    content = b.readlines()
    content = [x.strip() for x in content]
    b.close()



buttons = []
button = Button(type="postback", title=titulo0, payload=vuelto0)
buttons.append(button)
button = Button(type="postback", title=titulo1, payload=vuelto1)
buttons.append(button)
button = Button(type="web_url", url=link, title=titulo2) ## BOTÓN URL ##
buttons.append(button)
