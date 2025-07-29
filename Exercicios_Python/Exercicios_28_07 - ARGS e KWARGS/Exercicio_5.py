def mediaValor(**kwargs):
    valores = kwargs.values()
    media = sum(valores) / len(valores)
    return f"{media:.2f}"

print(mediaValor(num1=3, num2=4, num3=6, num4=7, num5=8))  # Saída: 5.60
#Eles são nomeados por isso deve ser kwargs
