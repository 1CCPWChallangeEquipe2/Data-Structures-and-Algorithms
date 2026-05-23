def calculate_cost(full_energy, type):
    cost = full_energy * 0.75
    if type == 2:
        descont = cost * 0.10
    else:
        descont  = 0
    cost_final = cost - descont + 0.50
    return cost_final

def simulate_recharge(current_load, final_load, type):
    potency = 7.5
    total = final_load - current_load
    
    if total != 0:
        cost = calculate_cost(total, type)
        minutes = total/potency

        return minutes, cost
    else:
        return 0, 0

def format_minutes(time):
    minutes = int(time)
    seconds = int((time - minutes) * 60)

    return f"{minutes}min{seconds}s"


print("============================================")
print("       Iniciando o sistema de recarga       ")
print("============================================")

name = input("Digite seu nome: ")

type_error = ''
while True:
    try: 
        type = int(input(f"""{type_error}Digite o tipo do seu usuário:
    1 - Padrão
    2 - Premium
Tipo: """))
            
        if type not in (1, 2):
            raise
        break
    except:
        type_error = '\nTIPO DE USUÁRIO INVÁLIDO! Tente novamente!\n'

capacity_error = ''
while True:
    try: 
        capacity = float(input(f"{capacity_error}Digite a capacidade da bateria (em kW): "))
        if capacity < 0:
            capacity_error = '\nDIGITE UM VALOR MAIOR OU IGUAL A 0! Tente novamente!\n'
            raise
        break
    except:
        capacity_error = '\nDIGITE UM VALOR NUMÉRICO VÁLIDO! Tente novamente!\n'

current_load_error = ''
while True:
    try: 
        current_load = float(input(f"{current_load_error}Digite sua carga atual (em kW): "))

        if current_load > capacity:
            current_load_error = '\nDIGITE UM VALOR NÃO PODE SER MAIOR QUE A CAPACIDADE! Tente novamente!\n'
            raise

        elif current_load < 0:
            current_load_error = '\nDIGITE UM VALOR MAIOR OU IGUAL A 0! Tente novamente!\n'
            raise

        break
    except:
        current_load_error = '\nDIGITE UM VALOR NUMÉRICO VÁLIDO! Tente novamente!\n'

final_load_error = ''
while True:
    try: 
        final_load = float(input(f"{final_load_error}Digite a carga final desejada (em kW): "))
        if final_load < current_load:
            final_load_error = '\nA CARGA FINAL DEVE SER MAIOR QUE A CARGA ATUAL! Tente novamente!\n'
            raise
        
        elif final_load > capacity:
            current_load_error = '\nDIGITE UM VALOR NÃO PODE SER MAIOR QUE A CAPACIDADE! Tente novamente!\n'
            raise

        break
    except:
        final_load_error = '\nDIGITE UM VALOR NUMÉRICO VÁLIDO! Tente novamente!\n'


minutes, cost = simulate_recharge(current_load, final_load, type)

print("\n============================================")
print("            Relatório da recarga            ")
print("============================================")
print(f"Nome: {name}")

if type == 1:
    print(f"Tipo: Padrão")
else:
    print(f"Tipo: Premium")

print(f"Tempo experado de recarga: {format_minutes(minutes)}")
print(f"Total de energia consumida: {(current_load-final_load):.2f} kW")
print(f"Custo: R$ {cost:.2f}")

print("\n============================================")
print("       Sistema de recarga Finalizado        ")
print("============================================")
