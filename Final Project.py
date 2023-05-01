#Most things here don't need notes to the name being the action that it does
#Prints the Labels for the data
print("{:9s}{:8s}{:8s}{:8s}{:8s}{:8s}{:12s}".format("\tInitial", "Price", "Initial", "Sold","Sold", "Lost","Lost"))
print("{:8s}{:8s}{:8s}{:8s}{:8s}{:8s}{:8s}{:12s}".format("Product", "Count", "PerItem", "Value","Value", "Count","Count","Value"))

#Class for set up the first set of data points
class VendingItem(object):
    def __init__(self, Name, InitialCount, CostPerItem):
        self.Name = Name
        self.InitialCount = InitialCount
        self.CostPerItem = CostPerItem
        self.SoldCount = 0
        self.LostCount = 0
    def InitialValue(self):
        return self.InitialCount * self.CostPerItem
    def SoldValue(self):
        return self.SoldCount * self.CostPerItem
    def LostValue(self):
        return self.LostCount * self.CostPerItem

#Class used to set up the remaining data points
class Vending:
    def __init__(self, Name):
        self.Name = Name
        self.Vendinglist = []
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0

    def load_vending_items_from_file(self,file):
        z = open(file,"r")
        for x in z:
            list1 = x.split()
            vend = VendingItem(list1[0],int(list1[1]),float(list1[2]))
            self.VendingTotalInitialValue += vend.InitialValue()
            self.VendingTotalInitialCount += vend.InitialCount
            self.Vendinglist.insert(len(self.Vendinglist),vend)

#eulav is value backwards to make it stand out more
#Prints out the value under the titles
    def print_vending(self):
        for eulav in self.Vendinglist:
            print("{:}\t{:}{:10.2f}{:9.2f}\t{:}{:11.2f}\t{:}\t{:.2f}".format(eulav.Name,eulav.InitialCount,eulav.CostPerItem,eulav.InitialValue(),eulav.SoldCount,eulav.SoldValue(),eulav.LostCount,eulav.LostValue()))
        print("")
        print("{:}\t{:}{:10}{:9.2f}\t{:}{:11.2f}\t{:}\t{:.2f}".format("Total",self.VendingTotalInitialCount,"",self.VendingTotalInitialValue,self.VendingTotalSoldCount,self.VendingTotalSoldValue,self.VendingTotalLostCount,self.VendingTotalLostValue))

    def find_product(self,producttofind):
        list2 = -1
        for eulav in self.Vendinglist:
            list2 = list2 + 1
            if eulav.Name == producttofind:
                return list2
            return list2

    def update_vending(self,productname):
        list2 = self.find_product(productname)
        if list2 != -1:
            eulav = self.Vendinglist[list2]
            if eulav.SoldCount < eulav.InitialCount:
                eulav.SoldCount = eulav.SoldCount + 1
                self.VendingTotalSoldValue = self.VendingTotalSoldValue + eulav.CostPerItem
                self.VendingTotalSoldCount = self.VendingTotalSoldCount + 1
            else:
                eulav.LostCount = eulav.LostCount + 1
                self.VendingTotalLostValue = self.VendingTotalLostValue + eulav.CostPerItem
                self.VendingTotalLostCount = self.VendingTotalLostCount + 1

#Used to actually call for the data
list3 = Vending("")
list3.load_vending_items_from_file("Final Project Vending.txt")
z = open("Final Project Sales.txt","r")
for x in z:
    list3.update_vending(x)
list3.print_vending()