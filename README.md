# Coema

# Coema

> *amanhecer, já é dia* — tupi

Sistema de acompanhamento contínuo para pacientes crônicos autoimunes, usando o Lúpus Eritematoso Sistêmico (LES) como caso-âncora. O objetivo de longo prazo é servir a rede pública de saúde (SUS), mas o projeto ainda não tem vínculo oficial com ela.

Projeto submetido ao **Way HUB / Ânima Hub** (Edital Regular 2026/2).

**Status atual:** fase de planejamento e desenho conceitual — em busca de colegas para compor o time antes do início da construção. Ainda não há código em produção; este repositório documenta a ideia, a arquitetura planejada e serve de ponto de partida para quem quiser embarcar no projeto.

---

## O problema

Pacientes com doenças autoimunes crônicas vivem entre consultas longas e espaçadas, com pouquíssimo suporte no intervalo entre elas:

- Fadiga cognitiva (comum em quadros autoimunes) prejudica a adesão ao tratamento.
- Profissionais na ponta do atendimento (UBS, pronto-socorro) muitas vezes não têm contexto clínico suficiente para entender apresentações complexas de doenças autoimunes.
- Alta rotatividade de profissionais na rede pública fragmenta o histórico clínico do paciente.
- Sem sinalização precoce, agravamentos evitáveis viram idas desnecessárias (ou tardias demais) ao serviço de saúde.

## A solução

Um sistema de dois lados:

- **Paciente:** registro diário de sintomas, medicação e exames, com lembretes escalonados (1 mês → 15 dias → 1 semana → 3 dias → 2 dias → véspera → horas antes).
- **Médico:** triagem por exceção — só é acionado quando há desvio relevante, nunca contatado diretamente pelo paciente.

| Nível | Significado | Ação |
|---|---|---|
| 🟢 Verde | Dentro do esperado | Autogestão do paciente |
| 🟡 Amarelo | Atenção | Sistema orienta o paciente a buscar atendimento, com resumo de contexto clínico |
| 🔴 Vermelho | Desvio relevante | Alerta ao médico de referência |

Documentação completa em [`docs/BRIEFING.md`](docs/BRIEFING.md).

## Princípios norteadores

- Paciente como agente, não como objeto de cuidado.
- Comunicação assimétrica intencional (protege tempo profissional e estabilidade emocional do paciente).
- Paciente como custodiante do próprio histórico clínico (modelo PHR).

## Stack planejada

| Camada | Tecnologia | Motivo |
|---|---|---|
| Frontend (paciente) | PWA — React | Funciona offline, sem loja de app, roda em celular mais fraco |
| Backend | Python — FastAPI | Ecossistema maduro para interoperabilidade em saúde (HL7 FHIR) |
| Banco de dados | PostgreSQL | Relacional, maduro em extensões de segurança/criptografia |
| Autenticação | OAuth2 + MFA (lado médico) | Segurança reforçada para dado sensível |

Ver [`frontend/README.md`](frontend/README.md) e [`backend/README.md`](backend/README.md) para o planejamento de cada parte.

## Roadmap

Ver [`ROADMAP.md`](ROADMAP.md).

## Como contribuir

O projeto está formando time agora. Procuramos:

- Alguém com proximidade da área clínica (medicina/enfermagem), para validar critérios de triagem com um profissional
- Dev backend com atenção a segurança e dado sensível
- Alguém com sensibilidade a acessibilidade e UX para o público real do SUS

Se tiver interesse, abra uma *issue* neste repositório ou entre em contato diretamente com a proponente.

## Cronograma no Way HUB

- Resultado da seleção: até 4 de agosto de 2026
- Sprint 1 (Product Canvas + Matriz Estratégica): até 21 de outubro
- Sprint 2 (pré-projeto, pitch gravado, dados de coparticipante, MVP opcional): até 18 de novembro

## Contato

**Proponente:** Fernanda Romão — UNA (Ânima Educação - Way Hub)