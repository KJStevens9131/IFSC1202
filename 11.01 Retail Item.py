class RetailItem:
  def __init__(self, Description, UnitOnHand,Price):
    self.Description = Description
    self.UnitOnHand = UnitOnHand
    self.Price = Price

  def InventoryValue(self): 
        return (self.UnitOnHand * self.Price)

#open file
f = open('11.01 Inventory.txt')

#create a list to hold objects of RetailItem
list = []

#read data from txt and store it 
for i in f:
  line = i.replace('\n','')
  data = line.split(', ')
  
  list.append(RetailItem(data[0],int(data[1]),float(data[2])))

#print header
print("{:>11} {:>17} {:>17} {:>17}".format("Description","Unit On Hand","Price","Inventory Value"))

#print data
for obj in list:
  print("{:>11} {:>17} {:>17} {:>17}".format(obj.Description,obj.UnitOnHand,obj.Price,'%.2f'%obj.InventoryValue()))

#close file
f.close()