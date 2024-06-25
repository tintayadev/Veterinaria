-- Habilitar claves foráneas
PRAGMA foreign_keys = ON;

-- Crear la tabla Mascota
CREATE TABLE Mascota (
    ID_Mascota INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Raza VARCHAR(50),
    Especie VARCHAR(50) NOT NULL,
    Edad INT,
    Peso DECIMAL(5,2),
    Sexo CHAR(1),
    FechaNacimiento DATE,
    ID_Dueno INT NOT NULL,
    FOREIGN KEY (ID_Dueno) REFERENCES Dueno(ID_Dueno)
);

-- Crear la tabla Dueno
CREATE TABLE Dueno (
    ID_Dueno INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(100),
    Email VARCHAR(50)
);

-- Crear la tabla Cita
CREATE TABLE Cita (
    ID_Cita INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    ID_Mascota INT NOT NULL,
    ID_Dueno INT NOT NULL,
    ID_Veterinario INT NOT NULL,
    Motivo VARCHAR(100),
    FOREIGN KEY (ID_Mascota) REFERENCES Mascota(ID_Mascota),
    FOREIGN KEY (ID_Dueno) REFERENCES Dueno(ID_Dueno),
    FOREIGN KEY (ID_Veterinario) REFERENCES Veterinario(ID_Veterinario)
);

-- Crear la tabla Tratamiento
CREATE TABLE Tratamiento (
    ID_Tratamiento INTEGER PRIMARY KEY AUTOINCREMENT,
    Descripcion VARCHAR(200) NOT NULL,
    Dosis VARCHAR(50),
    Duracion VARCHAR(50),
    FechaInicio DATE,
    FechaFin DATE,
    ID_Mascota INT NOT NULL,
    FOREIGN KEY (ID_Mascota) REFERENCES Mascota(ID_Mascota)
);

-- Crear la tabla Facturacion
CREATE TABLE Facturacion (
    ID_Factura INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha DATE NOT NULL,
    ID_Cita INT NOT NULL,
    ID_Dueno INT NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    Pagado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (ID_Cita) REFERENCES Cita(ID_Cita),
    FOREIGN KEY (ID_Dueno) REFERENCES Dueno(ID_Dueno)
);

-- Crear la tabla Especialidad
CREATE TABLE Especialidad (
    ID_Especialidad INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(200)
);

-- Crear la tabla Veterinario
CREATE TABLE Veterinario (
    ID_Veterinario INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50) NOT NULL,
    ID_Especialidad INT NOT NULL,
    Telefono VARCHAR(20),
    Email VARCHAR(50),
    FOREIGN KEY (ID_Especialidad) REFERENCES Especialidad(ID_Especialidad)
);

-- Crear la tabla Consulta
CREATE TABLE Consulta (
    ID_Consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Diagnostico VARCHAR(200),
    Observaciones TEXT,
    ID_Cita INT NOT NULL,
    ID_Veterinario INT NOT NULL,
    FOREIGN KEY (ID_Cita) REFERENCES Cita(ID_Cita),
    FOREIGN KEY (ID_Veterinario) REFERENCES Veterinario(ID_Veterinario)
);

-- Crear la tabla Cirugia
CREATE TABLE Cirugia (
    ID_Cirugia INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha DATE NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(200),
    ID_Mascota INT NOT NULL,
    ID_Veterinario INT NOT NULL,
    FOREIGN KEY (ID_Mascota) REFERENCES Mascota(ID_Mascota),
    FOREIGN KEY (ID_Veterinario) REFERENCES Veterinario(ID_Veterinario)
);

-- Crear la tabla Hospitalizacion
CREATE TABLE Hospitalizacion (
    ID_Hospitalizacion SERIAL PRIMARY KEY,
    FechaIngreso DATE NOT NULL,
    FechaAlta DATE,
    Motivo VARCHAR(200),
    ID_Mascota INT NOT NULL,
    ID_Veterinario INT NOT NULL,  -- Agregar la columna ID_Veterinario
    FOREIGN KEY (ID_Mascota) REFERENCES Mascota(ID_Mascota),
    FOREIGN KEY (ID_Veterinario) REFERENCES Veterinario(ID_Veterinario)
);

