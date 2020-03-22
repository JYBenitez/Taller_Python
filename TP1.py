aNumeros=[]
aMulti4=[]
iSumNegativos=0
iCant=0
iCantMulti4=0
iCantPar=0
iCantMulti3=0
iNumero = 0
txtPositivo="Por favor ingrese un valor mayor o igual a cero(0):\n"
txtNegativo="Por favor ingrese un valor menor a cero(0):\n"
txt=txtPositivo
iCantMax=10
iCantMitad=iCantMax/2

def cargarVector(vector, numero):
    vector.append(numero) 
    return

def ordenarVectorCreciente(vector):
    order = sorted(vector,reverse=False)
    return order

def calcularPromedio(numero, cant):
    if cant ==0:
        print("Error! no se puede dividir por cero")
    else:
        return numero / cant
    return

def esMultiplo(valor, multiplo):
    if multiplo ==0:
        print("Error! no se puede dividir por cero")
    else:
        return valor%multiplo
    return

print("Se deben ingresar %d numeros enteros.\nEn primer lugar se ingresaran %d valores positivos; luego, %d negativos.\nUna vez cargados, se mostrara los resultados." %(iCantMax,iCantMitad, iCantMitad))

while iCant < iCantMax:
    iNumero = int(input(txt))
    if (iNumero >= 0 and iCant < iCantMitad) or (iNumero < 0 and iCant >= iCantMitad):
        cargarVector(aNumeros, iNumero)
        if iNumero < 0:
            iSumNegativos+=iNumero
        if iNumero < 0 and esMultiplo(iNumero,4) == 0:
            cargarVector(aMulti4,iNumero)
            iCantMulti4+=1
            if esMultiplo(iNumero,3) == 0:
                iCantMulti3+=1
            if esMultiplo(iNumero,2)==0:
                iCantPar+=1                
        iCant+=1  
        if iCant == iCantMitad:
            txt=txtNegativo  
print ("Promedio de los numeros negativos es:%d " %(calcularPromedio(iSumNegativos,iCantMitad)))
print ("Vector ordenado ascendente:")
aNumeros=ordenarVectorCreciente(aNumeros)
for i in range(iCantMax):
    print("elemento %d, valor: %d" %(i, aNumeros[i])) 
if iCantMulti4>0:
    print ("Vector con multiplos de 4:")
    for i in range(iCantMulti4):
        print("elemento %d, valor: %d" %(i, aMulti4[i])) 
else :
    print ("No se ingresaron multiplos de 4")
if iCantMulti3 > 0:
    print ("Se ingresaron %d multiplos de 4 y 3" %iCantMulti3)
if iCantPar > 0:
     print ("Se ingresaron %d multiplos de 4 y numero par" %iCantPar)

