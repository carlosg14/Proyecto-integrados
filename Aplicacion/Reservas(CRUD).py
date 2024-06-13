from Conexion_BD import conexion_bd
from Formateador import formateador



def reservar_aula(dni_usuario, capacidad_aula, proyector, emision_en_vivo, tipo_aula, horario_inicio, horario_finalizacion):

    """
    En esta funcion se realiza la reserva de un aula, para lo cual primero se verifica si es posible efectuarla
    y luego se crea el registro correspondiente a la reserva en la base de datos.

    Parametros:

        dni_usuario [int]
        capacidad_aula [int]
        emision_en_vivo [bool] : True si posee capacidad de emitir en vivo.
        proyector [bool]: True si posee proyector, False si no.
        tipo_aula [int]: 1:Taller, 2:Auditorio, 3:Tradicional
        horario_inicio [string]: Horario en el cual se desea reservar el aula. Formato [%H:%M]
        horario_finalizacion [string]: Horario de finalizacion de la clase. Formato [%H:%M]

    Retornos:

        Esta funcion no retorna nada. Pero imprime en consola lo siguiente:
         - Si no es posible reservar el aula.
         - Si se pudo reservar el aula con exito.
    """
    # Esta consulta devuelve las aulas con las condiciones requeridas(capacidad, proyector, etc)
    # Ademas devuelve las aula que no estan reservadas o que estan reservadas en un horaio que solapa con el solicitado.
    consulta = (
        """
        SELECT idAulas, Nombre_Real FROM aulas 
        where Capacidad = %(capacidad_aula)s 
        and Proyector = %(proyector)s
        and Tipo_Aula = %(tipo_aula)s
        and Emision_en_vivo = %(emision_en_vivo)s
        and idAulas not in 
        (select idaula from reserva where Horario_Inicio between %(horario_inicio)s and %(horario_finalizacion)s 
        or Horario_Finalizacion between %(horario_inicio)s and %(horario_finalizacion)s)
        """
    )
    # Se cargan los datos necesarios para la consulta.
    datos = {
        'capacidad_aula': capacidad_aula,
        'proyector': proyector,
        'emision_en_vivo': emision_en_vivo,
        'tipo_aula': tipo_aula,
        'horario_inicio': horario_inicio,
        'horario_finalizacion': horario_finalizacion,
        'dni_usuario': dni_usuario
    }
    resultados = conexion_bd(consulta, datos, 1)

    # Se comunica el resultado al usuario.
    system('cls')
    print('Las aulas que cumplen con sus necesidades son: \n')
    encabezados = ['ID_Aula', 'Nombre']
    system('cls')
    formateador(resultados, encabezados)

    # Se registra la nueva reserva.
    id_aula = input('Ingrese el id del aula que desea reservar: ')
    datos['idAula'] = int(id_aula)
    insercion = (
        """
        insert into reserva (DNI, idaula, Horario_Inicio, Horario_Finalizacion) values
        (%(dni_usuario)s, %(idAula)s, %(horario_inicio)s, %(horario_finalizacion)s)
        """
    )
    conexion_bd(insercion, datos, 2)
    print('\n La reserva a sido registrada con exito.')


def cancelar_reserva(dni_usuario, horario_inicio, cod_aula):

    """
    Esta funcion se encarga de eliminar  o actualizar una reserva, para lo cual confirma si la misma
    existe y en ese caso cancela o actualiza la reserva.

    Parametros:

        dni_usuario [int]
        horario_inicio [datetime]: Horario de la reserva.
        cod_aula [int]: Codigo del aula reservada.

    """
    opcion = input('Dese cancelar o actualizar una reserva (1: Cancelar, 2: Actualizar):')
    if opcion == '1':
        consulta = ('DELETE FROM reserva where DNI = %(dni)s and Horario_Inicio = %(inicio)s and idaula = %(aula)s')
        datos = {'dni': dni_usuario, 'inicio': horario_inicio, 'aula': cod_aula}
        conexion_bd(consulta, datos, 4)
    elif opcion == '2':
        dni = int(input('Ingresa el DNI del nuevo titular de la reserva: '))
        actualizacion = ('UPDATE reserva SET DNI = %(nuevo)s where DNI = %(antiguo)s')
        datos = {'nuevo': dni, 'antiguo': dni_usuario}
        conexion_bd(actualizacion, datos, 3)


def ver_reservas(cod_aula):
    """
    Esta funcion muestra todos los registros de la tabla de reservas
    o filtra por los que tengan como ID a cod_aula.

    Parametros:
        cod_aula[Int]
    """
    while True:
        print('\n' * 50)
        opcion = input('Desea mostrar todas las reservas o filtrar por aula(1: Sin filtro, 2: Con filtro): ')
        if opcion == '1':
            consulta = ('SELECT * FROM reserva')
            resultados = conexion_bd(consulta, None, 1)
            formateador(resultados)
            volver = input('\n Presione una letra para volver al menu:  ')
            return
        elif opcion == '2':
            consulta = ('SELECT * FROM reserva WHERE idaula = %(cod_aula)s')
            datos = {'cod_aula': cod_aula}
            resultados = conexion_bd(consulta, datos, 1)
            system('cls')
            formateador(resultados)
            volver = input('\n Presione una letra para volver al menu:  ')
            return
        else:
            print('Opcion incorrecta')

