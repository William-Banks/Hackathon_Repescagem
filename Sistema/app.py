# Importação da biblioteca OS para facilitar a visualização do código e da biblioteca time para personalizar a inicialização
import os
import time

# Criação do dicionário responsável por armazenar os usuários e inicialização
usuarios = {}
os.system('cls')
print('Inicializando sistema...')
time.sleep(1)
os.system('cls')
print('3...')
time.sleep(1)
os.system('cls')
print('2...')
time.sleep(1)
os.system('cls')
print('1...')
time.sleep(1)
os.system('cls')

# Criação do ciclo responsável por exibir o menu de opções na tela
while True:
    print()
    print(10*'=', 'GERENCIADOR DE USUÁRIOS - Tech4U', 10*'=')
    print()
    print('-> 1. Adicionar Usuário')
    print('-> 2. Listar Usuários')
    print('-> 3. Editar Usuário')
    print('-> 4. Remover Usuário')
    print('-> 5. Sair do sistema\n')
    print(54*'=')
    
    # É aguardada a seleção de uma opção dentre as disponíveis

    opcao = input('\nEscolha a opção desejada: ')

    # Caso a opção selecionada seja 1, o sistema receberá o nome e idade do usuário e armazenará os dados recebidos dentro do dicionário de usuários

    if opcao == '1':
        os.system('cls')
        print(15*'-')
        nome = input('Digite o seu nome: ').upper()
        os.system('cls')
        print(15*'-')
        idade = int(input('Digite a sua idade: '))

        # Verifica-se se a idade recebida não é inválida e se o usuário já existe

        if idade >= 0 and idade < 120:
            if nome not in usuarios:
                usuarios[nome] = {'Nome' : nome, 'Idade' : idade}
                os.system('cls')
                print(f'O usuário {nome} foi cadastrado com sucesso!\n')
            else:
                print('O usuário já existe.')
        else:
            print('Idade inválida')

    # Caso a opção seja 2, será feita a exibição de todos os usuários cadastrados na tela

    elif opcao == '2':

        # Ele verifica se há usuários cadastrados

        if usuarios:

            # Com o for, ele percorre todo o dicionário contendo os usuários, permitindo exibir suas informações na tela

            for chave, dados in usuarios.items():
                print(25*'-')
                print(f"Nome: {dados['Nome']} , Idade: {dados['Idade']}")
        else:
            os.system('cls')
            print('Não há usuários cadastrados.\n')

    # Caso a opção seja 3, o sistema irá receber um nome de usuário que, caso esteja cadastrado, poderá receber uma nova idade

    elif opcao == '3':
        os.system('cls')

        # Recebimento do nome de usuário alvo

        user = input('Digite o nome do usuário que deseja atualizar: ').upper()
        if user in usuarios:

            # Aqui o sistema recebe a nova idade
            age = int(input('Digite a nova idade: '))
            
            # O sistema verifica se a idade é válida. Ele realiza a atualização caso seja válida

            if age >= 0 and age < 120:
                usuarios[user] = {'Nome' : user, 'Idade' : age}
            else:
                print('Idade inválida.')
        else:
            print('Usuário não cadastrado.')

    # Caso a opção seja 4 e o usuário que o sistema receber estiver no sistema, ele será excluído

    elif opcao == '4':
        os.system('cls')

        # Aqui o sistema recebe o nome do usuário alvo

        remover = input('Digite o usuário que deseja remover: ').upper()

        # Ele verifica se ele se encontra cadastrado no sistema e o deleta

        if remover in usuarios:
           del usuarios[remover]
           os.system('cls')
           print('Usuário removido com sucesso!\n')
        else:
            print('Usuário não cadastrado.')

    # Caso a opção seja 5 o sistema finalizará o processo

    elif opcao == '5':
        os.system('cls')
        print('Saindo do sistema...')
        break

    # Isso é impresso caso o número recebido na opção não seja válido dentre as disponíveis

    else:
        print('Opção inválida. Tente novamente.')