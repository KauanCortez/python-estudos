def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
        
    
def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo.')
    else:
        print(f'Arquivo {arq} criado com sucesso.')
        
        
def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um ERRO ao ler o aquivo.') 
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()  
    print('  ')

           
def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')    
    except:
        print('Houve um ERRO ao escrever os dados.')        
    else:
        a.write(f'{nome};{idade}\n')
        print('  ')
        print(f'Novo Registro de {nome} criado com sucesso.')
        a.close()          
        print('  ')