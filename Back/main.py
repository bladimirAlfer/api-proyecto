# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_medicos import router as medicos_router
from app_citas_medicas import router as citas_router
from app_pacientes import router as pacientes_router

app = FastAPI()

origins = [
    "http://52.72.247.76:8000",  # Asegúrate de incluir aquí todos los dominios que utilizarán tu API
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ajusta según tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(medicos_router, prefix="/medicos", tags=["Medicos"])
app.include_router(citas_router, prefix="/citas", tags=["Citas"])
app.include_router(pacientes_router, prefix="/pacientes", tags=["Pacientes"])
