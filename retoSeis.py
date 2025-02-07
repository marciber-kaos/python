import mysql.connector
import json

# Cargar configuración
with open("configuracion.json") as config_file:
    config = json.load(config_file)

# Conectar a la base de datos
conexion = mysql.connector.connect(**config)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")
coches = cursor.fetchall()

# Imprimir resultados de forma tabular
print("+----+--------+---------+-------+-------------+--------+")
print("| ID | Marca  | Modelo  | Color | Kilometraje | Precio |")
print("+----+--------+---------+-------+-------------+--------+")
for coche in coches:
    print(f"| {coche[0]:<2} | {coche[1]:<6} | {coche[2]:<7} | {coche[3]:<5} | {coche[4]:<11} | {coche[5]:<6} |")
print("+----+--------+---------+-------+-------------+--------+")

conexion.close()

