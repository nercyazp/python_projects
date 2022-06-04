alto = float(input())
ancho = float(input())
profundo = float(input())
volumen=alto*ancho*profundo
costo=volumen*5
print(volumen)
if alto>30:
    costofinal=costo+2000
    if costofinal>10000 :
        costofinal=costofinal*0.19+costofinal
        print (costofinal)
    else:
        print(costofinal)
elif(costo>10000):
    costofinal=costo*0.19+costo
    print(costofinal)
else:
    print(costo)








