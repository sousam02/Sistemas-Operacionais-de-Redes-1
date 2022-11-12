#!/usr/bin/env python
import cgitb, cgi
import render
import math


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

circ_abdominal_ = float(form.getvalue('circ_abdominal'))
sexo = form.getvalue('sexo')
data = []

match sexo:
        case 'masculino':
            if circ_abdominal_ <= 90:
                data.append('bg-info')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é normal, continue assim!')
            elif circ_abdominal_ > 90 and circ_abdominal_ < 94:
                data.append('bg-success')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é médio, previna-se!')
            elif circ_abdominal_ >= 94 and circ_abdominal_ < 102:
                data.append('bg-warning')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é alto, tome cuidado com sua saúde!')
            elif circ_abdominal_ >= 102:
                data.append('bg-danger')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é muito alto, procure ajuda profissional!')
        case 'feminino':

            if circ_abdominal_ <= 80:
                data.append('bg-info')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é normal, coninue assim!')
            elif circ_abdominal_ > 80 and circ_abdominal_ < 84:
                data.append('bg-success')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é médio, previna-se!')
            elif circ_abdominal_ >= 84 and circ_abdominal_ < 88:
                data.append('bg-warning')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é alto, tome cuidado!')
            elif circ_abdominal_ >= 88:
                data.append('bg-danger')
                data.append('De acordo com sua circunferência abdominal, seu risco de doença cardíaca é muito alto, procure ajuda profissional!')





render.template_tela(data)