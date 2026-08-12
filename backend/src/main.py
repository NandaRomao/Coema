from fastapi import FastAPI
from .controllers import triagem_controller

app = FastAPI(
    title="Coema API",
    description="API do sistema de acompanhamento contínuo para pacientes crônicos autoimunes no SUS.",
    version="0.1.0"
)

# Incluindo as rotas (Controllers)
app.include_router(triagem_controller.router, prefix="/triagem", tags=["Triagem"])

@app.get("/")
def root():
    return {"message": "Coema API - Status: Online"}
