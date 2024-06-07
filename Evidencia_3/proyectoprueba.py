def reservar_aula():
    # Opcion de reserva
    print("Agendando reserva...")

def cancelar_reserva():
    # Opcion de cancelacion
    print("Cancelando reserva...")

def ver_reserva():
    # Opcion de observacion de reserva
    print("Mostrando reserva...")

def main():
    while True:
        print("Menú:")
        print("1) Reservar aula")
        print("2) Cancelar reserva")
        print("3) Ver reserva")
        print("4) Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            reservar_aula()
            print ("su aula fue reservada con exito!")
        elif opcion == "2":
            cancelar_reserva()
            print ("su reserva fue cancelada")
        elif opcion == "3":
            ver_reserva()
            print ("procesando su reserva")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
if __name__ == "__main__":
    main()
