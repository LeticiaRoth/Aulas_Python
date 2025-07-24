import datetime

#Importa para mostrar o horário
mostrar_hora = datetime.datetime.now()

#Forma a hora para mostrar certo a hora, minutos e segundo
hora_formatada = mostrar_hora.strftime("%H:%M:%S")
print(f"Horário atual: {hora_formatada}")