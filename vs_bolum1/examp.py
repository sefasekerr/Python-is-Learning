# brands = ["toyota", "ford", "bmw", "audi"]
# result1 = len(brands)
# result2 = brands[0] + brands [len(brands)-1]
# result3  = brands.index("ford")
# brands[result3] = "togg"
# result3 = brands
# result4 = "togg" in brands
# result5 = brands[:2]
# brands.extend(["renault","citroen"])
# brands.pop()
# result6 = brands
# student1 = ["yğit bilgi " , 2010, [70,80,90]]
# student2 = ["ada bilgi ", 2011, [70,70,80]]
# student3 = ["çınar turan ", 2017, [60,60,90]]
# stundets_info = [student1, student2, student3]
# age = [2025 - stundets_info[0][1], 2025 - stundets_info[1][1], 2025 - stundets_info[2][1]]
# nots_avg = [sum(stundets_info[0][2])/len(stundets_info[0][2]), sum(stundets_info[1][2])/len(stundets_info[1][2]), sum(stundets_info[2][2])/len(stundets_info[2][2])]
# print(age)
# print(nots_avg)
# print(stundets_info)



# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(brands)
# print(result6)

customers = ["sadikturan", "ahmetyilmaz","cinarturan", "yğitbilgi"]
order_toals = [12000,13000,5000,15000]

customers.append("sadikturan")
order_toals.append(5000)

customers.pop()
order_toals.pop()

for customer in customers:
    i = customers.index(customer)
    print(f"{customer} isimli müşterinin sipariş tutarı: {order_toals[i]}")
    
customers.sort()
order_toals.reverse()
a = order_toals.index(min(order_toals))
print(f"{customers[a]} isimli müşterinin en düşük sipariş tutarı: {order_toals[a]}")

print(customers.count("sadikturan"))
customers.remove("ahmetyilmaz")
customers.clear()
order_toals.clear()

customers.append(input("Lütfen müşteri ismi giriniz: "))
order_toals.append(float(input("Lütfen sipariş tutarı giriniz: ")))
print(customers)
print(order_toals)  















