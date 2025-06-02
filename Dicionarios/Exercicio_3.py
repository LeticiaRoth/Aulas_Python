pessoa ={
    "nome": "Carlos",
    "idade": 40,
    "cidade": "Belo Horizonte"
}

del pessoa["idade"]
valores = pessoa.values()
print(list(valores))