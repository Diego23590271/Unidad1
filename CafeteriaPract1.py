# ALGORITMO CafeteriaColaPila
# 1. Inicio
# 2. Declarar las variables globales:
#    Pila <- vacía
#    Cola <- vacía
#    Productos[3] <- {"Torta","Sandwich","Dobladita"}
#    N <- 0 , i <- 0 , Indice <- 0 , Prod <- "" , Persona <- ""
# 3. Escribir: "¿Cuántos productos desea generar?"
# 4. Leer: N
# 5. Para i <- 1 Hasta N Hacer
#    5.1 Indice <- Random(0,2)   # número aleatorio entre 0 y 2
#    5.2 Prod <- Productos[Indice]
#    5.3 Apilar(Pila, Prod)
#    5.4 Escribir: "Se agregó: ", Prod
# 6. Fin Para
# 7. Escribir: "Insertando 3 personas en la cola..."
# 8. Para i <- 1 Hasta 3 Hacer
#    8.1 Persona <- "Persona " + ConvertirATexto(i)
#    8.2 Encolar(Cola, Persona)
#    8.3 Escribir: Persona , " se formó en la cola"
# 9. Fin Para
# 10. Escribir: "Atendiendo a las personas:"
# 11. Mientras NO EsColaVacia(Cola) Hacer
#     11.1 Persona <- Desencolar(Cola)
#     11.2 Si NO EsPilaVacia(Pila) Entonces
#          11.2.1 Prod <- Desapilar(Pila)
#          11.2.2 Escribir: Persona , " recibe ", Prod
#     11.3 SiNo
#          11.3.1 Escribir: Persona , " no alcanzó producto"
#     11.4 FinSi
# 12. Fin Mientras
# 13. Fin

# ALGORITMO CafeteriaColaPila en Python

import random
from collections import deque

def cafeteria_cola_pila():
    pila = [] 
    cola = deque()  
    productos = ["Torta", "Sandwich", "Dobladita"]  
    N = 0  

    N = int(input("¿Cuántos productos desea generar?: "))

    for i in range(N):
        indice = random.randint(0, 2)  
        prod = productos[indice]
        pila.append(prod)  
        print("Se agregó:", prod)

    print("\nInsertando 3 personas en la cola...")
    for i in range(1, 4):
        persona = "Persona " + str(i)
        cola.append(persona)  
        print(persona, "se formó en la cola")

    print("\nAtendiendo a las personas:")
    while len(cola) > 0: 
        persona = cola.popleft()  
        if len(pila) > 0:  
            prod = pila.pop()  
            print(persona, "recibe", prod)
        else:
            print(persona, "no alcanzó producto")

cafeteria_cola_pila()
