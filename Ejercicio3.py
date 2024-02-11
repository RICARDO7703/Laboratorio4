def parentesis_balanceados(cadena):
    #se crea una lista vacia para que simule una pila
    pila = []
    
    #Se evalua para saber si es  un parenteris de apertura o cierre
    for caracter in cadena:
        if caracter == '(' or caracter == '{' or caracter == '[':
            pila.append(caracter)
        elif caracter == ')' and pila and pila[-1] == '(':
            pila.pop()
        elif caracter == '}' and pila and pila[-1] == '{':
            pila.pop()
        elif caracter == ']' and pila and pila[-1] == '[':
            pila.pop()
        else:
            return False
    
    #Se guarda el valor de la pila
    return not pila

# Cadenas de prueba
cadena1 = "({[()]})"
cadena2 = "({[{()]})"

print("¿Los paréntesis en '{}' están balanceados?: {}".format(cadena1, parentesis_balanceados(cadena1)))
print("¿Los paréntesis en '{}' están balanceados?: {}".format(cadena2, parentesis_balanceados(cadena2)))
