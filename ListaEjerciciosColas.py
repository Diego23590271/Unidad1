#colas
#4to ejercicio simulacion de cajeri automatico
"""
Simulación de cajero automático Modela la fila de un cajero automático con una cola. 
Cada cliente tiene un nombre y una transacción (retiro, depósito, consulta). 
Los clientes deben ser atendidos en orden de llegada
"""
"""
from collections import deque

class Cliente:
    def __init__(self, nombre, transaccion):
        self.nombre = nombre
        self.transaccion = transaccion

    def __str__(self):
        return f"{self.nombre} ({self.transaccion})"


class CajeroAutomatico:
    def __init__(self):
        self.cola = deque()

    def nuevo_cliente(self, cliente):
        self.cola.append(cliente)
        print(f"{cliente} llegó a la fila.")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo a {cliente}.")
        else:
            print("No hay clientes en la fila.")

    def mostrar_fila(self):
        if self.cola:
            print("Fila actual:", " -> ".join(str(c) for c in self.cola))
        else:
            print("La fila está vacía.")


cajero = CajeroAutomatico()

cajero.nuevo_cliente(Cliente("Ana", "Retiro"))
cajero.nuevo_cliente(Cliente("Luis", "Depósito"))
cajero.nuevo_cliente(Cliente("Marta", "Consulta"))

cajero.mostrar_fila()

cajero.atender_cliente()
cajero.mostrar_fila()

cajero.atender_cliente()
cajero.atender_cliente()
cajero.atender_cliente()
"""


#5to Ejercicio Cola circular para turnos
"""
class ColaCircular:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.indice = 0  # primer jugador

    def turno_actual(self):
        return self.jugadores[self.indice]

    def siguiente_turno(self):
        self.indice = (self.indice + 1) % len(self.jugadores)
        return self.turno_actual()

jugadores = ["Ana", "Luis", "Marta", "Carlos"]
cola = ColaCircular(jugadores)

#Simulamos rango
for i in range(7):
    print(f"Turno {i+1}: {cola.turno_actual()}")
    cola.siguiente_turno()
"""


#6to Ejercicio impresora compartida
"""
Diseña una simulación de una cola de impresión, donde diferentes usuarios envían
documentos. Cada documento tiene un tamaño y deben imprimirse en orden de
llegada
"""
from collections import deque
import time

class Documento:
    def __init__(self, usuario, nombre, tamaño):
        self.usuario = usuario
        self.nombre = nombre
        self.tamaño = tamaño  # en páginas

    def __str__(self):
        return f"{self.nombre} ({self.tamaño} pág.) de {self.usuario}"


class ColaImpresion:
    def __init__(self):
        self.cola = deque()

    def enviar_documento(self, documento):
        self.cola.append(documento)
        print(f"Documento enviado: {documento}")

    def imprimir(self):
        if self.cola:
            doc = self.cola.popleft()
            print(f"🖨 Imprimiendo: {doc}")
            time.sleep(0.5)  # simulamos tiempo de impresión
            print(f"Documento impreso: {doc}")
        else:
            print("No hay documentos en la cola.")

    def mostrar_cola(self):
        if self.cola:
            print("Cola de impresión:", " -> ".join(str(d) for d in self.cola))
        else:
            print("La cola de impresión está vacía.")
            

impresora = ColaImpresion()

impresora.enviar_documento(Documento("Ana", "Tarea1.pdf", 5))
impresora.enviar_documento(Documento("Luis", "Informe.docx", 3))
impresora.enviar_documento(Documento("Marta", "Presentación.pptx", 7))

impresora.mostrar_cola()

impresora.imprimir()
impresora.imprimir()
impresora.imprimir()
impresora.imprimir()


