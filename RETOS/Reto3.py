""" 
numeroPaquetes = int(input()) 
costoTotal=0
for i in range(1, numeroPaquetes+1):
    alto = float(input())
    ancho = float(input())
    profundo = float(input())
    volumen=alto*ancho*profundo
    costo=volumen*5
    print(volumen)
    if alto>30:
        costo=costo+2000
        if costo>10000 :
            costo=costo*1.19
            print (costo)
        else:
            print(costo)
    elif(costo>10000):
        costo=costo*1.19
        print(costo)
    else:
        print(costo)
    costoTotal=costoTotal+costo
    i+=1
print(costoTotal) """

#con msj
numeroPaquetes = int(input("num paque")) 
costoTotal=0

for i in range(1, numeroPaquetes+1):
    print("Paquete",i)
    alto = float(input("alto en paquete"))
    ancho = float(input("Ancho en paquete"))
    profundo = float(input("profu en paquete"))
    volumen=alto*ancho*profundo
    costo=volumen*5
    print("este es el volumen: ",volumen)
    if alto>30:
        costo=costo+2000
        if costo>10000 :
            costo=costo*1.19
            print ("costo",costo)
        else:
            print("costo",costo)
    elif(costo>10000):
        costo=costo*1.19
        print("costo",costo)
    else:
        print("costo",costo)
    costoTotal=costoTotal+costo
    i+=1
print("costo total: ",costoTotal )