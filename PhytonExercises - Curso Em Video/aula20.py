# FUNÇÕES - Rotina (ex. print, float, len, input, int - todas elas são uma função, uma funcionalidade. Elas já existem e tem um objetivo especifico)

# Eu posso por ex criar uma função para imprimir as linhas de divisão inseridas nos códigos de exercicio feito anteriormente.

# def significado de definição de função

####################### 1 #############
def mostraLinha():
    print('--'*20)


# programa principal
mostraLinha()
# quando a função é chamada, ele retorna para as linhas de definição e executa o código

###################### 2 ##############


def mensagem(msg):  # msg é o parametro declarado na chamada da função, nas linhas abaixo
    print('----')
    print(msg)
    print('----')


# programa principal
mensagem('SISTEMA DE ALUNOS')

#################### 3 ##############


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
# a chamada dessa função só vai funcionar se receber dois parametros, pq foi a forma como ela foi definida. Nem menos e nem a mais
soma(b=10, a=9)
# eu posso alterar os valores dos parametros da forma que eu quiser, só preciso explicitar entre os parenteses


def contador(*núm):
    print(núm)
    # empacotamento. o asterisco signifca que ele vai receber quantos parametros for recebido na chamada da função


contador(2, 1, 7)
contador(9, 7)
contador(1, 2, 3, 4, 5)
# resultados em tupla
