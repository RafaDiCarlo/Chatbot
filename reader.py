f=open("WEBHOOK_VERIFY_TOKEN.env", "r")
if f.mode == "r":
    verify_token = f.read()
    f.close()

f1=open("WEBHOOK_ACCESS_TOKEN.env", "r")
if f1.mode == "r":
    access_token = f1.read()
    f1.close()
