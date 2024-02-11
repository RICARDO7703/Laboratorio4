#Se crea la clase 
class ColaConPilas:
    def __init__(self):
        #Se inicializa las dos colas
        self.pila_entrada = []
        self.pila_salida = []
    
    #Devuelve True si amabas pilas estans vacias. Si ambas pilas estan vacias esntonces la cola esta vacia
    def esta_vacia(self):
        return not self.pila_entrada and not self.pila_salida
     
    #Añade elementos a la lsita
    def enqueue(self, elemento):
        self.pila_entrada.append(elemento)
    
    #Devuelve el elemento al al inicio
    def dequeue(self):
        if not self.pila_salida:
            if not self.pila_entrada:
                # La cola está vacía
                return None 
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        return self.pila_salida.pop()

# Pruebas
cola = ColaConPilas()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print("Elemento retirado:", cola.dequeue())
print("Elemento retirado:", cola.dequeue())

cola.enqueue(4)
cola.enqueue(5)

print("Elemento retirado:", cola.dequeue())
print("¿La cola está vacía?:", cola.esta_vacia())
