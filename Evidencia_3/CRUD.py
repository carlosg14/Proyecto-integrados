def reservar_aula(dni_usuario, capacidad_aula, proyector, aula_taller, solo_butacas, con_pupitres, horarios):

    """
    En esta funcion se realiza la reserva de un aula, para lo cual primero se verifica si es posible efectuarla
    y luego se crea el registro correspondiente a la reserva en la base de datos.

    Parametros:

        dni_usuario [int]
        capacidad_aula [int]
        proyector [bool]: True si posee proyector, False si no.
        aula_taller [bool]: True si se pueden hacer tareas como dibujo, electronica, etc, False si no.
        solo_butacas [bool]: True si solo posee butacas, False si no.
        con_pupitres [bool] True si solo posee pupitres, False si no.
        horario [datetime]: Horario en el cual se desea reservar el aula.

    Retornos:

        Esta funcion no retorna nada. Pero imprime en consola lo siguiente:
         - Si no es posible reservar el aula.
         - Si se pudo reservar el aula con exito.
    """

    print("Agendando reserva...")


def cancelar_reserva(dni_usuario, horario, cod_aula ):

    """
    Esta funcion se encarga de eliminar una reserva, para lo cual confirma si la misma
    existe y en ese caso cancela la reserva.

    Parametros:

        dni_usuario [int]
        horario [datetime]: Horario de la reserva.
        cod_aula [int]: Codigo del aula reservada.

    Rertorno:

        Esta funcion no retorna nada. Pero imprime en pantalla:
         - Si la reserva fue cancelada con exito.

    """
    print("Cancelando reserva...")

def ver_reservas(dni_usuario, horario, cod_aula ):
    """
    Esta funcion muestra la tabla de reservas. La cual solicita al gestor
    de base de datos MySql.

    """
    print("Mostrando reserva...")
