from Conexion_BD import conexion_bd
from Formateador import formateador

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
    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    else:
        print('Opcion incorrecta.')
