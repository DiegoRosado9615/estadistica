import matplotlib.pyplot as mp
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
    pass
    
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
 x=[32.6,53.5,28.9,48.2,67.4]
 print(mediaGeometrica(x))