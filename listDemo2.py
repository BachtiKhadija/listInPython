#les listes sont modifiables
l=[12,True,15,16.3]
l[1]=55
print(l)
#python propose plusieurs méthodes pour modifier les listes

#inserer une nouvelle valeur à la fin 
l.append(200)
print(l)
#inserer une nouvelle valeur dans une position donnée
l.insert(1,300) # l.insert(pos,newValue)
print(l)

#supprimer le dérnier element 
deletedItem=l.pop()
print(deletedItem)
print(l)
#supprimer un elemnt specifique 
#l.pop(index)

l.pop(1)
#l.remove(element)
l.remove(55)
print(l)
#UTLISER del  => del listName[position]

del l[2]

print(l)