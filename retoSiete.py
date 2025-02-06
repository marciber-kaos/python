import mysql.connector
import json
from tabulate import tabulate

# Cargar configuración
with open("configuracion.json") as config_file:
    config = json.load(config_file)

# Conectar a la base de datos
conexion = mysql.connector.connect(**config)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")
coches = cursor.fetchall()

# Imprimir resultados con `tabulate`
print(tabulate(coches, headers=["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"], tablefmt="grid"))

conexion.close()
