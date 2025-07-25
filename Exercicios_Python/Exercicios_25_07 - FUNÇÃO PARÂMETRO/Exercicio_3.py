def encontrarCaractere(texto, caractere):
    return texto.count(caractere)

frase = input("Digite a frase:")
caractere = input("Coloque o caractere que deseja encontrar:\n")
print(f"O caractere '{caractere}' aparece {encontrarCaractere(frase, caractere)} vezes.")



