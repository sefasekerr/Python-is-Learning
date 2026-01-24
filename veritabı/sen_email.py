import smtplib
from email.mime.text import MIMEText


port = 587
smtp_server = "smtp-relay.brevo.com"
login = "9fed03001@smtp-brevo.com"



sender_email = "sefaseker92@gmail.com"
receiver_email = email_address

text = f"""
hoşgeldinn{name}
vayyyy ilk e-postammm
python uygulmasından geldi"""

message = MIMEText(text,"plain")
message["Subject"]=f"merhaba {name}"
message["From"] = sender_email
message["To"]= receiver_email

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
    
print("eposta gönderildi")