from collections import namedtuple
import statistics
Pico = namedtuple("Pico", "nombre altitud provincia")
picos = [Pico("Mulhacén", 3479, "Granada"), Pico("Torreón", 1648, "Cádiz"),
         Pico("Peña Santa", 2596, "León"), Pico("Naranjo", 2519, "Asturias"),
         Pico("Alcazaba", 3371, "Granada"), Pico("Veleta", 3396, "Granada"),
         Pico("Torrecilla", 1919, "Málaga"), Pico("Llambrión", 2647, "León"),
         Pico("Teide", 3718, "Santa Cruz de Tenerife")]

#EJ 1
nombres_ordenados = sorted([pico.nombre for pico in picos])
print(nombres_ordenados)

#EJ 2
picos_altitud_nombre = [(p.altitud, p.nombre) for p in picos]
print(picos_altitud_nombre)

#EJ 3
nombres_picos_Granada = [pico for pico in picos if pico.provincia == "Granada"]
print(nombres_picos_Granada)

#EJ 4
picos_mas_2000 = sorted([(p.altitud, p.nombre) for p in picos if p.altitud > 2000], reverse=True)
print(picos_mas_2000)

#EJ 5
suma_picos_León = sum(p.altitud for p in picos if p.provincia == 'León')
print(suma_picos_León)

#EJ 6
pico_mas_alto = max(picos, key = lambda p: p.altitud)
print((pico_mas_alto.altitud, pico_mas_alto.nombre))

#EJ 7
altitud_media = sum(p.altitud for p in picos) / len(picos)
print(altitud_media)

#EJ 8
provincias = sorted(set(p.provincia for p in picos))
print(provincias)