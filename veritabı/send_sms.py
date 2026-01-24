import vonage

client = vonage.Client(key="e026e679", secret="rS9NDzxMqDXNBOUNFyYspb4QneUMVd61gJjbVDQLsUGlYmEdBR")
sms = vonage.Sms(client)

responseData = sms.send_message({
    "from": "sefa",
    "to": "905418018477",   # ülke kodu ile numara
    "text": "Merhaba Sefa, bu bir test mesajıdır!"
})

if responseData["messages"][0]["status"] == "0":
    print("Mesaj başarıyla gönderildi.")
else:
    print(f"Hata: {responseData['messages'][0]['error-text']}")
    
    
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "905418018477",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

AIzaSyBUEk5V8x_cyHMdkHH0pc3pT51v7hbYiPE