-- Insertar datos en la tabla Dueno
INSERT INTO Dueno (Nombre, Apellidos, Telefono, Direccion, Email) VALUES 
('Juan', 'Perez', '123456789', 'Calle Falsa 123', 'juan.perez@example.com'),
('Maria', 'Gonzalez', '987654321', 'Avenida Siempre Viva 456', 'maria.gonzalez@example.com'),
('Carlos', 'Ramirez', '555555555', 'Boulevard Central 789', 'carlos.ramirez@example.com'),
('Ana', 'Lopez', '111111111', 'Calle Luna 1', 'ana.lopez@example.com'),
('Pedro', 'Martinez', '222222222', 'Calle Sol 2', 'pedro.martinez@example.com'),
('Lucia', 'Diaz', '333333333', 'Calle Estrella 3', 'lucia.diaz@example.com'),
('Miguel', 'Torres', '444444444', 'Calle Mar 4', 'miguel.torres@example.com'),
('Laura', 'Morales', '555555555', 'Calle Viento 5', 'laura.morales@example.com'),
('Jorge', 'Hernandez', '666666666', 'Calle Fuego 6', 'jorge.hernandez@example.com'),
('Sofia', 'Fernandez', '777777777', 'Calle Agua 7', 'sofia.fernandez@example.com'),
('Raul', 'Garcia', '888888888', 'Calle Nube 8', 'raul.garcia@example.com'),
('Elena', 'Sanchez', '999999999', 'Calle Rayo 9', 'elena.sanchez@example.com'),
('Diego', 'Vargas', '101010101', 'Calle Trueno 10', 'diego.vargas@example.com'),
('Julia', 'Rojas', '202020202', 'Calle Tormenta 11', 'julia.rojas@example.com'),
('Fernando', 'Castro', '303030303', 'Calle Relampago 12', 'fernando.castro@example.com');

-- Insertar datos en la tabla Mascota
INSERT INTO Mascota (Nombre, Raza, Especie, Edad, Peso, Sexo, FechaNacimiento, ID_Dueno) VALUES 
('Fido', 'Labrador', 'Perro', 5, 30.5, 'M', '2019-01-01', 1),
('Whiskers', 'Siames', 'Gato', 3, 4.3, 'F', '2020-06-15', 2),
('Rex', 'Pastor Alemán', 'Perro', 7, 25.0, 'M', '2017-08-21', 3),
('Bella', 'Bulldog', 'Perro', 4, 20.0, 'F', '2020-05-10', 4),
('Milo', 'Beagle', 'Perro', 2, 10.0, 'M', '2021-09-14', 5),
('Luna', 'Persa', 'Gato', 3, 3.5, 'F', '2020-07-23', 6),
('Max', 'Boxer', 'Perro', 6, 28.0, 'M', '2018-03-15', 7),
('Coco', 'Chihuahua', 'Perro', 1, 2.5, 'F', '2022-11-19', 8),
('Rocky', 'Husky', 'Perro', 8, 35.0, 'M', '2016-12-01', 9),
('Oliver', 'Maine Coon', 'Gato', 4, 5.0, 'M', '2019-06-30', 10),
('Simba', 'Ragdoll', 'Gato', 5, 6.0, 'M', '2018-11-05', 11),
('Daisy', 'Shih Tzu', 'Perro', 2, 8.0, 'F', '2021-02-27', 12),
('Lola', 'Poodle', 'Perro', 3, 7.5, 'F', '2020-10-09', 13),
('Nina', 'Sphynx', 'Gato', 2, 3.0, 'F', '2021-12-25', 14),
('Buddy', 'Golden Retriever', 'Perro', 6, 32.0, 'M', '2018-08-18', 15);

