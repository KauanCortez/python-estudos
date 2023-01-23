def acessivel(msg):
    import requests
    
    site = str(input(msg))
    try:
        requests.get(site)
    except:
        return f'\033[0;31mO site {site}\nnão está acessível no momento. :( \033[m'
    else:
        return f'\033[0;33mConsegui acessar o site {site}\ncom sucesso!. :)\033[m'
        