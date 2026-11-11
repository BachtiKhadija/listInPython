l=list(range(0,30))
print(l)
#l2 > contient les elemnts paires de l 
l2=list() #[]
for x in l:
    if x%2==0:
        l2.append(x)
print(l2)

#[x for x in l if x%2==0]

l3=[x for x in l if x%2!=0]

print(l3)