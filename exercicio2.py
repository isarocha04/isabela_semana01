

def cumulativo(lista):
    for i in range(1, len(lista)):
        lista[i] += lista[i-1]
    print(lista)
    return lista
    
cumulativo([1,2,3])
