#prueba 6


lista1 = []
lista2 = []
lista3 = []
lista4 = []

#creo el array de 100 numeros
for x in range (101):
    lista1.append(x)

for x in range (101):
    if (lista1[x]%2 == 0):
        lista2.append(lista1[x])
        
for x in range (101):
    if (lista2[x]%4 == 0):
        lista3.append(lista2[x])

for x in range (101):
    if (lista3[x]%5 == 0):
        lista4.append(lista3[*])
print (lista4)
