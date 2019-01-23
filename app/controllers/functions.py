from random import randint
from datetime import date

def shufflebg():
    x = randint(1, 5)
    if x == 1:
        return "bg"
    if x == 2:
        return "bg1"
    if x == 3:
        return "bg2"
    if x == 4:
        return "bg3"
    return "bg"


def strToDate(s):
    dia = s[0:2]
    mes = s[3:5]
    ano = s[6:10]

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    return date(ano, mes, dia)


def dateToStr(d):
    return "%i/%.2i/%i" % (d.day, d.month, d.year)

def trataCpf(cpf):
    r = ""
    for letra in cpf:
        if '9' >= letra >= '0':
            r+=letra

    return r

