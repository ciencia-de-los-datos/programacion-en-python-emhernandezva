"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""




from operator import itemgetter
from functools import reduce

def datos():
    with open ("data.csv",mode='r') as file:
        listFilas=file.readlines()
        listFilas=[i.replace('\n','') for i in listFilas]
        listFilas=[i.split('\t') for i in listFilas]
    return listFilas

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    listFilas=datos()
    Rta/
    214
    """
    Rta=sum([int(i[1]) for i in datos()])

    return Rta

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    dictPalabras={}
    listFilas=datos()
    listTuplasPalabras=[(i[0],1) for i in listFilas]
    for k, v in listTuplasPalabras:
        if k in dictPalabras:dictPalabras[k]=dictPalabras[k]+v
        else: dictPalabras[k]=v
    listConteoPalabras=[(k,v) for k,v in dictPalabras.items()]
    listConteoPalabras=list(sorted(listConteoPalabras,key=itemgetter(0)))
    return listConteoPalabras


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dictSumaPalabras={}
    listFilas=datos()
    listTuplasSuma=[(i[0],int(i[1])) for i in listFilas]
    for k, v in listTuplasSuma:
        if k in dictSumaPalabras:dictSumaPalabras[k]=dictSumaPalabras[k]+v
        else: dictSumaPalabras[k]=v
    listSumaValores=[(k,v) for k,v in dictSumaPalabras.items()]
    listSumaValores=list(sorted(listSumaValores,key=itemgetter(0)))
    return listSumaValores
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dictRegistroMes={}
    listFilas=datos()
    listTuplasMeses=[(i[2].split('-')[1],1) for i in listFilas]
    for k, v in listTuplasMeses:
        if k in dictRegistroMes:dictRegistroMes[k]=dictRegistroMes[k]+v
        else: dictRegistroMes[k]=v
    listRegistroMes=[(k,v) for k,v in dictRegistroMes.items()]
    listRegistroMes=list(sorted(listRegistroMes,key=itemgetter(0)))
    return listRegistroMes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dictLetras={}
    listFilas=datos()
    listTuplasMaxMin=[(i[0],[int(i[1]),int(i[1])]) for i in listFilas]
    Maximo=lambda valor, ValorAnterior: valor if valor>=ValorAnterior else ValorAnterior
    Minimo=lambda valor, ValorAnterior: valor if valor<=ValorAnterior else ValorAnterior
    for k, v in listTuplasMaxMin:
        if k in dictLetras:dictLetras[k]=[Maximo(dictLetras[k][0],v[0]),Minimo(dictLetras[k][1],v[1])]
        else: dictLetras[k]=[Maximo(v[0],v[0]),Minimo(v[1],v[1])]
    listMaxMin=[(k,v) for k,v in dictLetras.items()]
    listMaxMin=list(sorted(listMaxMin,key=itemgetter(0)))
    listMaxMin=[(k,v[0],v[1]) for k,v in listMaxMin]
    return listMaxMin


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dictCadenas={}
    listCadenas=[i[4].split(',') for i in datos()]
    listCadenas=reduce(lambda x,y:x+y,listCadenas)
    listTuplasMaxMin=[(i.split(':')[0],[int(i.split(':')[1]),int(i.split(':')[1])]) for i in listCadenas]
    Maximo=lambda valor, ValorAnterior: valor if valor>=ValorAnterior else ValorAnterior
    Minimo=lambda valor, ValorAnterior: valor if valor<=ValorAnterior else ValorAnterior
    for k, v in listTuplasMaxMin:
        if k in dictCadenas:dictCadenas[k]=[Minimo(dictCadenas[k][0],v[0]),Maximo(dictCadenas[k][1],v[1])]
        else: dictCadenas[k]=[Minimo(v[0],v[0]),Maximo(v[1],v[1])]
    listMaxMin=[(k,v) for k,v in dictCadenas.items()]
    listMaxMin=list(sorted(listMaxMin,key=itemgetter(0)))
    listMaxMin=[(k,v[0],v[1]) for k,v in listMaxMin]
    return listMaxMin


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dictValores={}
    listFilas=datos()
    listTuplaC01=[(int(i[1]),[i[0]]) for i in listFilas]
    for k, v in listTuplaC01:
        if k in dictValores:dictValores[k]=dictValores[k]+v
        else: dictValores[k]=v
    listTuplaC01=[(k,v) for k, v in dictValores.items()]
    listTuplaC01=list(sorted(listTuplaC01,key=itemgetter(0)))
    return listTuplaC01



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dictValores={}
    listFilas=datos()
    listTuplaC01=[(int(i[1]),[i[0]]) for i in listFilas]
    for k, v in listTuplaC01:
        if k in dictValores:dictValores[k]=dictValores[k]+v
        else: dictValores[k]=v
    listTuplaC01=[(k,v) for k, v in dictValores.items()]
    listTuplaC01=[(k,list(sorted(set(v)))) for k, v in dictValores.items()]
    listTuplaC01=list(sorted(listTuplaC01,key=itemgetter(0)))
    return listTuplaC01


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dictCadenas={}
    listCadenas=[i[4].split(',') for i in datos()]
    listCadenas=reduce(lambda x,y:x+y,listCadenas)
    listTuplasCadenas=[(i.split(':')[0],1) for i in listCadenas]
    for k, v in listTuplasCadenas:
        if k in dictCadenas:dictCadenas[k]=dictCadenas[k]+v
        else: dictCadenas[k]=v
    listTuplasCadenas=[(k,v) for k,v in dictCadenas.items()]
    dictTuplasCadenas=dict(sorted(listTuplasCadenas,key=itemgetter(0)))
    return dictTuplasCadenas



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    listFilas=datos()
    conteo=lambda x: len(x.split(','))
    listTuplasLetraC45=[(i[0],conteo(i[3]),conteo(i[4])) for i in listFilas]
    return listTuplasLetraC45



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dictletrasC4={}
    listTuplasC4=[(i[3].split(','),i[1]) for i in datos()]
    listTuplasC4=[(n,int(i[1]))  for i in listTuplasC4 for n in i[0]]
    for k, v in listTuplasC4:
        if k in dictletrasC4:dictletrasC4[k]=dictletrasC4[k]+v
        else: dictletrasC4[k]=v
    listTuplasC4=[(k,v) for k,v in dictletrasC4.items()]
    dictTuplasC4=dict(sorted(listTuplasC4,key=itemgetter(0)))
    return dictTuplasC4
 


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dictletrasC5={}
    listletrasC5=[(i[0],sum([int(n.split(':')[-1]) for n in i[4].split(',')])) for i in datos()]
    for k, v in listletrasC5:
        if k in dictletrasC5:dictletrasC5[k]=dictletrasC5[k]+v
        else: dictletrasC5[k]=v
    dictletrasC5=dict(sorted(dictletrasC5.items()))
    return dictletrasC5


if __name__=='__main__':
    """print(pregunta_01())
    print(pregunta_02())
    print(pregunta_03())
    print(pregunta_04())
    print(pregunta_05())
    print(pregunta_06())
    print(pregunta_07())
    print(pregunta_08())
    print(pregunta_09())
    print(pregunta_10())
    print(pregunta_11())
    print(pregunta_12())"""