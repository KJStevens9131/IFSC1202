str = input ("Enter a string : ")
strr = str[::-1]
ind1 = str.find('f')
if ind1 == -1:
  print(0)
else:
  ind = strr.find('f')
  n= len(str)
  ind2 = n - ind
  if ind1 == ind2:
    print (ind1)
  else:
    print (ind1, ind2)