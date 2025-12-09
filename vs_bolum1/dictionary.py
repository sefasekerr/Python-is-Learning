customers = {
    101:    {
        "customerName": "yiğit bilgi",
        "birthyear": 2010,
        "notes": [40, 80, 90],
    },


    102:    {
        "customerName": "ada bilgi",
        "birthyear": 2012,
        "notes": [80, 80, 80],
    },


    103:    {
        "customerName": "çınar turan",
        "birthyear": 2017,
        "notes": [70, 70, 70],
    }
}


number = int(input("Lütfen müşteri numarasını giriniz: "))

if number in customers:
    print(
        f"{number} numaralı müşterinin adı: {customers[number]['customerName']}")
else:
    print("Müşteri bulunamadı.")
