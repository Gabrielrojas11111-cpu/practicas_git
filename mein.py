from funtions import suma
from calculos import calclar_area_c,calcular_area_t,calcular_area_cu
triangulo=calcular_area_t
caudrado=calclar_area_c


#programa
print("hola mundo")
resultado= suma(5,10)
print(resultado)


# menu_areas.py


def mostrar_menu():
    print("\n--- MENÚ DE ÁREAS ---")
    print("1. Área de un triángulo")
    print("2. Área de un cuadrado")
    print("3.suma")
    print("4.area del circulo")
    print("5. Salir")

def menu_git():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")


        if opcion == "1":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            print("Área del triángulo:", calcular_area_t(base, altura))

        elif opcion == "2":
            lado = float(input("Ingresa el lado del cuadrado: "))
            print("Área del cuadrado:", calclar_area_c(lado))

        elif opcion == "3":
            a = float(input("el numero a sumar: "))
            b = float(input("el siguiente numero para sumar: "))
            print("area del cuadradro:", suma(a,b))

        elif opcion =="4":
            radio=float(input("ingresar la area de circulo: "))
            print("la area de un circulo es:",calcular_area_cu(radio))

        if opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
menu_git()