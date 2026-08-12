# UX — Diretrizes de Experiência do Usuário

**Autora:** Fernanda Romão
**Status:** documento vivo — será expandido conforme o projeto avança

Este documento reúne os princípios de experiência de usuário definidos para o Coema, com foco especial em acessibilidade — decisão que parte da natureza do público-alvo: pacientes com Lúpus Eritematoso Sistêmico (que pode afetar a visão), potencialmente idosos, e com o objetivo de longo prazo de atender usuários do SUS, incluindo pessoas com baixa alfabetização digital.

---

## 1. Princípios de acessibilidade

- **Codificação redundante:** nenhuma informação importante deve depender de um único canal. Ícone + palavra sempre juntos — nunca só um ou só o outro. Isso garante que a informação chegue independente de limitação de leitura, de visão ou de familiaridade com símbolos.
- **Legibilidade:** fontes grandes, alto contraste entre texto e fundo, linguagem simples e direta — sem jargão médico ou técnico do lado do paciente.
- **Independência de cor:** nenhuma informação crítica pode ser comunicada *apenas* pela cor. Ver seção 2.
- **Referência técnica:** as diretrizes internacionais de acessibilidade (WCAG) servem de base geral para validação futura da interface.

---

## 2. O problema do semáforo (e a solução)

O sistema de triagem do Coema usa três níveis — verde, amarelo, vermelho — para indicar o status do paciente. O risco: as formas mais comuns de daltonismo (deuteranopia/protanopia, que afetam cerca de 8% dos homens) dificultam justamente a distinção entre vermelho e verde — as duas cores mais críticas do sistema.

**Solução — codificação redundante aplicada à triagem:**

| Nível | Cor | Ícone/forma | Texto |
|---|---|---|---|
| Autogestão | Verde | ✓ (check) | "Verde" / "Tudo certo" |
| Atenção | Amarelo | ⚠ (triângulo de atenção) | "Amarelo" / "Atenção" |
| Alerta médico | Vermelho | ⛔ / ✕ | "Vermelho" / "Alerta" |

Nunca exibir o status apenas como uma bolinha colorida — sempre cor + ícone + palavra, juntos.

---

## 3. Navegação

A navegação é diferenciada por perfil de usuário e por dispositivo esperado.

### Lado paciente (PWA, majoritariamente celular)

- **Sem hambúrguer como navegação principal.** Em tela de toque não existe hover — o dedo toca direto, não paira sobre o ícone antes. Além disso, o ícone de hambúrguer tem taxa de descoberta baixa para usuários com pouca familiaridade digital: ele esconde as opções atrás de um símbolo que nem todo mundo reconhece como "menu".
- **Barra de navegação fixa**, sempre visível na parte inferior da tela, com 3–4 ícones + texto (ex.: "Registrar", "Histórico", "Meu status", "Ajuda"). Nada fica escondido atrás de um clique extra.

### Lado médico (provavelmente desktop, mais opções)

- Usuário já está em contexto mais "profissional" e tolera mais complexidade de interface.
- **Menu hambúrguer com submenu é aceitável aqui**, caso a quantidade de opções justifique (navegação extensa) — mas **sempre acionado por clique/toque, nunca por hover.** Hover exige precisão motora fina para manter o cursor parado sobre o ícone, o que prejudica qualquer usuário com mão menos firme — e simplesmente não existe em touch.

---

## 4. Próximos passos

- [ ] Personas (paciente típico, médico de referência)
- [ ] Fluxo de usuário: registro diário → triagem → resposta (verde/amarelo/vermelho)
- [ ] Wireframes de baixa fidelidade aplicando a paleta de cores já definida (ver `BRIEFING.md`)
- [ ] Checklist de contraste de cores (validar a paleta de marca contra a paleta semântica de alerta)