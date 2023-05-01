class VendingItem:

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

class Vending:

    def __init__(self):
        self.VendingList = []
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0

    def load_vending_items_from_file(self, filename):

# open the file and read a lines
        with open(filename) as file:
            line = file.readline().strip('\n')

# while the line is not empty
            while line != "":

# Split the line into its components and create a VendingItem object
                split_list = line.split()
                vending_item_obj = VendingItem(split_list[0], int(split_list[1]), float(split_list[2]))

# using the InitialValue method, add the value to the VendingTotalInitialValue
                self.VendingTotalInitialValue = vending_item_obj.InitialValue()

# Using the IntialCount attribute, add the value to the VendingTotalInitialCount
                self.VendingTotalInitialCount = vending_item_obj.InitialCount

# append the VendingItem object to the VendingList
                self.VendingList.append(vending_item_obj)

# read the nextline
                line = file.readline().strip('\n')


    def print_vending(self):

        sum_initial_count = 0
        sum_initial_value = 0
        sum_sold_count = 0
        sum_sold_value = 0
        sum_lost_count = 0
        sum_lost_value = 0

        print("\t\tInitial\t\tPrice\tInitial\tSold\tSold\tLost\tLost")
        print("Product\tCount\tPer Item\tValue\tCount\tValue\tCount\tValue")

        for product in self.VendingList:

            sum_initial_count += product.InitialCount
            sum_sold_count += product.SoldCount
            sum_sold_value += product.SoldValue()
            sum_lost_count += product.LostCount
            sum_lost_count += product.LostValue()

            print(f"{product.Name}\t{product.InitialCount}\t\t{product.CostPerItem}\t\t{product.InitialValue()}\t\t{product.SoldCount}\t\t{product.SoldValue()}\t\t{product.LostCount}\t\t{product.LostValue()}")

        print(f"Total\t{sum_initial_count}\t\t\t\t{sum_sold_count}\t\t{sum_sold_value}\t\t\t{sum_lost_count}\t\t\t{sum_lost_count}")

    def find_product(self, productToFind):

# search the product names
        for index in range (len(self.VendingList)):
# check if the Name is matching
            if(self.VendingList[index].Name == productToFind):
                return index

    def update_vending(self, productName):

# search for the product in the VendingList and find the Index
        index = self.find_product(productName)

        item = self.VendingList[index]

# check if there is a product to sell
        if(item.SoldCount < item.InitialCount):

# increment SoldCount
            item.SoldCount += 1

# Increment the VendingTotalSoldCount
            self.VendingTotalSoldCount += 1

# add CostPerItem to the VendingTotalSoldValue
            self.VendingTotalSoldValue += item.CostPerItem

        else:

# Increment the LostCount
            item.LostCount += 1

# increment the VendingTotalLostCount
            self.VendingTotalLostCount += 1

# Add CostPerItem to VendingTotalLostValue
            self.VendingTotalLostValue += item.CostPerItem

# Main Program


# Create Vending object
vending_object = Vending()

# load the vending machine
vending_object.load_vending_items_from_file("Final Project Vending.txt")

# update vending from sales.txt
with open("Final Project Sales.txt") as file:
    for line in file.readlines():
        vending_object.update_vending(line.strip('\n'))

# print the results
vending_object.print_vending()

# call the main function
