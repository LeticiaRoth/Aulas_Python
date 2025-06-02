herois = {
    "Homem de Ferro" : 95,
    "Capitão América" : 97
}

armas_heroi = {
    "Armadura de alta tecnologia" : 87,
    "Escudo Vibranium" : 100
}

viloes = {
    "Thanos" : 100,
    "Loki" : 86
}

#Defino uma função para escolher o herói e arma
def luta():


    #Escolha do herói pelo usuário
    print("Escolha o seu herói:")
    for heroi in herois:
        print(f"-{heroi}")

    heroi_escolhido = input("\nDigite o nome do héroi:")

    if heroi_escolhido not in herois:
        print("Herói não encontrado!")
        return



    #Escolha da arma pelo usuário
    print("Escolha sua arma:")
    for armas in armas_heroi:
        print(f"- {armas}")

    arma_escolhida = input("\nDigite o nome da arma:")

    if arma_escolhida not in armas_heroi:
        print("Arma não encontrada")
        return



    #Escolha do vilão pelo usuário
    print("Escolha um vilão para batalhar:")
    for vilao in viloes:
        print(f"- {vilao}")

    vilao_escolhido = input("\nDigite o vilão desejado:")

    if vilao_escolhido not in viloes:
        print("Vilão não encontrado")
        return




    heroi_poder = herois[heroi_escolhido] + armas_heroi[arma_escolhida]
    vilao = viloes[vilao_escolhido]

    print("\nHÉROIS VS VILÕES")
    resultado = heroi_poder - vilao
    print(f"RESULTADO:{resultado}")

    if heroi_poder > vilao:
        print(f"{heroi_escolhido} VENCEU com a {arma_escolhida}")
    elif heroi_poder < vilao:
        print(f"{vilao_escolhido} VENCEU, GAME OVER")
    else:
        print(f"EMPATE, RESULTADO: {resultado}")

luta()