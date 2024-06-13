from Conexion_BD import conexion_bd
from Formateador import formateador

def aulas():
    """
    Esta funcion realiza el CRUD de la tabla aulas.
    """
    while True:
        # Se imprime el menu.
        print('\n' * 50)
        print('=' * 30)
        print("Menú:")
        print('1. Mostrar tabla.')
        print('2. Insertar registro.')
        print('3. Actualizar capacidad de un aula.')
        print('4. Eliminar un aula.')
        print('5. Salir.')
        print('=' * 30)
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            formateador(conexion_bd(('SELECT * FROM aulas'), None, 1))
            volver = input('\n Presione una letra para volver al menu:  ')
        elif opcion == '2':
            consulta = ("""
                       INSERT INTO aulas (idAulas, idEdificio, Piso, Nombre_Real, Capacidad, Emision_en_vivo, Proyector, Tipo_Aula) 
                       VALUES (%(id)s, %(edificio)s, %(piso)s, %(nombre)s, %(capacidad)s, %(emision)s, %(proyector)s, %(tipo_aula)s)
                   """)
            datos = {
                'id': int(input('Ingrese el id de la nueva aula: ')),
                'edificio': int(input('Ingrese el id del edificio al cual pertenece el aula: ')),
                'piso': int(input('Ingrese el piso en el cual se encuentra el aula: ')),
                'nombre': input('Ingrese el nombre del aula: '),
                'capacidad': int(input('Ingrese la capacidad del aula: ')),
                'emision': int(input('Ingrese si tiene capacidad de emitir en vivo (1 -> si, 0 -> no.): ')),
                'proyector': int(input('Ingrese si tiene  proyector (1 -> si, 0 -> no.): ')),
                'tipo_aula': int(input('Ingrese el tipo de aula que desea reservar (1:Taller, 2:Auditorio, 3:Tradicional): '))
            }
            conexion_bd(consulta, datos, 2)
        elif opcion == '3':
            consulta = ('UPDATE aulas SET capacidad = %(capacidad)s WHERE idAulas = %(id)s')
            datos = {
                'id': int(input('Ingrese el id del aula a actualizar: ')),
                'capacidad': int(input('Ingrese la nueva capacidad del aula'))
            }
            conexion_bd(consulta, datos, 3)
        elif opcion == '4':
            consulta = ('DELETE FROM aulas WHERE idAula = %(id)s')
            datos = {'id': int(input('Ingrese el id del aula a eliminar: '))}
            conexion_bd(consulta, datos, 4)
        elif opcion == '5':
            break
        else:
           print('Opcion incorrecta.')
