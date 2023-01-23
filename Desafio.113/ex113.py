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

   
def leiaFloat(msg):
    """
    -> Faz a validação de um número e só o retorna se ele for Real.
    :param: msg: Mensagem que informa ao usuário o que deve ser digitado.
    :return: Retorna o valor de n se, e somente se, ele for Real.
    """
    while True:
        try:
            r = float(input(msg))
        except ValueError:
            print('\033[31mERRO: Por favor, digite um número REAL válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usúario preferiu não informar esse valor.')
            r = 0
        else:
            break
    return r
    