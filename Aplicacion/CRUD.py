from Conexion_BD import conexion_bd
from datetime import datetime
from os import system


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


def cancelar_reserva(dni_usuario, horario, cod_aula):

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


def ver_reservas(cod_aula):
    """
    Esta funcion muestra los registros de la tabla de reservas que tengan como ID a cod_aula.

    Parametros:
        cod_aula[Int]
    """
    consulta = ('SELECT * FROM reserva WHERE idaula = %(cod_aula)s')
    datos = {'cod_aula': cod_aula}
    resultados = conexion_bd(consulta, datos, 1)
    system('cls')
    formateador(resultados)
    volver = input('\n Presione una letra para volver al menu:  ')
    return

def crud():
    pass


def formateador(resultados: list) -> None:

    """
   Esta funcion se encarga de presentar en formato de tabla a traves de la consola los datos que contiene
   resultado.

    Parametros:
        - resultado [list]: Lista de dicionarios que contiene resultados de una consulta SQL.

    Retornos:
        - None: Esta funcion no retorna nada
    """

    # Creacion e impresion del encambezado de cada tabla.
    print('=' * len(resultados[0]) * 21 + '=')
    linea = '|'
    for resultado in resultados[0].keys():
        linea = linea + '{:^20}|'.format(str(resultado))
    print(linea)
    print('=' * len(linea))

    # Insersion de los datos en una tabla e impresion de la misma.
    for registro in resultados:
        linea = '|'
        for atributo in registro.values():
            linea = linea + '{:^20}|'.format(str(atributo))
        print(linea)
        print('-' * len(linea))
    print('')


def login():
    """
    Autenticacion de usuarios y registro de usuarios nuevos.

    Retornos
        dni [int]
    """
    nuevo = input('Ingrese 1 si ya tiene usario, 0 si no: ')
    if nuevo == '1':
        # Se auntentifica la identidad del usuario.
        while True:
            usuario = int(input('Ingrese su DNI: '))
            passw = input('Ingrese su contraseña: ')
            consulta = ('SELECT Password FROM usuarios where dni = %(dni)s ')
            dato = {'dni': usuario}
            credencial = conexion_bd(consulta, dato, 1)

            if credencial[0]['Password'] == passw:
                system('cls')
                return usuario
            else:
                print('Contraseña invalida')
    else:
        # Se solicitan datos para registrarse en el sitema.
        dni = int(input('Ingrese su DNI: '))
        nombre = input('Ingrese su nombre: ')
        cargo = int(input('Ingrese su cargo (1: Docente, 2: Autoridad, 3:Alumno): '))
        materia = input('Ingrese la materia: ')
        mail = input('Ingrese su mail: ')
        passw = input('Ingrese su contraseña: ')

        insercion = (
            """
            INSERT INTO usuarios (dni, Nombre_Completo, Cargo, Materia, Mail, Password) values
            (%(dni)s, %(nombre)s, %(cargo)s, %(materia)s, %(mail)s, %(passw)s)
            """
        )

        datos = {
            'dni': dni,
            'nombre': nombre,
            'cargo': cargo,
            'materia': materia,
            'mail': mail,
            'passw': passw
        }
        conexion_bd(insercion, datos, 2)
        return dni
