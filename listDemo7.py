#string => list (toujours realisable)
s="bonjour"


l=list(s)
l.append(" le monde!")
#l.insert(2,60)
print(l)
#list => string (realisable si les lements de la liste sont des strings)
res="".join(l)
print(res)