-- Insertar datos en la tabla Especialidad
INSERT INTO Especialidad (Nombre, Descripcion) VALUES 
('Cirugía', 'Especialidad en procedimientos quirúrgicos'),
('Dermatología', 'Especialidad en problemas de la piel'),
('Cardiología', 'Especialidad en problemas del corazón'),
('Oftalmología', 'Especialidad en problemas de los ojos'),
('Neurología', 'Especialidad en problemas del sistema nervioso'),
('Ortopedia', 'Especialidad en problemas óseos y musculares'),
('Endocrinología', 'Especialidad en problemas hormonales'),
('Gastroenterología', 'Especialidad en problemas digestivos'),
('Oncología', 'Especialidad en cáncer y tumores'),
('Nefrología', 'Especialidad en problemas renales'),
('Urología', 'Especialidad en problemas urinarios'),
('Odontología', 'Especialidad en problemas dentales'),
('Rehabilitación', 'Especialidad en recuperación física'),
('Anestesiología', 'Especialidad en anestesia y manejo del dolor'),
('Nutrición', 'Especialidad en dietética y nutrición animal');

-- Insertar datos en la tabla Veterinario
INSERT INTO Veterinario (Nombre, Apellidos, ID_Especialidad, Telefono, Email) VALUES 
('Ana', 'Martinez', 1, '111222333', 'ana.martinez@example.com'),
('Luis', 'Fernandez', 2, '444555666', 'luis.fernandez@example.com'),
('Elena', 'Diaz', 3, '777888999', 'elena.diaz@example.com'),
('Juan', 'Mendez', 4, '121212121', 'juan.mendez@example.com'),
('Maria', 'Suarez', 5, '343434343', 'maria.suarez@example.com'),
('Pedro', 'Lopez', 6, '565656565', 'pedro.lopez@example.com'),
('Lucia', 'Perez', 7, '787878787', 'lucia.perez@example.com'),
('Miguel', 'Gomez', 8, '909090909', 'miguel.gomez@example.com'),
('Laura', 'Garcia', 9, '232323232', 'laura.garcia@example.com'),
('Jorge', 'Morales', 10, '454545454', 'jorge.morales@example.com'),
('Sofia', 'Vega', 11, '676767676', 'sofia.vega@example.com'),
('Raul', 'Jimenez', 12, '898989898', 'raul.jimenez@example.com'),
('Elena', 'Navas', 13, '010101010', 'elena.navas@example.com'),
('Diego', 'Zapata', 14, '303030303', 'diego.zapata@example.com'),
('Julia', 'Rivas', 15, '505050505', 'julia.rivas@example.com');

-- Insertar datos en la tabla Cita
INSERT INTO Cita (Fecha, Hora, ID_Mascota, ID_Dueno, ID_Veterinario, Motivo) VALUES 
('2024-07-01', '10:00:00', 1, 1, 1, 'Consulta general'),
('2024-07-02', '11:30:00', 2, 2, 2, 'Chequeo dermatológico'),
('2024-07-03', '09:00:00', 3, 3, 3, 'Revisión cardíaca'),
('2024-07-04', '08:30:00', 4, 4, 4, 'Chequeo ocular'),
('2024-07-05', '14:00:00', 5, 5, 5, 'Consulta neurológica'),
('2024-07-06', '13:00:00', 6, 6, 6, 'Chequeo ortopédico'),
('2024-07-07', '15:00:00', 7, 7, 7, 'Consulta endocrinológica'),
('2024-07-08', '12:00:00', 8, 8, 8, 'Consulta gastrointestinal'),
('2024-07-09', '16:00:00', 9, 9, 9, 'Consulta oncológica'),
('2024-07-10', '10:30:00', 10, 10, 10, 'Consulta nefrológica'),
('2024-07-11', '11:00:00', 11, 11, 11, 'Consulta urológica'),
('2024-07-12', '14:30:00', 12, 12, 12, 'Chequeo dental'),
('2024-07-13', '09:30:00', 13, 13, 13, 'Consulta de rehabilitación'),
('2024-07-14', '08:00:00', 14, 14, 14, 'Consulta de anestesia'),
('2024-07-15', '13:30:00', 15, 15, 15, 'Consulta nutricional');

