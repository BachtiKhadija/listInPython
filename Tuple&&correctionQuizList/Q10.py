l=[chr(c) for c in range(97,106)]
print(l)
l2=l.copy() #shallow
l3=l #deep
l4=list(l) #shallow
print(l2)
print(l3)
print("*"*50)
l.append('j')

print(l,l2,l3,sep='\n')