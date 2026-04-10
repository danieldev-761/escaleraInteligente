#Escalera inteligente

#Objetivo: Mostrar en una pantalla cada paso que una persona debe dar para bajar desde un piso hasta el primer piso


print("--------------- ESCALERA INTELIGENTE ----------------")
nombre= str(input("Ingrese el nombre del usuario: "))
piso_actual= int(input("Ingrese el piso en el que se encuentra: "))


primer_piso= 1

if primer_piso == piso_actual:
    print("Señor usuario, ya se encuentra en el primer piso.")

while piso_actual != primer_piso:

    print(f"Estoy en piso {piso_actual}. El siguiente paso es bajar uno. \n")

    #El piso actual disminuye en 1 cada vez que el piso baja.
    piso_actual= piso_actual -1

    if piso_actual == primer_piso:
        print("Ha llegado al piso 1. Gracias por utilizar nuestros servicios.") 

    else:
        print(f"Usuario {nombre}, baja al piso {piso_actual}.")
        
        