-- Insertar datos en la tabla Tratamiento
INSERT INTO Tratamiento (Descripcion, Dosis, Duracion, FechaInicio, FechaFin, ID_Mascota) VALUES 
('Antibióticos para infección', '1 pastilla cada 8 horas', '7 días', '2024-07-01', '2024-07-07', 1),
('Cremas para la piel', 'Aplicar dos veces al día', '10 días', '2024-07-02', '2024-07-12', 2),
('Medicamento para el corazón', '1 pastilla al día', '30 días', '2024-07-03', '2024-08-02', 3),
('Gotas oculares', '3 gotas cada 6 horas', '5 días', '2024-07-04', '2024-07-09', 4),
('Medicamento para el sistema nervioso', '2 pastillas al día', '15 días', '2024-07-05', '2024-07-20', 5),
('Suplemento para articulaciones', '1 pastilla al día', '30 días', '2024-07-06', '2024-08-05', 6),
('Hormonas tiroideas', '1 pastilla al día', '90 días', '2024-07-07', '2024-10-05', 7),
('Medicamento digestivo', '1 pastilla cada 12 horas', '20 días', '2024-07-08', '2024-07-28', 8),
('Quimioterapia', 'Inyección cada semana', '12 semanas', '2024-07-09', '2024-09-25', 9),
('Diurético', '1 pastilla cada 8 horas', '14 días', '2024-07-10', '2024-07-24', 10),
('Antibiótico para infección urinaria', '1 pastilla cada 12 horas', '10 días', '2024-07-11', '2024-07-21', 11),
('Limpieza dental', 'Aplicar gel cada 12 horas', '7 días', '2024-07-12', '2024-07-19', 12),
('Fisioterapia', 'Ejercicios diarios', '30 días', '2024-07-13', '2024-08-12', 13),
('Anestesia general', 'Dosis única', 'Procedimiento', '2024-07-14', '2024-07-14', 14),
('Dieta especializada', '1 vez al día', '60 días', '2024-07-15', '2024-09-13', 15);

-- Insertar datos en la tabla Facturacion
INSERT INTO Facturacion (Fecha, ID_Cita, ID_Dueno, Total, Pagado) VALUES 
('2024-07-01', 1, 1, 150.00, FALSE),
('2024-07-02', 2, 2, 200.00, TRUE),
('2024-07-03', 3, 3, 300.00, FALSE),
('2024-07-04', 4, 4, 180.00, TRUE),
('2024-07-05', 5, 5, 250.00, FALSE),
('2024-07-06', 6, 6, 220.00, TRUE),
('2024-07-07', 7, 7, 270.00, FALSE),
('2024-07-08', 8, 8, 230.00, TRUE),
('2024-07-09', 9, 9, 310.00, FALSE),
('2024-07-10', 10, 10, 190.00, TRUE),
('2024-07-11', 11, 11, 210.00, FALSE),
('2024-07-12', 12, 12, 160.00, TRUE),
('2024-07-13', 13, 13, 240.00, FALSE),
('2024-07-14', 14, 14, 140.00, TRUE),
('2024-07-15', 15, 15, 280.00, FALSE);

