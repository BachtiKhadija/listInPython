#remplacer les valeurs négatives par zero
l=[1,2,-8,0,10,-9,13,-6]
print(l)
l1=list()
for x in l:
    if x>=0:
        l1.append(x)
        
    else:
        l1.append(0)
print(l1)


#l2=[resulta if condition  else resulta2 for item in range ]

l3=[x if  x>=0 else 0  for x in l]
print(l3)