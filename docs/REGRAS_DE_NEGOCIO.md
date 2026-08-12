# Regras de Negócio — Coema

Este documento centraliza as lógicas, fluxos e restrições clínicas e de produto do sistema Coema. Estas regras devem guiar toda a implementação do código, tanto no Frontend quanto no Backend.

## 1. Assimetria de Comunicação
O fluxo de comunicação é estritamente unidirecional em relação ao início do contato para proteção de ambas as partes:
- **O paciente NUNCA inicia contato direto com o médico** através do sistema (ex: sem chat livre). Isso protege o tempo profissional e evita ansiedade de espera pelo paciente ("estar incomodando" ou frustração por não receber resposta).
- **O médico pode iniciar contato** com o paciente após receber um alerta do sistema.

## 2. Matriz de Triagem por Exceção
O sistema analisa os registros diários do paciente e classifica o risco em três níveis. Não há uso de Inteligência Artificial opaca no Nível 1; todas as regras devem ser claras, baseadas em condicionais ("if/else") auditáveis e aprovadas clinicamente.

| Nível | Risco | Ação do Sistema | Ação Esperada |
|---|---|---|---|
| 🟢 **Verde** | Dentro do esperado | Nenhuma intervenção ativa. | Autogestão do paciente. |
| 🟡 **Amarelo** | Atenção | Sistema dispara mensagem automática orientando o paciente a buscar atendimento (UBS/Pronto-socorro), gerando um resumo clínico da situação para facilitar o triage na ponta. | Paciente procura a rede. |
| 🔴 **Vermelho** | Desvio relevante | Sistema dispara alerta imediato para o médico de referência responsável pelo paciente no sistema. | Médico intervém. |

## 3. Fluxo de Lembretes Escalonados
A janela de alertas para garantir a adesão ao tratamento e evitar o esquecimento (considerando a fadiga cognitiva comum em doenças autoimunes) deve seguir rigorosamente a seguinte régua de tempo antes de um evento crítico (ex: consulta, exame ou renovação de medicação):
1. **1 mês** antes
2. **15 dias** antes
3. **1 semana** antes
4. **3 dias** antes
5. **2 dias** antes
6. **Véspera**
7. **Horas antes** do evento

## 4. Custódia do Histórico Clínico (PHR)
- **Personal Health Record (PHR):** O paciente é o verdadeiro custodiante do próprio histórico. Os dados coletados viajam com ele, independentemente do médico ou unidade de saúde onde for atendido.
- O sistema deve permitir que o paciente conceda ou revogue acesso ao seu histórico para profissionais de saúde específicos, de acordo com as regras da LGPD (minimização de dados, transparência e consentimento).
