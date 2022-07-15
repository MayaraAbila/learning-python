def voto(idade):
    # escopo de importação. Utiliza menos memória.
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return "Não Vota"
    if 16 <= idade <= 17 or idade > 70:
        return "Voto Facultativo"
    else:
        return "Voto Obrigatório"


ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
