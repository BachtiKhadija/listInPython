l=[x for x in range(0,10)]
#syntaxe générale =>[item for item in range]
#version détaillée
"""l[]
for x in range(0,10):
    l.append(x)"""
    
    
#eexmple 
#soit la lise l1=[1,2,3,4,5,6,7,8]
l1=list(range(1,9))
#créer l2 qui contient les carrée des valeurs de l1
l2=[]
for x in l1:
    l2.append(x**2)
print("l1 =>",l1)
print("l2 =>",l2)

l3=[x**3  for x in l1]
print("l3 =>",l3)