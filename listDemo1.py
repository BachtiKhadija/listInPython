l=[] # liste vide 
l=[12,"hello",False,15.23]
print(l)
print(len(l))#nombre des elements de la liste
#print(l[4])#index out of range
print(l[-2])
#parcourir la liste 
#méthode1: parcourir element par element
"""
 syntaxe  =>  for elet in listName:
                    ...
                    
                    ...
                    
"""
for x in l: 
    print(x)
print("*"*60)
#méthode2: parcourir les elements par position

for i in range(0,len(l)):
    print(l[i])