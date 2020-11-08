#prueba7
#la diferencia entre el while y el for es que el for es un numero de veces y el while es siempre que se cumpla la condicion 
#creo las variables
lista1 = []
contador = 0


#creo el arrray con 100 numeros
for x in range (11):
    lista1.append(x)
print ("Array original: \n", lista1)
#aqui igualo x a cero     
#x = 0
#aqui imprimo los numeros 1 a 1 hasta el tope
"""while (lista1[x] < 100):
    print (lista1[x])

    x = x+1
    if x == 21:
        break
        
for x in range (101):
    print (lista1[x])
    contador = contador+1

#este for lo que hace es quitar los numeros que se poueden dividir entre tres
#OJO: la funcion remove quita elemntos de la lista por lo que nunca llega a 100   
for x in range (101):
    #print (x)
    if ((lista1[x]%3) == 0):
        lista1.remove(lista1[x])
        #print (lista1)
    if (lista1[x] == 100):
        break

print ("Array final: \n", lista1)
"""
for x in range (4):

    if (lista1[x] < 2):
        lista1.remove(lista1[x])
        lista1.remove(lista1[0])  


    else:
        for x in range(2):
            if ((lista1[x] % lista1[x]) == 0):
                lista1.remove(lista1[x])


print ("Array primos", lista1)


