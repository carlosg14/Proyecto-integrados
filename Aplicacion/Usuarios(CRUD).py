from Conexion_BD import conexion_bd
from Formateador import formateador


def usuarios():
    while True:
        # Se imprime el menu.
        print('\n' * 50)
        print('=' * 30)
        print("Menú:")
        print('1. Mostrar tabla.')
        print('2. Insertar registro.')
        print('3. Actualizar mail de un usuario.')
        print('4. Eliminar un usuario.')
        print('5. Cantidad de n° de telefono por usuario.')
        print('6. Salir.')
        print('=' * 30)
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            formateador(conexion_bd(('SELECT * FROM usuarios'), None, 1))
            volver = input('\n Presione una letra para volver al menu:  ')
        elif opcion == '2':
            consulta = ("""
                       INSERT INTO usuarios (dni, Nombre_Completo, Cargo, Materia, Mail, Password) 
                       VALUES (%(dni)s, %(nombre)s, %(cargo)s, %(materia)s, %(mail)s, %(pass)s)
                   """)
            datos = {
                'dni': int(input('Ingrese el dni del nuevo usuario: ')),
                'nombre': input('Ingrese el nombre del usuario: '),
                'materia': input('Ingrese la materia del usuario: '),
                'mail': input('Ingrese el mail del usuario: '),
                'cargo': int(input('Ingrese su cargo (1: Docente, 2: Autoridad, 3:Alumno): ')),
                'pass': input('Ingrese su contraseña: ')
            }
            conexion_bd(consulta, datos, 2)
        elif opcion == '3':
            consulta = ('UPDATE usuarios SET mail = %(mail)s WHERE dni = %(dni)s')
            datos = {
                'dni': int(input('Ingrese el dni del usuario a actualizar: ')),
                'mail': int(input('Ingrese el nuevo mail del usuario: '))
            }
            conexion_bd(consulta, datos, 3)
        elif opcion == '4':
            consulta = ('DELETE FROM usuarios WHERE dni = %(dni)s')
            datos = {'dni': int(input('Ingrese el dni del usuario a eliminar: '))}
            conexion_bd(consulta, datos, 4)
        elif opcion == '5':
            consulta = ("""SELECT Nombre_Completo as Nombre, count(*) FROM usuario
                        inner join telefonos on usuario.dni = telefonos.DNI
                        GROUP BY usuario.Nombre
                        """)
            resultado = conexion_bd(consulta, None, 1)
            formateador(resultado)
            volver = input('\n Presione una letra para volver al menu:  ')
        elif opcion == '6':
            pass
        else:
            print('Opcion incorrecta.')
