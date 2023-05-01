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

class Vending(object):
    def __init__(self):
        self.VendingList = []
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0

    def load_vending_items_from_file(self, filename):
        input1 = open(filename, "r")
        ListofLines = input1.readlines()
        input1.close()
        for line in ListofLines:
            tmplist = line.split()
            v1 = VendingItem(tmplist[0], int(tmplist[1]), float(tmplist[2]))
            self.VendingTotalInitialValue += v1.InitialValue()
            self.VendingTotalInitialCount += v1.InitialCount
            self.VendingList.insert(len(self.VendingList), v1)

    def print_vending(self):
        print('\tInitial\tPrice\tInitial\tSold\tSold\tLost\tLost')
        print('Product\tCount\tPerItem\tValue\tValue\tCount\tCount\tValue')
        for item in self.VendingList:
            print("%s\t%d\t%0.2f\t%0.2f\t%d\t%0.2f\t%d\t%0.2f" % (item.Name, item.InitialCount, item.CostPerItem, item.InitialValue(), item.SoldCount, item.SoldValue(), item.LostCount, item.LostValue()))
        print("Total Initial Value: %0.2f" % self.VendingTotalInitialValue)
        print("Total Initial Count: %d" % self.VendingTotalInitialCount)
        print("Total Sold Value: %0.2f" % self.VendingTotalSoldValue)
        print("Total Sold Count: %d" % self.VendingTotalSoldCount)
        print("Total Lost Value: %0.2f" % self.VendingTotalLostValue)
        print("Total Lost Count: %d" % self.VendingTotalLostCount)

    def find_product(self, producttofind):
        for i in range(len(self.VendingList)):
            if self.VendingList[i].Name == producttofind:
                return i
        return -1

    def update_vending(self, productname):
        index = self.find_product(productname)
        if index >= 0:
            if self.VendingList[index].SoldCount < self.VendingList[index].InitialCount:
                self.VendingList[index].SoldCount += 1
                self.VendingTotalSoldCount += 1
                self.VendingTotalSoldValue += self.VendingList[index].CostPerItem
            else:
                self.VendingList[index].LostCount += 1
                self.VendingTotalLostCount += 1
                self.VendingTotalLostValue += self.VendingList[index].CostPerItem

v1 = Vending()
v1.load_vending_items_from_file('Final Project Vending.txt')  # assuming the input file name is 'vending_items.txt'
v1.print_vending()

while True:
    product = input("Enter product name to purchase (or 'quit' to exit): ")
    if product == 'quit':
        break
    v1.update_vending(product)

v1.print_vending()