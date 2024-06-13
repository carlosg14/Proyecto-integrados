SELECT * FROM usuarios;

SELECT Nombre_Real, Tipo_Aula FROM aulas;

SELECT Nombre_Real FROM aulas WHERE Tipo_Aula = 1;

SELECT * FROM reserva WHERE Horario_Inicio BETWEEN '8:00' AND '14:00';

SELECT * FROM edificio limit 2;

SELECT * FROM edificio 
INNER JOIN aulas ON edificio.idedificio = aulas.idEdificio;

SELECT * FROM usuarios
INNER JOIN reserva ON usuarios.dni = reserva.DNI
WHERE usuarios.Nombre_Completo = 'admin';

SELECT * FROM usuarios WHERE Cargo = 3 AND Materia = 'Sistemas';

SELECT * FROM aulas WHERE Capacidad > 50;

SELECT Tipo_Aula FROM aulas 
GROUP BY Tipo_Aula;

SELECT Cargo, count(*) AS Cantidad FROM usuarios
GROUP BY Cargo; 

SELECT u.Nombre_Completo, count(*) AS Cantidad FROM usuarios u, telefonos t
WHERE u.dni = t.DNI
group by u.Nombre_Completo;
