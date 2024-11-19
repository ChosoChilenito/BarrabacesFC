import json

JSON = "data.json"

def cargar():
    try:
        with open(JSON, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"profesores": [], "alumnos": [], "apoderados": [], "goles": []}

def guardar(datos):
    with open(JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Profesores
def agregar_profesor(rut, nombre, año_nacimiento, especialidad):
    datos = cargar()
    nuevo_profesor = {"rut": rut, "nombre": nombre, "año_nacimiento": año_nacimiento, "especialidad": especialidad}
    datos["profesores"].append(nuevo_profesor)
    guardar(datos)

def modificar_profesor(rut, nuevos_datos):
    datos = cargar()
    for profesor in datos["profesores"]:
        if profesor["rut"] == rut:
            profesor.update(nuevos_datos)
    guardar(datos)

def eliminar_profesor(rut):
    datos = cargar()
    datos["profesores"] = [prof for prof in datos["profesores"] if prof["rut"] != rut]
    guardar(datos)

# Apoderados
def agregar_apoderado(rut, nombre, num_telefono):
    datos = cargar()
    nuevo_apoderado = {"rut": rut, "nombre": nombre, "num_telefono": num_telefono}
    datos["apoderados"].append(nuevo_apoderado)
    guardar(datos)

def modificar_apoderado(rut, nuevos_datos):
    datos = cargar()
    for apoderado in datos["apoderados"]:
        if apoderado["rut"] == rut:
            apoderado.update(nuevos_datos)
    guardar(datos)

def eliminar_apoderado(rut):
    datos = cargar()
    datos["apoderados"] = [apod for apod in datos["apoderados"] if apod["rut"] != rut]
    guardar(datos)

# Alumnos
def agregar_alumno(rut, nombre, direccion, año_nacimiento, posicion, año_incorporacion, profesor, apoderado):
    datos = cargar()
    nuevo_alumno = {"rut": rut, "nombre": nombre, "direccion": direccion, "año_nacimiento": año_nacimiento, "posicion": posicion, 
    "año_incorporacion": año_incorporacion, "profesor": profesor ,"apoderado": apoderado}
    datos["alumnos"].append(nuevo_alumno)
    guardar(datos)

def modificar_alumno(rut, nuevos_datos):
    datos = cargar()
    for alumno in datos["alumnos"]:
        if alumno["rut"] == rut:
            alumno.update(nuevos_datos)
    guardar(datos)

def eliminar_alumno(rut):
    datos = cargar()
    datos["alumno"] = [alum for alum in datos["alumnos"] if alum["rut"] != rut]
    guardar(datos)

def listado_alum(rut_profesor):
    datos = cargar()
    alumnos = [alumno for alumno in datos["alumnos"] if alumno["profesor"] == rut_profesor]
    return alumnos

def contacto_apoderado(rut_alumno):
    datos = cargar()
    alumno_encontrado = None
    for alumno in datos["alumnos"]:
        if alumno["rut"] == rut_alumno:
            alumno_encontrado = alumno
            break
    
    if alumno_encontrado is not None:
        apoderado_encontrado = None
        for apoderado in datos["apoderados"]:
            if apoderado["rut"] == alumno_encontrado["apoderado"]:
                apoderado_encontrado = apoderado
                break
        
        if apoderado_encontrado is not None:
            return {"nombre": apoderado_encontrado["nombre"], "telefono": apoderado_encontrado["telefono"]}
    
    return None

def ranking_goleadores(mes, año, n):
    datos = cargar()
    
    goles_mes = []
    for gol in datos["goles"]:
        fecha = gol["fecha"]
        if fecha.startswith(f"{año}-{mes:02d}"):
            goles_mes.append(gol)
    
    ranking = {}
    for gol in goles_mes:
        rut_alumno = gol["rut_alumno"]
        if rut_alumno in ranking:
            ranking[rut_alumno] += gol["cantidad_goles"]
        else:
            ranking[rut_alumno] = gol["cantidad_goles"]
    
    def obtener_goles(item):
        return item[1]
    
    ranking_ordenado = sorted(ranking.items(), key=obtener_goles, reverse=True)
    top_n = ranking_ordenado[:n]
    
    resultado = []
    for rut, goles in top_n:
        nombre_alumno = None
        for alumno in datos["alumnos"]:
            if alumno["rut"] == rut:
                nombre_alumno = alumno["nombre"]
                break
        
        if nombre_alumno is None:
            nombre_alumno = rut 

        resultado.append((nombre_alumno, goles))
    
    return resultado