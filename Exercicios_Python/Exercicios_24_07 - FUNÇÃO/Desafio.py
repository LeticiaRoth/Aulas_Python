def armazenar_dados():
    #Dados inseridos na lista
    habitantes = [
        {"Nome": "Letícia", "Sexo": "F", "Esporte favorito": "Futebol", "Idade": 18},
        {"Nome": "Layslla", "Sexo": "F", "Esporte favorito": "Vôlei", "Idade": 19},
        {"Nome": "Mateus", "Sexo": "M", "Esporte favorito": "Tênis", "Idade": 11},
        {"Nome": "Leonardo", "Sexo": "M", "Esporte favorito": "Natação", "Idade": 13},
    ]
    return habitantes

def aviso_nenhum_homem_natacao():
    print("Não há nenhum homem que goste de natação!")

def calcular_media_homem_natacao(habitantes):
    homens_natacao = [h for h in habitantes if h["Sexo"] == "M" and h ["Esporte favorito"] == "Natação"]

    if homens_natacao:
        soma_idades = sum(h["Idade"] for h in homens_natacao)
        media_idade = soma_idades / len(homens_natacao)
        print(f"Idade média dos homens que gostam de natação: {media_idade}")
    else:
        aviso_nenhum_homem_natacao()


habitantes = armazenar_dados()
calcular_media_homem_natacao(habitantes)