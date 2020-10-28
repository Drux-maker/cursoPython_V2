#prueba 4
import random


#hago la variable 
#numeros = (random.randint(0,101))
lista1 = []
lista2 = []
lista3 = []

# creo un array o lista de 100 nuemros consecutivos

for x in range (101):
    lista1.append(x)
#print (lista1)

#creo otro array copiando
for x in range (101):
    lista2.append(0)
    lista2[x] = lista1[x]
#print (lista2)
        
#copio los numeros pares en el array 2
"""    
for x in range (101):
    lista3.append()
    if (lista2[x]%2 == 0):
        lista3[x] = lista2[x]
print (lista3)
"""


for x in range (101):
    if (x%2 == 0):
        lista3.extend(x)
print (lista3)
    
    
        
    
