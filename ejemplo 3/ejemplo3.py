import random
import time

numeros = (random.randint(0,10))

acierto = False

    
print("escribe tu numero del 1 al 10")
a = input
   

while (not acierto):
    if a == numeros:
        print ("acertaste")
        acierto = True
        break

"""

Como comprobar el software:

print("Introduce un numero:  ")
a=input()   # Recogemos un caracter del teclado. 
print(a)    # Python considera los caracteres los datos de teclado... y un caracter no es un numero
b=a*6
print(b)    #curiosos, verdad?  como piensa que es una letra la multiplica aaaaaaaaa
a=int(a)    # Aqui conviertes la letra en numero entero (int)
a=a*9       # ahora 'a' ya es un numero para tu ordenador y puedes hacer mantematicas con 'a'
print(a)


"""
        
        
    
    
