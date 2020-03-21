print("Se deben ingresar 10 numeros enteros.\nEn primer lugar se ingresaran 5 valores positivos; luego, 5 negativos.\nUna vez cargados, se mostrara los resultados.")
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

while iCant < 5:
    iNumero = int(input(txt))
    if (iNumero >= 0 and iCant < 5) or (iNumero < 0 and iCant > 5):
        cargarVector(aNumeros, iNumero)
        if iNumero < 0:
            iSumNegativos+=iNumero
        if esMultiplo(iNumero,4) == 0:
            cargarVector(aMulti4,iNumero)
            iCantMulti4+=1
            if esMultiplo(iNumero,3) == 0:
                iCantMulti3+=1
            if esMultiplo(iNumero,2)==0:
                iCantPar+=1                
        iCant+=1  
        if iCant == 5:
            txt=txtNegativo  
  

def cargarVector(vector, numero):
    vector.append(numero) 
    return

def ordenarVectorCreciente(vector):
    vector.Sort
    return

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

