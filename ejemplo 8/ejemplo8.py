

lista1 = []
primos = []
Noprimos = []

for x in range(100):
    lista1.append(x)


for x in range(100):
    for y in range (x,1,-1):
        if ((x == y)):
            continue
        #a=lista1[x]
        #b=lista1[y]
        if (lista1[x]%lista1[y] ==0):
            Noprimos.append(lista1[x])
            break
        if y==2:
            primos.append(lista1[x])    
print (primos)
