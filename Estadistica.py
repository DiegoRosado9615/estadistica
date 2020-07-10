import matplotlib as mp
import math

"""
Un modulo que tendra algunas cosas de estadistica que van desde medias, 
hasta graficas
"""
def mediaAritmetica(listaNumeros):
    """Funcion que saca la medianAritmetica, 
        recibe una lista de número
        devuelve un entero  
    """
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
       
        
def creadorGraficaBarras(nombresX, valores,titulo ):
    fig=mp.figure(u'Grafica de Barras')
    ax=fig.add_subplot(111)
    xx=valores
    ax.bar(nombresX,xx,width=1,align='center')
    ax.set_xticks(xx)
    #ax.set_xticklabels(nombresX)
    mp.show()

"""
Funcion del main 
"""
if __name__ == "__main__":
   y=[3,5,9,10,20,21,24,24,27,35]
   x=[100,90,80,45,50,50,60,40,25,20]
   print(pedienteX(x,y))
   