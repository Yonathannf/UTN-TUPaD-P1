#1_ 

#precios_frutas = {
#    'Banana': 1200,
#    'Ananá': 2500,
#    'Melón': 3000,
#    'Uva': 1450
#}

#precios_frutas['Naranja'] = 1200
#precios_frutas['Manzana'] = 1500
#precios_frutas['Pera'] = 2300

#print(precios_frutas)

#2_ 

#precios_frutas = {
#    'Banana': 1200,
#    'Ananá': 2500,
#    'Melón': 3000,
#    'Uva': 1450,
#    'Naranja': 1200,
#    'Manzana': 1500,
#    'Pera': 2300
#}

#precios_frutas['Banana'] = 1330
#precios_frutas['Manzana'] = 1700
#precios_frutas['Melón'] = 2800

#print(precios_frutas)

#3_ 

#precios_frutas = {
#    'Banana': 1330,
#    'Ananá': 2500,
#    'Melón': 2800,
#    'Uva': 1450,
#    'Naranja': 1200,
#    'Manzana': 1700,
#    'Pera': 2300
#}

#lista_frutas = list(precios_frutas.keys())

#print(lista_frutas)

#4_ 

#contactos = {}

#for i in range(5):
#    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
#    telefono = input(f"Ingresá el número de {nombre}: ")
#    contactos[nombre] = telefono

#print("\nAgenda cargada:", contactos)

#nombre_consulta = input("\n¿A quién querés consultar?: ")

#if nombre_consulta in contactos:
#    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
#else:
#    print(f"{nombre_consulta} no está en la agenda.")

#5_ 

#frase = input("Ingresá una frase: ")

#palabras = frase.split()

#palabras_unicas = set(palabras)
#print("\nPalabras únicas:")
#print(palabras_unicas)

#contador_palabras = {}
#for palabra in palabras:
#    if palabra in contador_palabras:
#        contador_palabras[palabra] += 1
#    else:
#        contador_palabras[palabra] = 1

#print("\nCantidad de apariciones de cada palabra:")
#print(contador_palabras)

#6_ 

#alumnos = {}

#for i in range(3):
#    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
#    print(f"Ingresá 3 notas para {nombre}:")
#    nota1 = float(input("Nota 1: "))
#    nota2 = float(input("Nota 2: "))
#    nota3 = float(input("Nota 3: "))
#    
#    alumnos[nombre] = (nota1, nota2, nota3)

#print("\nPromedios de los alumnos:")
#for nombre, notas in alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"{nombre}: {promedio:.2f}")

#7_ 

#parcial_1 = {"Ana", "Juan", "Luis", "Sofía", "Marcos"}
#parcial_2 = {"Luis", "Sofía", "Valentina", "Pedro", "Ana"}

#ambos = parcial_1 & parcial_2
#print("Aprobaron ambos parciales:", ambos)

#solo_uno = parcial_1 ^ parcial_2
#print("Aprobaron solo uno de los dos:", solo_uno)

#al_menos_uno = parcial_1 | parcial_2
#print("Aprobaron al menos un parcial:", al_menos_uno)

#8_ 

#stock_productos = {
#    "Arroz": 20,
#    "Fideos": 35,
#    "Aceite": 15
#}

#producto = input("Ingresá el nombre del producto a consultar: ")

#if producto in stock_productos:
#    print(f"Stock actual de {producto}: {stock_productos[producto]}")
#    

#    agregar = input(f"¿Querés agregar unidades a {producto}? (sí/no): ").lower()
#    if agregar == "sí":
#        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
#        stock_productos[producto] += cantidad
#        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
#else:
#    print(f"{producto} no está en el sistema.")
#    agregar_nuevo = input("¿Querés agregarlo como nuevo producto? (sí/no): ").lower()
#    if agregar_nuevo == "sí":
#        cantidad = int(input(f"Ingresá la cantidad inicial para {producto}: "))
#        stock_productos[producto] = cantidad
#        print(f"{producto} agregado con un stock de {cantidad} unidades.")

#print("\nStock actualizado:")
#for prod, cant in stock_productos.items():
#    print(f"{prod}: {cant}")

#9_ 

#dia = input("Ingresá el día: ").lower()
#hora = input("Ingresá la hora (HH:MM): ")

#evento = agenda.get((dia, hora))

#if evento:
#    print(f"Evento encontrado: {evento}")
#else:
#    print("No hay evento registrado en ese horario.")

#10_

#paises = {
#    "Argentina": "Buenos Aires",
#    "Brasil": "Brasilia",
#    "Francia": "París",
#    "Japón": "Tokio"
#}

#capitales = {capital: pais for pais, capital in paises.items()}

#print("Diccionario invertido:")
#print(capitales)
