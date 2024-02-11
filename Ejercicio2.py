cola = ["Maria", "Alejandra,", "Jose", "Mario"]

#Agregamos elementos al final de la cola
cola.append("Karla")
cola.append("Flor")
print(cola)

print("------------------------------------")

#Sacando elementos por el principio de la cola
n = cola.pop(0)
print(cola)
print(f'Estan atendiendo a {n}')