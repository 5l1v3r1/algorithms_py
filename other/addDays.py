# algorithm for adding days to a specific date (DD/MM/YYYY), variable and function names are in portuguese

meses_dias = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
'11': 30, '12': 31}

def addDias(data_atual, dias):
    (dia, mes, ano) = tuple([int(i) for i in data_atual.split('/')])
    dia += dias

    while dia > meses_dias[str(mes)]:
        print(mes)
        dia -= meses_dias[str(mes)]
        mes += 1
        if mes > 12:
            ano += 1
            mes = 1

    return f'{dia}/{mes}/{ano}'

data = '01/01/2020'
print(addDias(data, 200))