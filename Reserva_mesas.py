#O menu é basico, com uma proteção para caso o usuário digite algo diferente de uma opção existente. 

def menu():
    while True:
        print('''
        1 - Reservar mesas
        2 - Remover reserva
        3 - Mostrar reservas
        4 - Alterar a reserva
        5 - Sair
        ''')
        try:
            opcao = int(input('Digite o que quer fazer: '))
            return opcao
        except:
            print('opção inválida')



def reservar_mesa(reservas):
    nome=input('Digite seu nome: ')
    numero_lugares=input('Quantas pessoas ocupariam a mesa: ')
    if nome == "" or nome == None:
        print('Nome invalido, digite novamente!')
    else:
        if nome in reservas:
            print('Já tem uma reserva em seu nome.')
        else:
            reservas.append(nome)
# abaixo o código da um premio a décima reserva.
    if len(reservas) % 10 ==0:
        for i in range( len(reservas)):
            x=reservas[i]
            if x == nome:
                print(f'A mesa em nome de {nome}, de numero {i+1}, foi premiada com uma sobremesa gratuita')
                break    
    return reservas

def remover_mesa(reservas):
    print(reservas)
    nome=input('Digite seu nome: ')
    if nome == "" or nome == None:
            print('Nome invalido, digite novamente!')
    else:   
        for i in range( len(reservas)):
            x=reservas[i]
            print(x)
            if x == nome:
                print(f'A mesa em nome de {nome}, de numero {i+1}, foi removida das reservas')
                reservas.remove(nome)
                break
    return reservas

def mostrar_reservas(reservas):
    print(f'Reservas para o dia: {reservas}')

def alterar_reservas(reservas):
    print(reservas)
    nome=input('Digite em nome de quem está a reserva: ')
    if nome in reservas:
        novo_nome=input('Digite o novo nome da reserva: ')
        for i in range( len(reservas)):
            x=reservas[i]
            if x == nome:
                reservas[i]=novo_nome
    return reservas

def main():
    reservas=[]
    while True:
        opc=menu()
        if opc >= 1 and opc <= 5:
            if opc == 1:
                reservas=reservar_mesa(reservas)
            elif opc == 2:
                reservas=remover_mesa(reservas)
            elif opc == 3:
                mostrar=mostrar_reservas(reservas)
            elif opc == 4:
                reservas= alterar_reservas(reservas)
            elif opc == 5:
                break
        else:
            print('opção inválida')

main()
