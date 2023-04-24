class RetailItem:



    def __init__(self, desc='', units=0, price=0.0):

        self.description = desc

        self.unitsOnHand = units

        self.price = price



    def InventoryValue(self):

        return self.unitsOnHand * self.price





def main():

    file = '11.01 Inventory.txt'

    items=[]

    file_in = open(file, 'r')

    for line in file_in:

        data = line.strip().split(',')

        name, units, price = data[0].strip(), int(data[1].strip()), float(data[2].strip())

        retail_item = RetailItem(name, units, price)

        items.append(retail_item)

    file_in.close()

    print('{:>12}{:>15}{:>15}{:>25}'.format('Description','Units On Hand','Price','Inventory Value'))

    for item in items:

        print(f'{item.description:>12}{item.unitsOnHand:>15}{item.price:>15.2f}{item.InventoryValue():>25.2f}')

main()