import os

def exibir_nome():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n');

def exibir_opcoes():

    print('1. Cadastrar restaurante');
    print('2. Listar restaurante');
    print('3. Alternar status do restaurante');
    print('4. Sair\n');

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def clear_print(frase):
    os.system('cls')
    linha = '*' * len(frase)
    print(linha)
    print(f"{frase}")
    print(f'{linha}\n')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu()
restaurante = []


def cadastrar_novo_restaurante():
    clear_print('Cadastrar novo restaurante')
    nome_restaurante = input('Coloque o nome do restaurante: ')
    categoria_restaurante = input(f'Coloque a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante,'categoria': categoria_restaurante,'ativo':False}
    restaurante.append(dados_do_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado!!\n")
    voltar_menu()

def listar_restaurante():
    clear_print('Aqui esta a lista dos restaurantes:')
    print(f'{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status\n')
    for i in restaurante:
        nome_restaurante = i['nome']
        categoria_restaurante = i['categoria']
        status_restaurante = 'ativado' if i['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')
    voltar_menu()

def ativar_restaurante():
    clear_print('Ativação/Desativacao do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_foi_encontrado = False
    for i in restaurante:
        if nome_restaurante == i['nome']:
            restaurante_foi_encontrado = True
            i['ativo'] = not i['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!!' if i['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!!'
            print(mensagem)
            break
    if not restaurante_foi_encontrado:
        print('O restaurante não foi encontrado!!')
        
    voltar_menu()

def encerrar():
    clear_print("Finalizando app!")

def opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()   
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            encerrar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    opcoes()

    
if __name__ == '__main__':
    main()
