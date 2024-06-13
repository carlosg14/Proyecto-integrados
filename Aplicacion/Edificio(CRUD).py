from Conexion_BD import conexion_bd
from Formateador import formateador

def edificios():
    while True:
        # Se imprime el menu.
        print('\n' * 50)
        print('=' * 30)
        print("Menú:")
        print('1. Mostrar tabla.')
        print('2. Insertar registro.')
        print('3. Actualizar nombre de un edificio.')
        print('4. Eliminar un aula.')
        print('5. Salir.')
        print('=' * 30)
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            formateador(conexion_bd(('SELECT * FROM edificio'), None, 1))
            volver = input('\n Presione una letra para volver al menu:  ')
        elif opcion == '2':
            consulta = ("""
                INSERT INTO aulas (idedificio, NombreReal, Direccion, Ciudad, Cantidad_Pisos) 
                VALUES (%(id)s, %(nombre)s, %(direccion)s, %(ciudad)s, %(pisos)s)
            """)
            datos = {
                'id': int(input('Ingrese el id del nuevo edificio: ')),
                'nombre': input('Ingrese el nombre del edificio: '),
                'direccion':input('Ingrese la direccion del edificio: '),
                'ciudad': input('Ingrese la ciudad del edificio: '),
                'pisos': int(input('Ingrese la cantidad de pisos que tiene el edificio: '))
            }
            conexion_bd(consulta, datos, 2)
        elif opcion == '3':
            consulta = ('UPDATE aulas SET NombreReal = %(nombre)s WHERE idedificio = %(id)s')
            datos = {
                'id': int(input('Ingrese el id del edificio a actualizar: ')),
                'nombre': int(input('Ingrese el nuevo nombre del edificio'))
            }
            conexion_bd(consulta, datos, 3)
        elif opcion == '4':
            consulta = ('DELETE FROM edificio WHERE idedificio = %(id)s')
            datos = {'id': int(input('Ingrese el id del edificio a eliminar: '))}
            conexion_bd(consulta, datos, 4)
        elif opcion == '5':
            break
        else:
            print('Opcion incorrecta.')
