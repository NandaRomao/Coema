from fastapi import APIRouter
from ..services.triagem_service import classificar_risco

router = APIRouter()

@router.get("/{paciente_id}")
def obter_triagem(paciente_id: str):
    """
    Endpoint responsável por avaliar os registros recentes do paciente
    e retornar a classificação de risco (Verde, Amarelo, Vermelho).
    """
    # Delega a lógica de negócio para a camada de Service
    status = classificar_risco(paciente_id)
    return {
        "paciente_id": paciente_id,
        "status_triagem": status
    }
