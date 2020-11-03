#prueba 6

#creo las variables
lista1 = []
lista2 = []
lista3 = []
lista4 = []
contador = 0
contador1 = 0

#creo el array de 100 numeros
for x in range (101):
    lista1.append(x)

for x in range (101):
    if (lista1[x]%2 == 0):
        lista2.append(lista1[x])
        contador = contador+1

for x in range (contador):
    if (lista2[x]%4 == 0):
        lista3.append(lista2[x])
        contador1 = contador1+1
      
for x in range (contador1):
    if (lista3[x]%5 == 0):
        lista3[x]= "*"
 
for x in range (contador):
    if (lista4[x]%2 == 1):
        lista3.append(x)

print (lista3)

