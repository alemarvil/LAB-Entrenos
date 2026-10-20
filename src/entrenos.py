from typing import NamedTuple,List
from collections import namedtuple
import csv
from datetime import datetime,date

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos (ruta:str)-> List[Entreno]:
    entrenos = []
    with open (ruta, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias , distancia, frecuencia , compartido in lector:
            entrenos.append (Entreno(
                tipo = str(tipo),
                fechahora = datetime.strptime(fechahora,'%d/%m/%Y %H:%M'),
                ubicacion = str(ubicacion),
                duracion = int(duracion),
                calorias = int(calorias),
                distancia = float(distancia),
                frecuencia = int(frecuencia),
                compartido = True if compartido == "S" else False #Cuidado con esto que se me habia pasado y habia puesto bool(compartido)
            ))
        return entrenos


def tipos_entreno (entrenos:List[Entreno])-> {str}:

    tipos = set()

    for t in entrenos:
        tipos.add(t[0])
    return sorted(tipos)


def entrenos_duracion_superior (entrenos:List[Entreno], d:float)-> List[Entreno]:
    entrenos_condicion = []
    for p in entrenos:
        if p[3] > d:
            entrenos_condicion.append(p)
    print (f"Hay {len(entrenos_condicion)} entrenos que superan los {d} minutos")
    return entrenos_condicion

def suma_calorias (entrenos:List[Entreno],fecha_inicio:datetime,fecha_fin:datetime)-> int:

    sum = 0
    for e in entrenos:
        if fecha_inicio <= e[1] <= fecha_fin:
            sum += e[4]
    print(f"En los entrenos realizados entre {fecha_inicio} y {fecha_fin} se han quemado {sum} calorias.")
    return sum

def entrenamiento_mas_kilometros(entrenos:List[Entreno])-> Entreno:
    d = {}
    for e in entrenos:
        d[e.distancia] = e
    mayor_d = max(d.keys())
    resultado = d[mayor_d]

    print (f"El entreno con mayor distancia recorrida es {resultado} con {mayor_d} kms recorridos.")
    return resultado

def duracion_media_entrenos (entrenos:List[Entreno], año:date, mes:date)-> float|None:
    suma = 0
    l = []
    for e in entrenos:
        if e.fechahora.year == año and e.fechahora.month == mes:
            l.append(e)
            suma += e.duracion

    if len(l) == 0:
        return None
    
    media = suma/len(l)
    print(f"La duración media de los entrenos del año {año} y el mes {mes} es {media}")
    return media
  

        









