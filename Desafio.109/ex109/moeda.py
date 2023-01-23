def metade(valor=0, formato=False):
    """
    -> Calcula a metade de um valor.
    :param: valor: Valor a ser dividido.
    :param: formato: Decide se adicionará ou não o símbolo de moeda ao valor.
    :return: Retorna a metade do valor com ou sem formatação de moeda.
    """
    res = valor / 2
    return res if formato is False else moeda(res)
    
    
def dobro(valor=0, formato=False):
    """
    -> Calcula o dobro de um valor.
    :param: valor: Valor a ser dobrado.
    :param: formato: Decide se adicionará ou não o símbolo de moeda ao valor.
    :return: Retorna o dobro do valor com ou sem formatação de moeda.    
    """
    res = valor * 2
    return res if formato is False else moeda(res)
    
        
def aumentar(valor=0, perc=0, formato=False):
    """
    -> Adiciona porcentagens especificas ao valor.
    :param: valor: Valor a ser aumentado.
    :param: perc: Porcentagem a ser adicionada.
    :param: formato: Decide se adicionará ou não o símbolo de moeda ao valor.
    :return: Retorna o valor com a porcentagem adicionada.
    """
    res = valor + (valor * perc / 100)
    return res if formato is False else moeda(res)
    
                    
def diminuir(valor=0, perc=0, formato=False):
    """
    -> Diminui uma porcentagem especifica do valor.
    :param: valor: Valor de onde a porcentagem será tirada.
    :param: perc: Porcentagem a ser diminuida.
    :param: formato: Decide se adicionará ou não o símbolo de moeda ao valor.
    :return: Retorna o valor já sem a porcentagem.
    """
    res = valor + (valor * perc / 100)
    return res if formato is False else moeda(res)
 
  
def moeda(valor=0, moeda='R$'):
    """
    -> Adiciona o Símbolo de uma moeda a um valor.
    :param: valor: Valor a quem o símbolo será adicionado.
    :param: moeda: Símbolo de moeda que será adicionado ao valor.
    :return: Retorna o valor já com o símbolo informado.
    """
    return f'{moeda}{valor :.2f}'        
    