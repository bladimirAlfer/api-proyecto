# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_medicos import router as medicos_router
from app_citas_medicas import router as citas_router
from app_pacientes import router as pacientes_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(medicos_router, prefix="/medicos", tags=["Medicos"])
app.include_router(citas_router, prefix="/citas", tags=["Citas"])
app.include_router(pacientes_router, prefix="/pacientes", tags=["Pacientes"])
