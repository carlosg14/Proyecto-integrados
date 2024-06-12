import CRUD
from os import system


def main():
    """
        En la funcion principal se presenta por consola el menu de opciones al usuario y
        en base a la eleccion del mismo se llama al procedimiento correspondiente.

        Retornos:

            [None]: Esta funcion no retorna nada.
    """


    dni_usuario = CRUD.login()

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

            # Se solicitan los datos
            capacidad_aula = int(input('Ingrese la capacidad que desea que tenga el aula: '))
            proyector = bool(int(input('Ingrese si quiere que posea proyector (1 -> si, 2 -> no.): ')))
            emicion_en_vivo = int(input('Ingrese si quiere que posea capacidad de emitir en vivo (1 -> si, 2 -> no.): '))
            tipo_aula = int(input('Ingrese el tipo de aula que desea reservar (1:Taller, 2:Auditorio, 3:Tradicional): '))
            horario_inicio = input('Ingrese el horario a recervar el aula (De 7 a 22 hs)(Formato Horas:Minutos): ')
            horario_finalizacion = input('Ingrese el horario de finalizacion (De 7 a 22 hs)(Formato Horas:Minutos): ')
            system('cls')
            CRUD.reservar_aula(dni_usuario, capacidad_aula, proyector, emicion_en_vivo,  tipo_aula, horario_inicio,
                               horario_finalizacion)
        elif opcion == "2":
            CRUD.cancelar_reserva()
        elif opcion == "3":
            cod_aula = int(input('Ingrese el codigo del aula: '))
            CRUD.ver_reservas(cod_aula)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()
