import json
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

def costoTotal(listaPaquetes, descuento):
    costoTotal=0
    descu=1-descuento/100
    for paquete in listaPaquetes:
        costoTotal+= calcularCosto(paquete["ALTO"], paquete["ANCHO"], paquete["PROFUNDO"])
    costoDef=costoTotal*descu
    return costoDef

with open('paquetes.json') as file:
    empresa = json.load(file)
print (costoTotal(empresa['PAQUETES'], 10))
