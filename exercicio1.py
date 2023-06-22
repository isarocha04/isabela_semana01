

def multiplas_operacoes(a,b):
    soma = a+b
    sub = a-b
    mult = a*b

    if b==0:
        print("ERRO - Divisao por zero")
        print("Soma = ", soma)
        print("Subtracao = ", sub)
        print("multiplicacao = ",mult)   
    else:
        div = a/b
        print("Divisao = ",div)
        print("Soma = ", soma)
        print("Subtracao = ", sub)
        print("multiplicacao = ",mult)   


multiplas_operacoes(1,2)
