class Item ():
    pay_rate = 0.7
    all=[]
    def __init__(self,name,price,quantity):
       
        assert price >=0
        assert quantity >=0,"the Error in Assertion {price}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    def total_price(self):
        return self.price * self.quantity
    def discount_amount (self):
        return self.price * self.pay_rate
    
    def __repr__(self):
        return f"Items  {self.name},{self.price},{self.quantity}"

    
item_1 = Item("Vignesh",1000,50)
item_2 = Item("Rajesh",100,30)
item_3 = Item("Mani",200,20)
item_4 = Item("Ram",400,80)
item_5 = Item("Master",600,60)

print(Item.all)


