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
citas_schema = "citas_schema"
medicos_schema = "medicos_schema"
pacientes_schema = "pacientes_schema"

@app.get("/")
def health_check():
    return {"status": "ok"}

# Definición de rutas para el router
@router.get("/", tags=["Citas"])
def get_citas():
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Uso de esquemas correctos
    cursor.execute(f"USE {citas_schema}")
    sql = f"""
    SELECT c.id, c.date, m.name as medico_name, p.name as paciente_name 
    FROM {citas_schema}.citas c
    JOIN {medicos_schema}.medicos m ON c.medico_id = m.id
    JOIN {pacientes_schema}.pacientes p ON c.paciente_id = p.id
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    mydb.close()
    return [{"id": row[0], "date": row[1], "medico_name": row[2], "paciente_name": row[3]} for row in result]

@router.get("/{id}", tags=["Citas"])
def get_cita(id: int):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Uso de esquemas correctos
    cursor.execute(f"USE {citas_schema}")
    sql = f"""
    SELECT c.id, c.date, c.medico_id, c.paciente_id, m.name as medico_name, p.name as paciente_name
    FROM {citas_schema}.citas c
    JOIN {medicos_schema}.medicos m ON c.medico_id = m.id
    JOIN {pacientes_schema}.pacientes p ON c.paciente_id = p.id
    WHERE c.id = %s
    """
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    mydb.close()
    if result:
        return {"id": result[0], "date": result[1], "medico_id": result[2], "paciente_id": result[3], "medico_name": result[4], "paciente_name": result[5]}
    raise HTTPException(status_code=404, detail="Cita not found")

@router.post("/", tags=["Citas"])
def add_cita(item: schemas.Cita):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Uso de esquemas correctos
    cursor.execute(f"USE {citas_schema}")
    sql = "INSERT INTO citas (medico_id, paciente_id, date) VALUES (%s, %s, %s)"
    val = (item.medico_id, item.paciente_id, item.date)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Cita added successfully"}

@router.put("/{id}", tags=["Citas"])
def update_cita(id: int, item: schemas.Cita):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Uso de esquemas correctos
    cursor.execute(f"USE {citas_schema}")
    sql = "UPDATE citas SET medico_id=%s, paciente_id=%s, date=%s WHERE id=%s"
    val = (item.medico_id, item.paciente_id, item.date, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Cita updated successfully"}

@router.delete("/{id}", tags=["Citas"])
def delete_cita(id: int):
    mydb = mysql.connector.connect(
        host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Uso de esquemas correctos
    cursor.execute(f"USE {citas_schema}")
    cursor.execute(f"DELETE FROM citas WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Cita deleted successfully"}

# Añadir el router al app
app.include_router(router, prefix="/citas")  # Importante incluir el router con el prefijo correcto
