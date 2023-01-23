def leiaInt(msg):
    """
    -> Faz a validação de um número e só o retorna se ele for inteiro.
    :param: msg: Mensagem que informa ao usuário o que deve ser digitado.
    :return: Retorna o valor n se, somente se, ele for Inteiro.
    """
    while True:
        try:
            n = int(input(msg))                     
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número INTEIRO válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usúario preferiu não informar esse valor.\033[m')
            return 0
        else:
            break
    return n
    
    
def linha(tam=42):
    return '-' * tam
    
    
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
    
def menu(lista):
    cabecalho('MENU')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[36m{item}\033[m')    
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
    