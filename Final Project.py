class VendingItem(object):
    def __init__(self,name,initial_count,cost_per_item):
        self.name=name
        self.initial_count=initial_count
        self.cost_per_item=cost_per_item
        self.sold_count=0


    def initial_value(self):
        initial_val=self.initial_count*self.cost_per_item
        return initial_val

    def sold_value(self):
        sold_val=self.sold_count*self.cost_per_item
        return sold_val


class Vending(object):

    def __init__(self,file_name):
#varibles to store data
        self.vending_list=[]
        self.vending_total_sold_count=0
        self.vending_total_sold_value=0
        self.vending_total_initial_value=0
        self.vending_total_initial_count=0

#read from file and update list and variables
        with open(file_name,"r") as file:
            for line in file:
                item=line.split()
                vending_item=VendingItem(item[0],int(item[1]),float(item[2]))
                self.vending_list.append(vending_item)
#iterate throught the list

        for item in self.vending_list:
            self.vending_total_initial_value=self.vending_total_initial_value+item.initial_value()
            self.vending_total_initial_count=self.vending_total_initial_count+item.initial_count


    def print_vending(self):
#print all information
        print("items present are: ")
#iterate throught the list

        for product in self.vending_list:
            print(("%s %d %f %d %f %f")%(product.name,product.initial_count,product.cost_per_item,product.sold_count,product.initial_value(),product.sold_value())) 
            print(("vending total inital count = %d")%(self.vending_total_initial_count))
            print(("vending total initial value = %f")%(self.vending_total_initial_value))
            print(("vending total sold count =%d")%(self.vending_total_sold_count))
            print(("vending total sold value = %f")%(self.vending_total_sold_value))
            print()


    def update_vending(self,name):
#iterate throught the list
        for i in range(0,len(self.vending_list)-1):
            product=self.vending_list[i]

            if(product.name==name):
                if(product.sold_count<product.initial_count):
                    product.sold_count=product.sold_count+1
                    self.vending_total_sold_count=self.vending_total_sold_count+1
                    self.vending_total_sold_value=self.vending_total_sold_value+product.sold_value()
                    return
                else:
                    print("product sold out")
                return


def main():
    vending =Vending("Final Project Vending.txt")
    vending.print_vending()
#get input as product name and then increment sold count of product by 1
    while(True):
        name=input("enter product name or type (exit) to exit :")
        if(name=="exit"):
            print("bye!!")
            break
        vending.update_vending(name)
        vending.print_vending()


main()