from pymongo import MongoClient
from tabulate import tabulate

client = MongoClient("mongodb://localhost:27017/")
db = client["cochesDB"]
coches = db["coches"].find()

print(tabulate(coches, headers="keys", tablefmt="grid"))
