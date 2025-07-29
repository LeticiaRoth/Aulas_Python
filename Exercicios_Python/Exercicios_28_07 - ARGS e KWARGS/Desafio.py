def corrida(p1, p2, p3, **kwargs):
    # Monta a lista
    posicoes = [p1, p2, p3]
    # A ordem das chaves dos kwargs
    ordem_chaves = ['quarto', 'quinto', 'sexto']
    for chave in ordem_chaves:
        if chave in kwargs:
            posicoes.append(kwargs[chave])
        else:
            posicoes.append(None)  # Caso falte

    print("\nClassificação inicial:")
    for i, corredor in enumerate(posicoes, start=1):
        print(f"{i}º lugar: {corredor}")

    # Pergunta sobre trapaça
    resposta = input("\nHouve trapaça? (sim/não): ").strip().lower()

    if resposta == 'sim':
        trapaceiro = input("Quem trapaceou? (siglas MC, PL, SN, FS, LG, SH): ").strip().upper()
        prejudicado = input("Quem foi prejudicado? (siglas MC, PL, SN, FS, LG, SH): ").strip().upper()

        # Verifica se ambos estão na lista
        if trapaceiro in posicoes and prejudicado in posicoes:
            i_trap = posicoes.index(trapaceiro)
            i_prej = posicoes.index(prejudicado)

            # Troca de posições
            posicoes[i_trap], posicoes[i_prej] = posicoes[i_prej], posicoes[i_trap]

            print("\nClassificação após a troca:")
            for i, corredor in enumerate(posicoes, start=1):
                print(f"{i}º lugar: {corredor}")
        else:
            print("Um ou ambos os corredores não estão na lista da corrida. Nenhuma alteração feita.")

    else:
        print("\nNenhuma trapaça detectada. Classificação final:")

        for i, corredor in enumerate(posicoes, start=1):
            print(f"{i}º lugar: {corredor}")


#Uso do input
print("Digite os corredores na ordem do vencedor ao último (use as siglas):")
p1 = input("1º lugar: ").strip().upper()
p2 = input("2º lugar: ").strip().upper()
p3 = input("3º lugar: ").strip().upper()

print("\nTrês últimos lugares:")
q = input("4º lugar: ").strip().upper()
qi = input("5º lugar: ").strip().upper()
s = input("6º lugar: ").strip().upper()

corrida(p1, p2, p3, quarto=q, quinto=qi, sexto=s)
