estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 3.2, 4.8]},
    {"nombre": "Luis", "notas": [2.9, 3.1, 2.8]},
    {"nombre": "Camila", "notas": [5.5, 6.7, 2.9]},
    {"nombre": "Pedro", "notas": [3.0, 2.5, 4.0]},
    {"nombre": "Valentina", "notas": [6.9, 5.2, 3.3]},
    {"nombre": "Andrés", "notas": [2.0, 2.8, 3.1]},
    {"nombre": "Javiera", "notas": [6.3, 4.1, 2.9]},
    {"nombre": "Matías", "notas": [3.7, 2.0, 3.4]},
    {"nombre": "Francisca", "notas": [6.5, 5.8, 6.0]},
    {"nombre": "Diego", "notas": [2.5, 2.2, 3.9]},
    {"nombre": "Catalina", "notas": [4.2, 3.5, 5.8]},
    {"nombre": "Ignacio", "notas": [2.8, 4.0, 3.1]},
    {"nombre": "Fernanda", "notas": [5.9, 6.7, 2.5]},
    {"nombre": "Sebastián", "notas": [3.5, 3.9, 2.3]},
    {"nombre": "Constanza", "notas": [6.0, 2.9, 3.8]},
    {"nombre": "Felipe", "notas": [2.9, 3.6, 2.1]},
    {"nombre": "Rocío", "notas": [4.4, 2.6, 3.9]},
    {"nombre": "Tomás", "notas": [2.7, 2.9, 3.2]},
    {"nombre": "Paula", "notas": [6.8, 4.0, 2.6]},
    {"nombre": "Cristóbal", "notas": [3.1, 2.8, 2.3]},
    {"nombre": "Daniela", "notas": [5.7, 6.9, 5.0]},
    {"nombre": "Rodrigo", "notas": [2.7, 3.4, 2.9]},
    {"nombre": "María", "notas": [4.3, 3.8, 2.9]},
    {"nombre": "Nicolás", "notas": [3.9, 2.1, 3.4]},
    {"nombre": "Sofía", "notas": [6.0, 2.9, 2.0]},
    {"nombre": "Claudia", "notas": [3.0, 2.2, 4.5]},
    {"nombre": "Gabriel", "notas": [2.4, 2.8, 3.2]},
    {"nombre": "Josefa", "notas": [5.8, 3.0, 2.7]},
    {"nombre": "Mauricio", "notas": [2.6, 1.9, 2.8]},
    {"nombre": "Carolina", "notas": [4.4, 3.7, 2.9]}
]

lis_prom = []
aprobados = 0
todas_notas = []
nota_bajo_4 = 0
ordenados = sorted(
    estudiantes,
    key=lambda est: sum(est["notas"]) / len(est["notas"]),
    reverse = True
)

for est in estudiantes:
    prom = sum(est["notas"]) / len(est["notas"])
    lis_prom.append(prom)
    if prom >= 4.0:
        aprobados = aprobados + 1
    todas_notas.extend(est["notas"])
    if any(n < 4.0 for n in est["notas"]):
        nota_bajo_4 = nota_bajo_4 + 1

conteo = {}
for n in todas_notas:
    if n in conteo:
        conteo[n] = conteo[n] + 1
    else:
        conteo[n] = 1    

nota_bajo_4 = (nota_bajo_4 / len(estudiantes)) * 100 

max_prom = max(lis_prom)
min_prom = min(lis_prom)
max_frec = max(conteo.values())
moda = [nota for nota, frec in conteo.items() if frec == max_frec]

print("El mejor promedio es: ", round(max_prom, 2))
print("El peor promedio es: ", round(min_prom, 2))
print("El número de estudiantes aprobados es de: ", aprobados)
print("La nota más frecuente es: ", moda)
print("El porcentaje de estudiantes que tiene al menos una nota bajo 4.0 es: ", round(nota_bajo_4, 2), "%")

for est in ordenados:
    prom = sum(est["notas"]) / len(est["notas"])
    print(f"{est['nombre']}: {round(prom, 2)}")
