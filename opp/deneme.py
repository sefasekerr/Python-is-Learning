with open("account_logs.txt","r+",encoding="utf-8") as file:
    for lines in file:
        # print(lines,end="") 
        lines = lines[:-1]
        if "bakiye" in lines:
            liste = lines.strip().split(":")
            bakiye = int(liste[1])
            sayi = input("giriş: ")
            file.write(sayi)