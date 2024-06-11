import CRUD


def main():
    """
        En la funcion principal se presenta por consola el menu de opciones al usuario y
        en base a la eleccion del mismo se llama al procedimiento correspondiente.

        Retornos:

            [None]: Esta funcion no retorna nada.
    """
    while True:

        # Impresion del menu.
        print('=' * 30)
        print("Menú:")
        print("1) Reservar aula")
        print("2) Cancelar reserva")
        print("3) Ver reserva")
        print("4) Salir")
        print('=' * 30)
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        # Llamada a la funcion correspondiente.
        if opcion == "1":
            CRUD.reservar_aula()
        elif opcion == "2":
            CRUD.cancelar_reserva()
        elif opcion == "3":
            CRUD.ver_reserva()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()
