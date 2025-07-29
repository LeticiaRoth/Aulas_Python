def numeroMaior(*args):
    if not args:
        return "Nenhum argumento"
    return  max(args)

print(numeroMaior(45,90,23,1))
print(numeroMaior())