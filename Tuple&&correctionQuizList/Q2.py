l=[chr(c) for c in range(97,104)]
print(l)
l2=[chr(c) for c in range(105,115)]

print(l2)
l3=l+l2
#print(l3)
output=l.extend(l2)  #ajouter les elts de l2 dans l
print(l,l2,output,sep="\n")