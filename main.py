import fastapi
import sqlite3
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Crea la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()

# Configura el middleware CORS para permitir solicitudes desde el origen especificado
origins = ["http://localhost:8080"]  # Reemplaza esto con el origen de tu aplicación web

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contacto(BaseModel):
    email: str
    nombre: str
    telefono: str

# Rutas para las operaciones CRUD

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    c = conn.cursor()
    c.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
              (contacto.email, contacto.nombre, contacto.telefono))
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    c = conn.cursor()
    c.execute('SELECT * FROM contactos;')
    response = []
    for row in c:
        contacto = {"email": row[0], "nombre": row[1], "telefono": row[2]}
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    c = conn.cursor()
    c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in c:
        contacto = {"email": row[0], "nombre": row[1], "telefono": row[2]}
    return contacto

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    c = conn.cursor()
    c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombre, contacto.telefono, email))
    conn.commit()
    return contacto

@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    c = conn.cursor()
    c.execute('DELETE FROM contactos WHERE email = ?', (email,))
    conn.commit()
    return {"mensaje": "Contacto eliminado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
