-- Crear una tabla de contactos
CREATE TABLE IF NOT EXISTS contactos (
    email TEXT PRIMARY KEY,
    nombre TEXT,
    telefono TEXT
);

-- Insertar algunos datos de ejemplo
INSERT INTO contactos (email, nombre, telefono) VALUES
    ('juan@example.com', 'Juan Pérez', '555-1234'),
    ('maria@example.com', 'María López', '555-5678');
