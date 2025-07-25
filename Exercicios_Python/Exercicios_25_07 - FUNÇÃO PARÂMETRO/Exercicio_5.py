def encontrarLetra(lista):
    contador = 0
    #Procura a palavra na lista
    for palavra in lista:

        #Função para buscar as palavras que começam com a letra A
        if palavra.lower().startswith('a'):
            contador += 1
    return contador

lista = ["Amor", "Castelo", "Avião", "Ovo", "Filme", "Macaco"]
resultado = encontrarLetra(lista)

print(f"Palavras que começam com a letra A: {resultado}")

