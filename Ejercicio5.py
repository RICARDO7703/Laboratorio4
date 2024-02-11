from collections import deque

def revertir_mitad_cola(cola):
    # La cola está vacía o tiene un número impar de elementos
    if not cola or len(cola) % 2 != 0:
        print("La cola no es válida para la reversión de la mitad.")
        return

    pila_reemplazo = []
    mitad = len(cola) // 2

    # Poner la primera mitad de la cola en la pila
    for _ in range(mitad):
        pila_reemplazo.append(cola.popleft())

    # Revertir la pila y poner de nuevo en la cola
    while pila_reemplazo:
        cola.append(pila_reemplazo.pop())

    # Devolver los elementos a la cola original
    for _ in range(mitad):
        cola.append(cola.popleft())

#Prueba
mi_cola = deque([1, 2, 3, 4, 5, 6])
print("Cola original:", mi_cola)

revertir_mitad_cola(mi_cola)
print("Cola con mitad revertida:", mi_cola)
