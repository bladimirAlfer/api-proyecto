from fastapi import FastAPI, HTTPException
import mysql.connector
import schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

# Configuración de CORS
origins = [
    "http://52.72.247.76:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Detalles de la base de datos
host_name = "3.219.70.47"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "proyecto"
schema_name = "pacientes_schema"

@app.get("/")
def health_check():
    return {"status": "ok"}

# Definición de rutas para el router
@router.get("/", tags=["Pacientes"])
def get_pacientes():
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"USE {schema_name}")
    cursor.execute("SELECT * FROM pacientes")
    result = cursor.fetchall()
    mydb.close()
    return result

@router.get("/{id}", tags=["Pacientes"])
def get_paciente(id: int):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"USE {schema_name}")
    cursor.execute(f"SELECT * FROM pacientes WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Paciente not found")

@router.post("/", tags=["Pacientes"])
def add_paciente(item: schemas.Paciente):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"USE {schema_name}")
    sql = "INSERT INTO pacientes (name, age) VALUES (%s, %s)"
    val = (item.name, item.age)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Paciente added successfully"}

@router.put("/{id}", tags=["Pacientes"])
def update_paciente(id: int, item: schemas.Paciente):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"USE {schema_name}")
    sql = "UPDATE pacientes SET name=%s, age=%s WHERE id=%s"
    val = (item.name, item.age, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Paciente updated successfully"}

@router.delete("/{id}", tags=["Pacientes"])
def delete_paciente(id: int):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"USE {schema_name}")
    cursor.execute(f"DELETE FROM pacientes WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Paciente deleted successfully"}

# Añadir el router al app
app.include_router(router, prefix="/pacientes")  # Importante incluir el router con el prefijo correcto
