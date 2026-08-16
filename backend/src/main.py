from fastapi import FastAPI
from .controllers import triagem_controller, historico_clinico_controller, registro_controller

app = FastAPI(
    title="Coema API",
    description="API do sistema de acompanhamento contínuo para pacientes crônicos autoimunes no SUS.",
    version="0.1.0"
)

# Incluindo as rotas (Controllers)
app.include_router(triagem_controller.router, prefix="/triagem", tags=["Triagem"])

# Incluindo as rotas histórico clínico , registros - Matheus

app.include_router(historico_clinico_controller.router, prefix="/historico-clinico", tags=["Histórico Clínico"])
app.include_router(registro_controller.router, prefix="/registro", tags=["Registro"])


@app.get("/")
def root():
    return {"message": "Coema API - Status: Online"}

