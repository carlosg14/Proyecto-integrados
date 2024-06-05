Algoritmo Diseño
	
	Definir _opcion, dni_usuario, capacidad_aula, id_reserva, horario Como Entero
	Definir proyector, emision_vivo, aula_taller, con_pupitres, solo_butacas, bandera Como Logico 
	
	bandera = Verdadero
	
	Mientras bandera Hacer
// Se muestra el menu
		Escribir 'Gestor de reservas'
		Escribir '1- Reservar un aula.'
		Escribir '2- Eliminar reserva.'
		Escribir '3- Mostrar reservas.'
		Escribir '4- Salir.'
// Se solicita al usuario que seleccione una opcion		
		Escribir 'Ingrese el numero de la opcion: '
		Leer _opcion
// Se ejecuta el bloque se codigo que cumple la condicion logica
		Si _opcion = 1 Entonces
			// Se solicitan los datos necesarios para realizar la reserva
			Escribir 'Ingrese el Dni del usuario: '
			Leer dni_usuario
			Escribir 'Ingrese la capacidad del aula requerida: '
			Leer capacidad_aula
			Escribir 'Necesita que el aula posea proyector: '
			Leer proyector
			Escribir 'Necesita que el aula sea de tipo taller: '
			Leer aula_taller
			Escribir 'Necesita que el aula posea solo butacas: '
			Leer solo_butacas
			Escribir 'Necesita que el aula tenga pupitres: '
			Leer con_pupitres
			Escribir 'Necesita que en el aula se pueda transmitir en vivo la clase:  '
			Leer emision_vivo
			Escribir 'Ingrese el horario en el cual desea reservar el aula: '
			Leer horario
			
			
		Fin Si
		Si _opcion = 2 Entonces
			// Se solicitan los datos necesarios para cancelar una reserva.
		Fin Si
		Si _opcion = 3 Entonces
			
		Fin Si
		Si _opcion = 4 Entonces
			bandera = Falso
		Fin Si

	Fin Mientras
		
	
FinAlgoritmo
