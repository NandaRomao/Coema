def classificar_risco(paciente_id: str) -> str:
    """
    Regra de Negócio: Triagem por Exceção.
    Avalia os dados do paciente e retorna:
    - Verde: Dentro do esperado
    - Amarelo: Atenção (buscar UBS)
    - Vermelho: Desvio relevante (alerta médico)
    """
    # TODO: Conectar com repositório de dados / banco.
    # Por enquanto, retorna um placeholder simulando um paciente estável.
    return "Verde"
