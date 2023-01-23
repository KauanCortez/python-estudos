def metade(valor):
    return valor / 2
    
    
def dobro(valor):
    return valor * 2
    
        
def aumentar(valor, perc = 0):
    porcentagem = valor * perc / 100
    return valor + porcentagem
    
                    
def diminuir(valor, perc = 0):
    porcentagem = valor * perc / 100
    return valor - porcentagem
 

def moeda(valor):
    return f'R${valor}'         
         