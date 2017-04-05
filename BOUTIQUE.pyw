from graphics import*

class Boutique:
    def __init__(self, name="Unkown",owner="This"):
        self.name = name
        self.owner = owner
        self.prices = {}
        self.quantities = {}

    def fillup(self):
        price = open("prices.txt","r")
        qty = open("quantities.txt","r")
        for line in price:
            a = line.split()
            self.prices[a[0] + " " + a[1]] = a[-1]
        for line in qty:
            a = line.split()
            self.quantities[a[0] + " " + a[1]] = a[-1]

    def setPrice(self, item, size,newPrice):
        self.prices[item.title() + " " + size.title()] = newPrice
        qty = open("prices.txt","r")
        content = ""
        for line in qty:
            a, b, c = line.split()
            if a == item.title() and b == size.title():
                c = newPrice
            content = content + a + " " + b + " " + str(c) + "\n"
        qty2 = open("prices.txt","w")
        qty2.write(content)
        qty2.close()

    def printReceipt(self, name, item, size, quantity, price):
        file = open("receipt.txt","w")
        print("{0:^30}".format(self.name.title()))
        print("{0:^30}".format(self.name), file = file)
        print("{0:10}: {1:1}".format("Name", name))
        print("{0:10}: {1:1}".format("Item", item))
        print("{0:10}: {1:1}".format("Size", size))
        print("{0:10}: {1:0}".format("Quantity", quantity))
        print("{0:10}: GHC{1:0.2f}".format("Unit price", price))
        print("{0:10}: GHC{1:0.2f}".format("Amount", quantity * price))
        print("{0:10}: {1:1}".format("Name", name), file = file)
        print("{0:10}: {1:1}".format("Item", item), file = file)
        print("{0:10}: {1:1}".format("Size", size), file = file)
        print("{0:10}: {1:0}".format("Quantity", quantity), file = file)
        print("{0:10}: GHC{1:0.2f}".format("Unit price", price), file = file)
        print("{0:10}: GHC{1:0.2f}".format("Amount", quantity * price), file = file)
        file.close()

    def printAvailableStock(self):
        qty = open("quantities.txt","r")
        items = "Item \t Size \t Quantity \n"
        for line in qty:
            a = line.split()
            items = items + a[0] + " \t " + a[1] + " \t " + a[2] + " \n"
        return items

    def reduceStock(self,item, size, quantity):
        qty = open("quantities.txt","r")
        
        self.quantities[item.title() + " " + size.title()] = int(self.quantities[item.title() + " " + size.title()]) - quantity
        content = ""
        for line in qty:
            a, b, c = line.split()
            if a == item.title() and b == size.title():
                c = int(c) - quantity
            content = content + a + " " + b + " " + str(c) + "\n"
        qty2 = open("quantities.txt","w")
        qty2.write(content)
        qty2.close()
        
            








n = Boutique()
n.fillup()
n.printReceipt("Elvis","Jeans","Small", 200, 13)
print(n.printAvailableStock())
n.reduceStock("Jeans","Small", 200)
print(n.printAvailableStock())
n.setPrice("Jeans","Small", 200)
