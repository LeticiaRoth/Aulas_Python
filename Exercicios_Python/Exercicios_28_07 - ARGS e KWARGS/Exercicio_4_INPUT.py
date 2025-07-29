def numeroMaior(*args):
    if not args:
        return "Nenhum argumento"
    return max(args)

#Input colocado pelo usuário
entrada=input("Digite vários números separado:")

#Conversão para uma litsa
lista_numeros = [float(num) for num in entrada.split()]

maior =numeroMaior(*lista_numeros)
print(f"Número maior:{maior}")