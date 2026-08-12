# Backend — Coema

**Status:** Inicializado. O ambiente Python e a estrutura base do FastAPI foram configurados.

## Planejado

- **Python + FastAPI** — ecossistema maduro para interoperabilidade em saúde (HL7 FHIR), relevante para uma futura conversa com a RNDS (Rede Nacional de Dados em Saúde)
- **PostgreSQL** como banco de dados — relacional, maduro em extensões de segurança/criptografia
- **OAuth2 + MFA** (pelo menos no lado médico)
- Modelagem de dados pensada desde já para compatibilidade futura com **FHIR**

## Pontos de atenção obrigatórios (não negociáveis)

- **LGPD**: dado de saúde é categoria especial — consentimento explícito, minimização de dados, criptografia em repouso e em trânsito, log de acesso, direito de exclusão do paciente
- **Regras de triagem auditáveis**: nada de modelo preditivo opaco no Nível 1 — apenas regras claras e explicáveis (se X e Y, então alerta amarelo), validadas com respaldo clínico (ex. adaptação de índices como o SLEDAI)
- **Disclaimers de responsabilidade**: o sistema é uma ferramenta de apoio/triagem, não diagnóstico — isso precisa estar refletido também na API e nas respostas ao usuário

## Endpoints previstos (Nível 1) — rascunho

- `POST /registros` — paciente registra sintoma/medicação/exame
- `GET /historico/{paciente_id}` — histórico completo do paciente (PHR)
- `GET /triagem/{paciente_id}` — status atual (verde/amarelo/vermelho)
- `POST /alertas` — disparo de alerta ao médico de referência (nível vermelho)
