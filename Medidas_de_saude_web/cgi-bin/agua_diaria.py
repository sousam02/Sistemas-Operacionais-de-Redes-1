#!/usr/bin/env python
import cgitb, cgi
import render
import math


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

peso_ = float(form.getvalue('peso'))

agua_diaria = peso_ * 0.035
data = []
data.append('bg-info')
resultado = "De acordo com seu peso, você deve tomar {:.2f} Litros de água diariamente.".format(agua_diaria)
data.append(resultado)



render.template_tela(data)


# calcular area



############ HTML
