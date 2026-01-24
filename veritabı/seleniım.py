towns = {"ADALAR" : 1	,
"ARNAVUTKÖY" : 2	,
"ATAŞEHİR" : 3	,
"AVCILAR" : 4	,
"BAĞCILAR" : 5	,
"BAHÇELİEVLER" : 6	,
"BAKIRKÖY" : 7	,
"BAŞAKŞEHİR" : 8	,
"BAYRAMPAŞA" : 9	,
"BEŞİKTAŞ" : 10,
"BEYKOZ" : 11,
"BEYLİKDÜZÜ" : 12,
"BEYOĞLU" : 13,
"BÜYÜKÇEKMECE" : 14,
"ÇATALCA" : 15,
"ÇAYIROVA" : 16,
"ÇEKMEKÖY" : 17,
"ESENLER" : 18,
"ESENYURT" : 19,
"EYÜP" : 20,
"EYÜPSULTAN" : 21,
"FATİH" : 22,
"GAZİOSMANPAŞA" : 23,
"GÜNGÖREN" : 24,
"KADIKÖY" : 25,
"KAĞITHANE" : 26,
"KAPAKLI" : 27,
"KARTAL" : 28,
"KÜÇÜKCEKMECE" : 29,
"KÜÇÜKÇEKMECE" : 30,
"MALTEPE" : 31,
"MERKEZ" : 32,
"PENDİK" : 33,
"SANCAKTEPE" : 34,
"SARIYER" : 35,
"SİLİVRİ" : 36,
"SULTANBEYLİ" : 37,
"SULTANGAZİ" : 38,
"ŞİLE" : 39,
"ŞİŞLİ" : 40,
"TUZLA" : 41,
"ÜMRANİYE" : 42,
"ÜSKÜDAR" : 43,
"YEŞİLKÖY" : 44,
"ZEYTİNBURNU" : 45,}
def deneme(ilce):
    for k,v in towns.items():
        if k == ilce:
            ilce = v
            return ilce
            


print(deneme("SULTANGAZİ"))