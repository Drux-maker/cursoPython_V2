#prueba7
#la diferencia entre el while y el for es que el for es un numero de veces y el while es siempre que se cumpla la condicion 
#creo las variables
lista1 = []
contador = 0
listanoprimos = []
listaprimos = []

#creo el arrray con 100 numeros
for x in range (101):
    lista1.append(x)
print ("Array original: \n", lista1)
#aqui igualo x a cero     

#x = 1
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
for x in range (1,11):
    
    for y in range (1,x):
        print ("valor de x e y ",x,y)
        if lista1[x] < 2:
            listanoprimos.append(lista1[x])        
        if((lista1[x]%lista1[y]) == 0):
           listanoprimos.append(lista1[x])
           break
        else :
            listaprimos.append(lista1[x])
            

  

print ("Array no primos", listanoprimos)
print ("Array primos", listaprimos)

""" 
if (((lista1[x]%lista1[x]) == 0) and ((lista1[x]%1) == 0)):
        print (lista1[x])
"""
