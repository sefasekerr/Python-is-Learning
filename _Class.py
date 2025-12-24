class CardItem:
    #constructor => yapıcı 
    def __init__(self, name, price, quantity):
        #instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
        with open("items.txt","a",encoding="utf-8") as file:
            file.write(f"Item name : {self.name} , Item price : {self.price} , Item quantity : {self.quantity}\n")
    #instance methods
    def calculate_total(self):
        calculate_total= self.price*self.quantity
        return calculate_total
        
    def apply_discount(self):
        ct = CardItem.calculate_total(self)
        rate = 0
        if ct >10000:
           rate = 0.8
        elif ct> 5000:
            rate= 0.9
        else:
            return ct
        ct = ct * rate 
        return   ct  
    
    def net_total(self):
        ad_ct = CardItem.apply_discount(self)
        return ad_ct
    

    # def save_item(self):
    #     pass
    
    #     with open("items.txt","a",encoding="utf-8") as file:
    #         file.write(f"Item name : {self.name} , Item price : {self.price} , Item quantity : {self.quantity}\n")
            
    def __str__(self):
        return f"Item name : {self.name} , Item price : {self.price} , Item quantity : {self.quantity}"
    
           
    

    
    
item1 = CardItem("telefon",50000,2)
item1.apply_discount()
print(item1.net_total())
# item1.save_item()
item1.name = "telefon"
item1.price = 10000
item1.quantity = 5

item2 = CardItem("bilgisayar",25000,1)
item3 = CardItem("şarj",500,2)
item2.name = "bilgisayar"
item2.price = 20000
item2.quantity = 1

print(item1.name)
print(item2.name)
print(item1.price )
print(item2.price)

print(CardItem.calculate_total(item1))
# CardItem.save_item(item1)
print(CardItem.apply_discount(item3))