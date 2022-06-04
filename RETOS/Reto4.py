def calcularCosto (alto, ancho, profundo):
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
        costo=costo+2000
        if costo>10000 :
            costo=costo*1.19
    elif(costo>10000):
        costo=costo*1.19
    return costo

def costoTotal(numeroPaquetes, descuento):
    costoTotal=0
    descu=1-descuento/100
    for i in range(numeroPaquetes):
        costoTotal+= calcularCosto(alto = float(input()), ancho = float(input()), profundo = float(input()))
    costoDef=costoTotal*descu
    return costoDef
print(calcularCosto(35,10,5))
print(costoTotal(2, 50))
