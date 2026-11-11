l=[12,13,15,16,18,19,20]
#get slice from list =>  listName[start:end:step]
# listName[start:stop]  => step=1 

print(l[2:5:1])# =>[15,16,18]
print(l[1:6]) #[13,15,16,18,19]
l2=l[:]
l3=l
l4=l.copy() #l4 comme l2 => shallow copy of l
print(l2) #copie de la lite 
print(l3)
l.append(20)
print("***************************************AFTER**************************")
print("l=>",l)
print("l3>",l3)

print("l2=>",l2)