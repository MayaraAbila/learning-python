from operator import length_hint


def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit == True:
        if r['media'] < 7:
            r['situacao'] = 'Reprovado'
        else:
            r['situacao'] = 'Aprovado'
    return r


#print(notas(3, 4, 6, 7, sit=True))
help(notas)
