import matplotlib as mp
import math

"""
Un modulo que tendra algunas cosas de estadistica que van desde medias, 
hasta graficas
"""
def mediaAritmetica(listaNumeros):
    cantidad=0
    for i in listaNumeros:
        cantidad= cantidad+i
    longitud= len(listaNumeros)
    return cantidad/longitud

def mediaGeometrica(lista_de_numeros):
    """
    Funcion que permite sacar la media geometrica de una lista que
    le pasan. 
    """
    producto=1
    longitund=len(lista_de_numeros)
    for i in lista_de_numeros:
        producto=producto*i
    return producto**(1/longitund)

def mediana(lista_de_numeros):
    """
    Función que permite sacar la mediana de una serie de números 
    recibe una lista.
    """
    longitud=len(lista_de_numeros)
    lista_de_numeros.sort()
    if(longitud%2==0):
        mitad=int(longitud/2)
        valor1=lista_de_numeros[mitad]
        valor2=lista_de_numeros[mitad-1]
        print (valor1)
        print(valor2)
        return int((valor1+valor2)/2)
    mitad=int(longitud/2)
    return lista_de_numeros[mitad]
        
def sumaLista(lista):
    """
    Funcion que me permitira sumar todos los elementos 
    de una lista    
    """
    contador=0
    for i in lista:
        contador+=i
    return contador            

def productoCuadrado(lista):
    """
    Metodo que eleva todos los elemtos de la lista al cuadrado
    """
    vectorFinal=[]
    contador=0
    while contador < len(lista):
        i=lista[contador]*lista[contador]
        vectorFinal.append(i)
        contador+=1
    return vectorFinal     

def productoVector(vector1,vector2):
    """
    Funcion que permite multiplicar entrada a 
    entrada 2 listas de numeros
    """
    contador=0
    vectorFinal=[]
    while contador < len(vector1):
        vectorFinal.append( vector1[contador]*vector2[contador])
        contador+=1 
    return vectorFinal

def pedienteX(x,y):
    """
    Metodo auxiliar que nos permite tener la "a" de la ecuacion de la recta
    en la cual pedimos x & y donde x & y son lista de puntos.  
    """
    n=len(x)
    productoxy=productoVector(x,y)
    sumaProdxy=sumaLista(productoxy)
    sumax=sumaLista(x)
    sumay=sumaLista(y)
    productoSxSy=sumax*sumay
    xCuadrado=productoCuadrado(x)
    sumaXCuadrado=sumaLista(xCuadrado)
    numeradorA=(n*sumaProdxy)-(sumax * sumay)
    denominadorA=(n*sumaXCuadrado)-sumax**2
    return numeradorA/denominadorA

def intercepcion(x,y):
    sumay=sumaLista(y)
    a=pedienteX(x,y)
    sumax=sumaLista(x)
    n=len(x)
    b=sumay-(a*sumax)
    return b/len(x)       
        
def creadorGraficaBarras(nombresX, valores,titulo ):
    fig=mp.figure(u'Grafica de Barras')
    ax=fig.add_subplot(111)
    xx=valores
    ax.bar(nombresX,xx,width=1,align='center')
    ax.set_xticks(xx)
    #ax.set_xticklabels(nombresX)
    mp.show()

def regrecionLineal(x,y):
    lf=[]
    a=pedienteX(x,y)
    b=intercepcion(x,y)
    lf.append(a)
    lf.append(b)
    print("La mejor aproximacion es a los valores dados son")
    print("y = " + str(a) + "x + " + str(b))
    return lf

def valoresPrimos(valoresX):
    """
    Funcion auxiliar que nos permitira tener los valores de una tabla
    extra para poder sacar Coeficiente de corelacion lineal
    """
    media=mediaAritmetica(valoresX)
    lr=[]
    contador=0
    i=0
    while contador < len(valoresX):
       i=valoresX[contador]
       lr.append(i-media)
       contador+=1 
    return lr

def productoCXYPRimos(listaPuntos):
    """"
    Producto cuadrado de x con la x prima recibe los valores de x y 
    tambien funciona con las y
    """
    xPrima=valoresPrimos(listaPuntos)
    lf=productoCuadrado(xPrima)
    return lf

def productoXY(valoreDeX, valoresDeY):
    xPrimo=valoresPrimos(valoreDeX)
    yPrima=valoresPrimos(valoresDeY)
    lf=[]
    contador=0
    valorActual=0
    
    for i in xPrimo:
        valorActual=i*yPrima[contador]
        lf.append(valorActual)
        contador+=1
    return lf    

            
def correlacionLineal(valoreDeX,valoresDeY):
    xPrima=productoCXYPRimos(valoreDeX)
    yprima=productoCXYPRimos(valoresDeY)
    sumaXPrima=sumaLista(xPrima)
    sumaYprima=sumaLista(yprima)
    producto=productoXY(valoreDeX,valoresDeY)
    rNumerado=sumaLista(producto)
    rDenomidaor=math.sqrt(sumaXPrima) * math.sqrt(sumaYprima)
    return rNumerado/rDenomidaor
    

"""
Funcion del main 
"""
if __name__ == "__main__":
   y=[3,5,9,10,20,21,24,24,27,35]
   x=[100,90,80,45,50,50,60,40,25,20]
   
   correlacionLineal(x,y)
   #print(productoXY(x,y))
   #print(valoresPrimos(x))
   #print(valoresPrimos(y))
