

def tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]==lista[j]:
                print(True)
                return True
    print(False)
    return False


tem_duplicados([1,2,3,4])
