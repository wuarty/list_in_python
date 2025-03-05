import os

lista = []
while True:
    print('Selecione uma opção:')
    opcao = input(
        '1 - Adicionar itens\n2 - Deletar itens\n3 - Listar itens\n4 - Sair\n')

    if opcao == '1':
        os.system('clear')
        valor = input('Digite o valor: ')
        lista.append(valor)
    elif opcao == '2':
        indice_str = input('Digite o índice do item que deseja deletar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível deletar o item')
    elif opcao == '3':
        os.system('clear')
        
        if len(lista) == 0:
            print('Não há itens na lista')
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
        print('Listar itens')
    elif opcao == '4':
        sair = input('Quer sair? Aperte [4] ').lower().startswith('4')
        print('Saindo...')
        break
    else:
        print('Por favor, escolha uma opção válida')
    