from Conexion_BD import conexion_bd

def login():
    """
    Autenticacion de usuarios y registro de usuarios nuevos.

    Retornos
        dni [int]
    """
    print('\n' * 50)
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
                print('\n' * 50)
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
