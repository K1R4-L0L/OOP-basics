class Fruit:
    def __init__(self, name,color, taste, price ):
        self.name = name
        self.color = color
        self.taste = taste 
        self.price = float(price)
   #Prints fruit details 
    def details(self):
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~

            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit Taste: {self.taste}
            Fruit cost: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~
        """)

     def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
         print(f"""
        #####################
        Total Cost: {total}
        #####################
        """)
apple = Fruit("Apple", "Red", "sour", 1.25)
pear = Fruit("Pear", "Green", "sweet", 1.50)
strawberry = Fruit("Strawberry", "Red", "sweet", 2.00)

apple.details()
pear.details()
strawberry.details()
apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)
