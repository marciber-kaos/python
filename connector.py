import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password='1234',
    database="coches"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM coches")
coches = cursor.fetchall()

# Imprimir resultados de forma tabular
print("ID    MARCA          MODELO         COLOR     KM        PRECIO")
print("--------------------------------------------------------------")
for coche in coches:
    print(f"{coche[0]:<5} {coche[1]:<15} {coche[2]:<15} {coche[3]:<10} {coche[4]:<10} {coche[5]:<10}")

conexion.close()
