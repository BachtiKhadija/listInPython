s="bonjour"
#on peut récupérer une valeur en utilisant l'indexing
#s[1]='a' # error 
print(s[1]) # affiche 'o'
#on peut récupérer une tranche en utilisant slicing
#nom_chaine[start:stop:step]

slice1=s[1:4:2] # => tranche de 1 => 4-1  "onj"
print(slice1)
slice2=s[1:6] #step par defaut 1  => 1 : 6-1
print(slice2)

slice3=s[5:2:-1]
print(slice3)