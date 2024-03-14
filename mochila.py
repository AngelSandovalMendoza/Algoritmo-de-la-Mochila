def mochila(capacidad, objetos):
    n = len(objetos)
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if objetos[i - 1]["peso"] <= w:
                dp[i][w] = max(objetos[i - 1]["peso"] + dp[i - 1][w - objetos[i - 1]["peso"]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    peso_total = capacidad
    objetos_seleccionados = []
    i = n
    while i > 0 and peso_total > 0:
        if dp[i][peso_total] != dp[i - 1][peso_total]:
            objetos_seleccionados.append(objetos[i - 1])
            peso_total -= objetos[i - 1]["peso"]
        i -= 1

    return dp[n][capacidad], objetos_seleccionados

# Definición de los objetos
objetos = [
    {"nombre": "Libro", "peso": 1}, 
    {"nombre": "Botella de agua", "peso": 2},
    {"nombre": "Portátil", "peso": 5}, 
    {"nombre": "Ropa", "peso": 3},
    {"nombre": "Comida", "peso": 4}, 
    {"nombre": "Cámara", "peso": 2},
    {"nombre": "Linterna", "peso": 1}, 
    {"nombre": "Mapa", "peso": 1},
    {"nombre": "Mochila", "peso": 3}, 
    {"nombre": "Tienda de campaña", "peso": 6},
    {"nombre": "Colchoneta", "peso": 4}, 
    {"nombre": "Navaja suiza", "peso": 1},
    {"nombre": "Botiquín", "peso": 3}, 
    {"nombre": "Brújula", "peso": 1},
    {"nombre": "Saco de dormir", "peso": 5}, 
    {"nombre": "Encendedor", "peso": 1},
    {"nombre": "Repelente de insectos", "peso": 2}, 
    {"nombre": "Cuerda", "peso": 3},
    {"nombre": "Gafas de sol", "peso": 1}, 
    {"nombre": "Protector solar", "peso": 2},
    {"nombre": "Sombrero", "peso": 1}, 
    {"nombre": "Guantes", "peso": 1},
    {"nombre": "Saco impermeable", "peso": 2}, 
    {"nombre": "Papel higiénico", "peso": 1},
    {"nombre": "Fósforos", "peso": 1}, 
    {"nombre": "Cubiertos", "peso": 1},
    {"nombre": "Botella de alcohol", "peso": 2}, 
    {"nombre": "Patineta", "peso": 5},
    {"nombre": "Lámpara de gas", "peso": 3}
]

# Capacidad de la mochila
capacidad = 20

# Llamamos a la función mochila
valor_maximo, objetos_seleccionados = mochila(capacidad, objetos)

# Imprimimos los resultados
print("El valor máximo que se puede obtener es:", valor_maximo)
print("Objetos seleccionados:")
for objeto in objetos_seleccionados:
    print(" -", objeto["nombre"], "(Peso:", objeto["peso"], ")")
