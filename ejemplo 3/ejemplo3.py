import random
import time

numeros = (random.randint(0,10))

acierto = False

   
print("escribe tu numero del 1 al 10")
#print(numeros)

a = input()

a = int(a)
       

while (not acierto):
    if (a == numeros):
        print ("acertaste")
        acierto = True
        break
    else:
        print ("escribe otro numero")
        a = input()
        a = int(a)

            
        
        
    
    
