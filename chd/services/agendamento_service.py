from datetime import datetime, timedelta, date, time
import random
import database

def gerar_agendamento():
    hoje = date.today()

    dias_aleatorios = random.randint(1, 365)
    dia_agendado = hoje + timedelta(days= dias_aleatorios)
    
    horas_aleatorias = random.randint(8, 18)
    horario_agendao = time(horas_aleatorias, 0, 0)

    data_agendada = datetime.combine(dia_agendado, horario_agendao)

    return str(data_agendada)

def gerador_de_agendamentos_validos(dados=None):
    if dados is None:
        dados = database.carregar_pacientes()

    while True: 
        agendamento = gerar_agendamento()
        encontrado = False

        for valor in dados.values():
            if valor["agendamento"] == agendamento:
                encontrado = True
                break

        if not encontrado:
            return agendamento
        

