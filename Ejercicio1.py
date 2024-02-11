pila = [1,2,3,4,5,6,7,8]

#Agregamos un elemento al final de la lista
pila.append(9)
print(pila)

print("------------------------------------")

#Sacamos el ultimo elemento de la lista
n = pila.pop()
print(pila)
print(f'Elemento sacado: {n}')

print("------------------------------------")

#Mostramos el elemento superior de la pila
print("El elemento superior de la pila es: ",pila[-1])

print("------------------------------------")

#Invertimos el orden de la pila

print(f'Orden de la pila {pila}')

pila_invertida = pila[::-1]
print(f'pila invertida {pila_invertida}')