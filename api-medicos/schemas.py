from pydantic import BaseModel

class Medico(BaseModel):
    name: str
    specialty: str

class Paciente(BaseModel):
    name: str
    age: int

class Cita(BaseModel):
    medico_id: int
    paciente_id: int
    date: str


