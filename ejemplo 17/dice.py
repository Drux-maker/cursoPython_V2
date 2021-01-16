import time
from random import seed
from random import choice

print ("Tiras un dado que numero te tocara...")

time.sleep(1.75)

lista = []

for x in range(7):
    lista.append(x)

for x in range (1
                ):
    dado = choice(lista)
    print("Y el numero que te ha tocado es el",dado)

