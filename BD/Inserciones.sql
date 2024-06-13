use proyecto_aulas
 
INSERT INTO edificio (idedificio, NombreReal, Direccion, Ciudad, Cantidad_Pisos) VALUES
 (1, 'Pascal', 'Ariza 2000', 'Cordoba', 3),
 (2, 'Iñaki', 'Ariza 2000', 'Cordoba', 3),
 (3, 'San Martin', 'Junin 2100', 'Carlos Paz', 2),
 (4, 'Belgrano', 'Junin 1200', 'Carlos Paz', 1),
 (5, 'Industrial', 'Ariza 2030', 'Cordoba', 2),
 (6, 'Central', 'Ariza 2170', 'Cordoba', 4)
 
 
INSERT INTO aulas (idAulas, idEdificio, Piso, Nombre_Real, Capacidad, Emision_en_vivo, Proyector, Tipo_Aula) values
(1, 2, 2, 'Tesla', 100, 1, 1, 1),
(2, 3, 2, 'Alberdi', 200, 1, 0, 2),
(3, 4, 2, 'Einstein', 20, 0, 1, 3),
(4, 1, 2, 'Tesla_2', 250, 1, 1, 2),
(5, 5, 2, 'Tesla_2', 50, 1, 1, 1)

INSERT INTO usuarios (dni, Nombre_Completo, Cargo, Materia, Mail, Password) VALUES 	
(231000, 'Alberto Duran', 1, 'Fisica', 'alberto@unc.com', 'hola123'),
(231001, 'Ignacio Dumas', 2, 'Quimica', 'igna@unc.com', 'ig123'),
(231002, 'Juan Perez', 3, 'Sistemas', 'perez@unc.com', 'secreto2'),
(231003, 'Hernan Lopez', 1, 'Matematica', 'hernan@unc.com', 'enigma'),
(231004, 'admin', 2, 'Seguridad', 'admin@unc.com', '1234')

insert into reserva (DNI, idaula, Horario_Inicio, Horario_Finalizacion) values
(231000,5, '12:00', '13:00'),
(231003,2, '8:00', '13:00'),
(231002,3, '17:00', '18:00'),
(231004,4, '12:00', '13:00'),
(231000,5, '11:00', '12:00')

 INSERT INTO telefonos (DNI, Telefono) VALUES 
 (231000, 457000),
 (231000, 546564),
 (231001, 344365),
 (231001, 3243543),
 (231003, 4567004),
 (231004, 456731)
 