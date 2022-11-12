#!/usr/bin/env python
import cgitb, cgi
import render
import math


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

peso_ = float(form.getvalue('peso'))
altura_ = (float(form.getvalue('altura')))/100

imc = peso_ / pow(altura_,2)
data = []


if imc >= 18.5 and imc < 25:
    data.append('bg-success')
    data.append('O seu IMC indica que está no peso ideal!')
elif imc >= 25 and imc < 30:
    data.append('bg-warning')
    data.append('O seu IMC indica que está com sobrepeso, cuide-se!')
elif imc >= 30 and imc < 40:
    data.append('bg-warning')
    data.append('O seu IMC indica que está com obesidade, comece a se cuidar!')
elif imc >= 40:
    data.append('bg-danger')
    data.append('O seu IMC indica que está com obesidade severa, busque ajuda profissional!')
else:
    data.append('bg-info')

render.template_tela(data)


# calcular area



############ HTML
