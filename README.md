## Tabla de Participantes

| Nombre | Apellido | DNI | Email | Link_Git_Hub |
|---|---|---|---|---|
| Carlos | Garcia | 40518523 | carlos.edu.garcia8@gmail.com | https://github.com/douglasg14b |
| Raul | Moreno | 29201107 | moreno.r.alberto@gmail.com | https://github.com/morenoh149 |
| Félix | Tapia | 42217815 | felixcruztapia@gmail.com | https://github.com/FelixCBA/Ejercicio_de_clase.git |
| Alejandra | Zotta | 20774460 | alejandra.zotta@unc.edu.ar | https://github.com/alejandrazotta |

## Descripción del Proyecto " Asignación de Aulas"
El problema de la superposición de horarios y la asignación eficiente de aulas en las instituciones educativas es un desafío común que puede generar diversos inconvenientes, como la pérdida de tiempo, la frustración de los docentes y alumnos, y la mala utilización de los recursos disponibles. 
Para lograrlo  se necesita informatizar el sistema de reservas. Cuenta con los siguientes  datos de:
* los edificios (Nombre, Dirección, cantidad de pisos)
* las aulas (Nombre, Capacidad, ubicación física) con sus respectivas características (aulataller, proyector, clase en vivo, butacas, pupitres)
* los usuarios (Datos personales, Materia, Cargo)
* Horario de uso 07.00 a 22:00

## Modulos del programa

* **Principal.py**: En este módulo se encuentra el menú principal de la aplicación. Desde este módulo se llaman a las demás funciones que se encuentran en el módulo CRUD.
* **CRUD.py**: Aquí encontramos funciones encargadas de realizar los CRUD a todas las tablas de la base de datos.
* **Conexion_BD.py**: Este módulo se encarga de abrir una conexion con la bd y realizar la consulta que se le pase por parametros.Luego de esto se cierra la conexion con la                        BD.
* **Formateador.py**: Este módulo le da formato de tabla a los datos que se le pasan como parametro. Estos datos son los que se obtienen luego de las consultas a la BD.
* **Login.py**: Este módulo se encarga de logear a los usuarios y en caso de que no este registrado, se lo registra.
* **config**: En este archivo se guardan datos para configurar el programa tales como las credenciales para acceder a la BD.

## Mapa de aplicacion
![Python - Marco 1](https://github.com/carlosg14/Proyecto-integrados/assets/169003565/138303a1-01e9-4a5b-b495-7d2cc1447e95)

## Requrimientos para ejecutar programa.

* Tener [python 3.12](https://www.python.org/downloads/) 🐍
* Tener instalado el conector de python a mysql: [mysql-connector-python	8.4.0](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html) 📦
* Tener instalado [MySQL](https://dev.mysql.com/downloads/installer/)📦
 


  
