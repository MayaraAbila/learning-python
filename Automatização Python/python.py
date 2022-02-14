import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib

meu_arquivo = pd.read_excel(
    "/home/mayara/PycharmProjects/Automatização Python/MeuArquivo.xlsx")
print(meu_arquivo)

# for v in meu_arquivo['numero']:
#    print(v)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# enquanto ele não encontrar nenhum elemento com id 'side' (exclusivo do pós login na web, ele vai continuar esperando)
while len(navegador.find_elements_by_id("side")) < 1:
    sleep(1)

# vai localizar a pessoa e o seu indice
for i, mensagem in enumerate(meu_arquivo['Mensagem']):
    pessoa = meu_arquivo.loc[i, "Pessoa"]  # [linha, coluna]
    # print(pessoa)
    numero = meu_arquivo.loc[i, "numero"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = (f"https://web.whatsapp.com/send?phone={numero}&text={texto}")
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        sleep(5)
    navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    sleep(5)
