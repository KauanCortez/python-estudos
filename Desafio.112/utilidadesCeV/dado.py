def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            if entrada.isnumeric():
                valido = True
                return float(entrada)
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido.\033[m')
        else:            
            valido = True
            return float(entrada)
            