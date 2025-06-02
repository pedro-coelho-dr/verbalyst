# Verbalyst API

Este documento descreve o funcionamento da API do projeto Verbalyst, detalhando os principais endpoints, fluxo de dados e organização dos arquivos responsáveis pelo backend.

## Visão Geral

A API do Verbalyst é responsável por fornecer os dados necessários para o funcionamento do jogo, incluindo a seleção do desafio diário, fornecimento de dicas (hints) e validação das tentativas dos jogadores (guesses). A API é implementada utilizando FastAPI e SQLModel, garantindo respostas rápidas e integração eficiente com o banco de dados.

## Endpoints Principais

1. **Obter o Jogo Diário**
   - **Endpoint:** `GET /game`
   - **Descrição:** Retorna o identificador do jogo do dia, selecionado de acordo com a data atual.
   - **Fluxo:** Utiliza a função `get_daily_game_id()` para determinar o jogo correspondente ao dia.

2. **Obter Dica**
   - **Endpoint:** `GET /hint/{hint_number}`
   - **Descrição:** Retorna uma dica específica (hint) para o jogo do dia, baseada na ordem de distância semântica.
   - **Validação:** O número da dica deve estar entre 1 e 10.
   - **Fluxo:** Busca as dicas relacionadas à palavra-alvo do jogo do dia e retorna a dica correspondente ao número solicitado.

3. **Fazer uma Tentativa**
   - **Endpoint:** `GET /guess/{guess}`
   - **Descrição:** Permite ao usuário enviar uma palavra como tentativa de adivinhar a palavra-alvo do jogo do dia.
   - **Validação:** Verifica se a palavra existe no banco de dados e se pertence ao conjunto do jogo.
   - **Fluxo:** Se a tentativa for correta, retorna sucesso; caso contrário, retorna a distância semântica e coordenadas da palavra tentada em relação à palavra-alvo.

## Organização de Arquivos

- `backend/src/api/daily.py`: Define os endpoints da API relacionados ao jogo diário, dicas e tentativas.
- `backend/src/services/daily.py`: Implementa a lógica para seleção do jogo diário.
- `backend/src/schemas/game.py`: Define os modelos de resposta (schemas) para dicas e tentativas.

## Fluxo de Funcionamento

1. O usuário acessa o endpoint `/game` para obter o identificador do jogo do dia.
2. O usuário pode solicitar dicas incrementais usando `/hint/{hint_number}`.
3. O usuário faz tentativas de adivinhar a palavra-alvo usando `/guess/{guess}`.
4. A API valida as entradas, consulta o banco de dados e retorna as informações necessárias para o frontend.


## Observações

- A API está estruturada para facilitar a expansão futura, incluindo modos multiplayer e novos tipos de desafios.
- O banco de dados deve estar populado com jogos, palavras e distâncias para o correto funcionamento dos endpoints.