-- Insertar datos en la tabla Consulta
INSERT INTO Consulta (Fecha, Hora, Diagnostico, Observaciones, ID_Cita, ID_Veterinario) VALUES 
('2024-07-01', '10:00:00', 'Infección bacteriana', 'Se receta antibiótico', 1, 1),
('2024-07-02', '11:30:00', 'Dermatitis', 'Se receta crema', 2, 2),
('2024-07-03', '09:00:00', 'Problema cardíaco', 'Se receta medicamento', 3, 3),
('2024-07-04', '08:30:00', 'Conjuntivitis', 'Se receta gotas', 4, 4),
('2024-07-05', '14:00:00', 'Epilepsia', 'Se receta medicamento', 5, 5),
('2024-07-06', '13:00:00', 'Artritis', 'Se receta suplemento', 6, 6),
('2024-07-07', '15:00:00', 'Hipotiroidismo', 'Se receta hormonas', 7, 7),
('2024-07-08', '12:00:00', 'Gastritis', 'Se receta medicamento', 8, 8),
('2024-07-09', '16:00:00', 'Tumor', 'Se inicia quimioterapia', 9, 9),
('2024-07-10', '10:30:00', 'Insuficiencia renal', 'Se receta diurético', 10, 10),
('2024-07-11', '11:00:00', 'Infección urinaria', 'Se receta antibiótico', 11, 11),
('2024-07-12', '14:30:00', 'Problemas dentales', 'Se receta gel dental', 12, 12),
('2024-07-13', '09:30:00', 'Fractura', 'Se inicia fisioterapia', 13, 13),
('2024-07-14', '08:00:00', 'Cirugía programada', 'Se realiza anestesia general', 14, 14),
('2024-07-15', '13:30:00', 'Obesidad', 'Se inicia dieta especializada', 15, 15);

-- Insertar datos en la tabla Cirugia
INSERT INTO Cirugia (Fecha, Tipo, Descripcion, ID_Mascota, ID_Veterinario) VALUES 
('2024-07-01', 'Extirpación', 'Extirpación de tumor', 1, 1),
('2024-07-02', 'Limpieza dental', 'Limpieza profunda', 2, 2),
('2024-07-03', 'Reparación ósea', 'Reparación de fractura', 3, 3),
('2024-07-04', 'Cataratas', 'Cirugía de cataratas', 4, 4),
('2024-07-05', 'Biopsia', 'Biopsia de tejido', 5, 5),
('2024-07-06', 'Ligamento cruzado', 'Reparación de ligamento', 6, 6),
('2024-07-07', 'Estómago', 'Cirugía gástrica', 7, 7),
('2024-07-08', 'Hernia', 'Reparación de hernia', 8, 8),
('2024-07-09', 'Amputación', 'Amputación de pata', 9, 9),
('2024-07-10', 'Cálculos renales', 'Extracción de cálculos', 10, 10),
('2024-07-11', 'Esterilización', 'Esterilización', 11, 11),
('2024-07-12', 'Remoción de masa', 'Remoción de masa', 12, 12),
('2024-07-13', 'Prótesis', 'Implante de prótesis', 13, 13),
('2024-07-14', 'Transplante', 'Transplante de órgano', 14, 14),
('2024-07-15', 'Reconstrucción', 'Reconstrucción facial', 15, 15);

-- Insertar datos en la tabla Hospitalizacion
INSERT INTO Hospitalizacion (FechaIngreso, FechaAlta, Motivo, ID_Mascota, ID_Veterinario) VALUES 
('2024-07-01', '2024-07-05', 'Infección grave', 1, 1),
('2024-07-02', '2024-07-06', 'Dermatitis severa', 2, 2),
('2024-07-03', '2024-07-07', 'Problema cardíaco', 3, 3),
('2024-07-04', '2024-07-08', 'Conjuntivitis severa', 4, 4),
('2024-07-05', '2024-07-09', 'Epilepsia grave', 5, 5),
('2024-07-06', '2024-07-10', 'Artritis severa', 6, 6),
('2024-07-07', '2024-07-11', 'Hipotiroidismo grave', 7, 7),
('2024-07-08', '2024-07-12', 'Gastritis severa', 8, 8),
('2024-07-09', '2024-07-13', 'Tumor maligno', 9, 9),
('2024-07-10', '2024-07-14', 'Insuficiencia renal', 10, 10),
('2024-07-11', '2024-07-15', 'Infección urinaria grave', 11, 11),
('2024-07-12', '2024-07-16', 'Problemas dentales graves', 12, 12),
('2024-07-13', '2024-07-17', 'Fractura compleja', 13, 13),
('2024-07-14', '2024-07-18', 'Cirugía mayor', 14, 14),
('2024-07-15', '2024-07-19', 'Obesidad severa', 15, 15);

