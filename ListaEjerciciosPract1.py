
"""
1. en python Diseña un programa que use una pila para comprobar si una expresión matemática 
tiene los paréntesis correctamente balanceados. 
"""

"""
Recorremos la expresión carácter por carácter.
Cada vez que encontremos un paréntesis de apertura ( lo apilamos.
Cada vez que encontremos un paréntesis de cierre ) verificamos si la pila no está vacía.
Si la pila está vacía → está mal balanceada.
Si no está vacía → desapilamos un (.
Al final, si la pila queda vacía → los paréntesis están balanceados.
Si aún hay elementos en la pila → no están balanceados.
"""

"""
def parentesis_balanceados(expresion):
    pila = []
    for caracter in expresion:
        if caracter == '(':
            pila.append(caracter)  # apilar, append meter un elemento 
        elif caracter == ')':
            if not pila:  # pila vacía y encontramos ')'
                return False
            pila.pop()  # desapilar, quitar el ultimo elemento agregado
    return len(pila) == 0
expresiones = [
    "((a+b)*c)",   # válido
    "(a+b))(",     # no válido
    "(a+b)*(c+d)", # válido
    "((a+b)",      # no válido
]
for exp in expresiones:
    if parentesis_balanceados(exp):
        print(f"{exp} →  válido")
    else:
        print(f"{exp} →  no válido")
"""



"""
2.  Implementa un algoritmo que convierta un número decimal a binario usando una
pila.
Ejemplo:
o 25 → 11001
"""
"""
Dividir el número entre 2.
Guardar el residuo en una pila.
Repetir hasta que el número sea 0.
Finalmente, desapilar todos los elementos → eso da el número en binario.
"""

"""
def decimal_a_binario(numero):
    pila = []
    # Paso 1: obtener residuos y apilarlos
    while numero > 0:
        residuo = numero % 2
        pila.append(residuo)  # apilar residuo
        numero //= 2
    # Paso 2: desapilar para formar el binario
    binario = ""
    while pila:
        binario += str(pila.pop())

    return binario if binario != "" else "0"


print("25 →", decimal_a_binario(25))  # 11001
print("8 →", decimal_a_binario(8))    # 1000
print("0 →", decimal_a_binario(0)) 
"""


"""
3. Simula el sistema de deshacer de un editor de texto. Cada operación se guarda en
una pila, y cuando el usuario elige “deshacer”, se recupera la última operación
"""
class EditorTexto:
    def __init__(self):
        self.texto = ""      # contenido actual
        self.historial = []  # pila de operaciones

    def escribir(self, nuevo_texto):
        self.historial.append(self.texto)
        self.texto += nuevo_texto

    def borrar(self, n):
        self.historial.append(self.texto)
        self.texto = self.texto[:-n]

    def deshacer(self):
        if self.historial:
            self.texto = self.historial.pop()
        else:
            print("No hay operaciones para deshacer.")

    def mostrar(self):
        print("Texto actual:", self.texto)

editor = EditorTexto()

editor.escribir("Hola")
editor.mostrar()  

editor.escribir(" Mundo")
editor.mostrar()   

editor.borrar(6)
editor.mostrar()  

editor.deshacer()
editor.mostrar()   

editor.deshacer() 
editor.mostrar()  
