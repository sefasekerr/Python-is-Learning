import datetime as dt


with open("log.txt", "a",encoding="UTF-8") as f:
    if 6<= dt.datetime.now().hour < 10:
        f.write(f"{dt.datetime.now().strftime("%H:%M")} günaydın yenimi uyanıyonn\n ")
    elif 10<= dt.datetime.now().hour < 14:
        f.write(f"{dt.datetime.now().strftime("%H:%M")} tünaydın su içmeyi unutma\n ")
        
    elif 14<= dt.datetime.now().hour < 22:
        f.write(f"{dt.datetime.now().strftime("%H:%M")} iyi gün geçir kendini odaklan bu asalak gibi olma (hiranuru işaret ettim)\n ")
        
    elif 22<= dt.datetime.now().hour <6 :
        f.write(f"{dt.datetime.now().strftime("%H:%M")} get uyu)\n ")
    
    f.write(f"{dt.datetime.now().hour}---saat\n")
    f.write(f"{dt.datetime.now().minute}-dakika\n")
    f.write(f"{dt.datetime.now().second}-saniye\n")


with open("log.txt", "r",encoding="utf-8") as f:
    print("Log içeriği:")
    print(f.read())
