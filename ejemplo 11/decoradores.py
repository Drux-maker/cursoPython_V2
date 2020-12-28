def decorador(funcion):
    def funcionDecorada(*args, **kwargs):
        print ("Funcion ejecutada", funcion.__name__)
        funcion(*args, **kwargs)

    return funcionDecorada

@decorador
def resta(n,m):
    return n-m


print (resta(3,5))
