import csv

def cargar_datos():
    datos = []
    with open('data.csv', 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def obtener_estudiantes_por_ciudad(ciudad, datos):
    estudiantes = []
    for estudiante in datos:
        if estudiante['ciudad'] == ciudad:
            estudiantes.append(estudiante)
    return estudiantes


def obtener_estudiantes_por_pais(pais, datos):
    estudiantes = []
    for estudiante in datos:
        if estudiante['País'] == pais:
            estudiantes.append(estudiante)
    return estudiantes

def obtener_estudiantes_por_rango_edades(edad_min, edad_max, datos):
    estudiantes = []
    for estudiante in datos:
        edad = int(estudiante['Edad'])
        if edad >= edad_min and edad <= edad_max:
            estudiantes.append(estudiante)
    return estudiantes

def obtener_ciudades_residencia(datos):
    ciudades = set()
    for estudiante in datos:
        ciudades.add(estudiante['Ciudad'])
    return ciudades

def calcular_edad_promedio_por_carrera(datos):
    edades_por_carrera = {}
    contador_por_carrera = {}
    for estudiante in datos:
        carrera = estudiante['Carrera']
        edad = int(estudiante['Edad'])
        if carrera in edades_por_carrera:
            edades_por_carrera[carrera] += edad
            contador_por_carrera[carrera] += 1
        else:
            edades_por_carrera[carrera] = edad
            contador_por_carrera[carrera] = 1
    edad_promedio_por_carrera = {}
    for carrera in edades_por_carrera:
        edad_promedio = edades_por_carrera[carrera] / contador_por_carrera[carrera]
        edad_promedio_por_carrera[carrera] = edad_promedio
    return edad_promedio_por_carrera

def comparar_edad_estudiantes_por_carrera(datos, edad_promedio_por_carrera):
    comparacion_por_carrera = {}
    for estudiante in datos:
        carrera = estudiante['Carrera']
        edad = int(estudiante['Edad'])
        edad_promedio = edad_promedio_por_carrera[carrera]
        if edad > edad_promedio:
            comparacion_por_carrera[estudiante['Nombre']] = 'por encima'
        else:
            comparacion_por_carrera[estudiante['Nombre']] = 'por debajo'
    return comparacion_por_carrera

def agrupar_estudiantes_por_rango_edades(datos):
    rangos_edades = {
        '18-25': [],
        '26-35': [],
        'mayores de 35': []
    }
    for estudiante in datos:
        edad = int(estudiante['Edad'])
        if edad >= 18 and edad <= 25:
            rangos_edades['18-25'].append(estudiante)
        elif edad >= 26 and edad <= 35:
            rangos_edades['26-35'].append(estudiante)
        else:
            rangos_edades['mayores de 35'].append(estudiante)
    return rangos_edades

def obtener_ciudad_mayor_variedad_carreras(datos):
    ciudades_carreras = {}
    for estudiante in datos:
        ciudad = estudiante['Ciudad']
        carrera = estudiante['Carrera']
        if ciudad in ciudades_carreras:
            ciudades_carreras[ciudad].add(carrera)
        else:
            ciudades_carreras[ciudad] = {carrera}
    ciudad_variedad_carreras = max(ciudades_carreras, key=lambda x: len(ciudades_carreras[x]))
    return ciudad_variedad_carreras

def generar_reporte(opcion, datos):
    if opcion == 1:
        ciudad = input('Ingrese la ciudad: ')
        estudiantes = obtener_estudiantes_por_ciudad(ciudad, datos)
        generar_reporte_estudiantes(estudiantes)
    elif opcion == 2:
        pais = input('Ingrese el país: ')
        estudiantes = obtener_estudiantes_por_pais(pais, datos)
        generar_reporte_estudiantes(estudiantes)
    elif opcion == 3:
        edad_min = int(input('Ingrese la edad mínima: '))
        edad_max = int(input('Ingrese la edad máxima: '))
        estudiantes = obtener_estudiantes_por_rango_edades(edad_min, edad_max, datos)
        generar_reporte_estudiantes(estudiantes)
    elif opcion == 4:
        ciudades = obtener_ciudades_residencia(datos)
        generar_reporte_ciudades(ciudades)
    elif opcion == 5:
        edad_promedio_por_carrera = calcular_edad_promedio_por_carrera(datos)
        generar_reporte_edad_promedio_carrera(edad_promedio_por_carrera)
    elif opcion == 6:
        edad_promedio_por_carrera = calcular_edad_promedio_por_carrera(datos)
        comparacion_por_carrera = comparar_edad_estudiantes_por_carrera(datos, edad_promedio_por_carrera)
        generar_reporte_comparacion_edad_estudiantes(comparacion_por_carrera)
    elif opcion == 7:
        rangos_edades = agrupar_estudiantes_por_rango_edades(datos)
        generar_reporte_rangos_edades(rangos_edades)
    elif opcion == 8:
        ciudad_variedad_carreras = obtener_ciudad_mayor_variedad_carreras(datos)
        generar_reporte_ciudad_variedad_carreras(ciudad_variedad_carreras)
    else:
        print('Opción inválida')

def generar_reporte_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print('No se encontraron estudiantes que cumplan los criterios.')
        return
    
    nombre_archivo = 'reporte_estudiantes.csv'
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=estudiantes[0].keys())
        escritor_csv.writeheader()
        escritor_csv.writerows(estudiantes)
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

