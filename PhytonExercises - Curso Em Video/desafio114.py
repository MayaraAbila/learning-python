import json
import urllib3
import urllib.request


def site():
    try:
        urllib.request.urlopen("https://www.youtube.com/").getcode()
    except:
        print('Não consegui acessar o site! =(')
    else:
        print('Consegui acessar o site com sucesso! =D')


site()
