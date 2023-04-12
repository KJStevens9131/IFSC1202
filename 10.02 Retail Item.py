#I tried multiple methods but could get the inventory value to multiply
class RetailItem ():

    def __init__(self):
        self.Description = ""
        self.UnitsOnHand = 0
        self.Price = 0
    def __repr__(self):
        return"{:>s}\t\t{:>s}\t\t{:>s}".format(self.Description,self.UnitsOnHand,self.Price)
    #def InventoryValue(self):
        #return(self.UnitsOnHand*self.Price)

print("{:>s}{:>15s}{:>10s}{:>20s}".format("Description", "Units On Hand", "Price","Inventory Value"))
FirstItem = RetailItem()
SecondItem = RetailItem()
ThirdItem = RetailItem()
Invfile = open("10.02 Inventory.txt","r")

x = Invfile.readline()
y = x.strip().split(",")
FirstItem.Description = y[0]
FirstItem.UnitsOnHand = y[1]
FirstItem.Price = y[2]
#FirstItem.InventoryValue() 
print(FirstItem)

x = Invfile.readline()
y = x.strip().split(",")
SecondItem.Description = y[0]
SecondItem.UnitsOnHand = y[1]
SecondItem.Price = y[2]
#SecondItem.InventoryValue()
print(SecondItem)

x = Invfile.readline()
y = x.strip().split(",")
ThirdItem.Description = y[0]
ThirdItem.UnitsOnHand = y[1]
ThirdItem.Price = y[2]
#ThirdItem.InventoryValue()
print(ThirdItem)

Invfile.close()