def generar_reporte_ciudades(ciudades):
    if len(ciudades) == 0:
        print('No se encontraron ciudades de residencia.')
        return
    
    nombre_archivo = 'reporte_ciudades.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Ciudades de residencia de los estudiantes:\n')
        for ciudad in ciudades:
            archivo.write(ciudad + '\n')
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

def generar_reporte_edad_promedio_carrera(edad_promedio_por_carrera):
    if len(edad_promedio_por_carrera) == 0:
        print('No se encontraron carreras.')
        return
    
    nombre_archivo = 'reporte_edad_promedio_carrera.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Edad promedio por carrera:\n')
        for carrera, edad_promedio in edad_promedio_por_carrera.items():
            archivo.write(f'{carrera}: {edad_promedio} años\n')
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

def generar_reporte_comparacion_edad_estudiantes(comparacion_por_carrera):
    if len(comparacion_por_carrera) == 0:
        print('No se encontraron estudiantes.')
        return
    
    nombre_archivo = 'reporte_comparacion_edad_estudiantes.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Comparación de edad de estudiantes por carrera:\n')
        for estudiante, comparacion in comparacion_por_carrera.items():
            archivo.write(f'{estudiante}: {comparacion} del promedio\n')
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

def generar_reporte_rangos_edades(rangos_edades):
    if len(rangos_edades) == 0:
        print('No se encontraron estudiantes.')
        return
    
    nombre_archivo = 'reporte_rangos_edades.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Estudiantes agrupados por rango de edades:\n')
        for rango, estudiantes in rangos_edades.items():
            archivo.write(f'{rango}:\n')
            for estudiante in estudiantes:
                archivo.write(f'Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}\n')
            archivo.write('\n')
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

def generar_reporte_ciudad_variedad_carreras(ciudad):
    if len(ciudad) == 0:
        print('No se encontraron estudiantes.')
        return
    
    nombre_archivo = 'reporte_ciudad_variedad_carreras.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f'Ciudad con mayor variedad de carreras universitarias:\n{ciudad}\n')
    print(f'Se ha generado el reporte en el archivo {nombre_archivo}.')

# Carga los datos del archivo CSV
datos = cargar_datos()

# Menú de opciones
while True:
    print('---- MENÚ ----')
    print('1. Obtener estudiantes por ciudad')
    print('2. Obtener estudiantes por país')
    print('3. Obtener estudiantes por rango de edades')
    print('4. Obtener todas las ciudades de residencia de los estudiantes')
    print('5. Identificar edad promedio por carrera')
    print('6. Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad')
    print('7. Agrupar estudiantes en diferentes rangos de edad')
    print('8. Identificar ciudad con mayor variedad de carreras universitarias entre los estudiantes')
    print('0. Salir')

    opcion = int(input('Ingrese una opción: '))
    if opcion == 0:
        break

    generar_reporte(opcion, datos)
