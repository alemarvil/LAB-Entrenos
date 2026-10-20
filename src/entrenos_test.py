from entrenos import * 


ruta = 'data\entrenos.csv'

if __name__ == "__main__":
    a = lee_entrenos(ruta)
    b = tipos_entreno(a)
    c = entrenos_duracion_superior(a,120)
    d = suma_calorias(a,datetime(2020,3,15,0,0),datetime(2020,6,30,23,59))
    e = entrenamiento_mas_kilometros(a)
    d = duracion_media_entrenos(a,2020,3)

