import math

def diameter(radius):
    return radius * 2
def circumference(radius):
    return 2 * math.pi * radius
def area(radius):
    return math.pi * radius * radius

def main():
    file1 = open("06.01 Radius.txt","r")
    #lst = []

    while True:
        line = file1.readline()
        if not line:
            break
        else:
            lst.append(float(line))

    print("{:>15} {:>15} {:>15} {:>15}".format("Radius","Diameter","Circumference","Area"))
    for radius in lst:
        print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius,diameter(radius),circumference(radius),area(radius)))



if __name__ == "__main__":
    main()