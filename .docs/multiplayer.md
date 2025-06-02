# Verbalyst Multiplayer

Este documento descreve a estrutura e funcionamento do modo multiplayer do projeto Verbalyst, detalhando os principais componentes, fluxo de dados e lógica de interação entre jogadores.

## Visão Geral

O modo multiplayer permite que dois ou mais jogadores participem de partidas síncronas, interagindo em tempo real por meio de desafios linguísticos. O sistema gerencia salas, sincronização de estado, pontuação e comunicação entre clientes e servidor.

## Componentes Principais

- **Servidor Multiplayer**  
  Responsável por gerenciar as salas, estados das partidas, validação de respostas e sincronização entre os jogadores. Implementado em Python com websockets.

- **Cliente Multiplayer**  
  Interface do usuário que conecta ao servidor, exibe o estado da partida, envia respostas e recebe atualizações em tempo real.

- **Gerenciador de Salas**  
  Permite criar, listar, entrar e sair de salas. Cada sala possui um identificador único e mantém o estado dos jogadores conectados.

- **Sincronização de Estado**  
  O servidor mantém o estado da partida (rodada atual, pontuação, respostas) e envia atualizações para todos os clientes conectados à sala.

## Fluxo de Funcionamento

1. **Criação/Entrada em Sala**
   - O jogador pode criar uma nova sala ou entrar em uma existente usando um código.
   - O servidor registra o jogador e atualiza a lista de participantes.

2. **Início da Partida**
   - Quando todos os jogadores estão prontos, a partida é iniciada.
   - O servidor envia o desafio da rodada para a partida onde estão todos os jogadores.

3. **Envio de Respostas**
   - Cada jogador envia sua resposta ao servidor.
   - O servidor valida as respostas e atualiza a pontuação.

4. **Atualização de Estado**
   - O servidor envia o resultado da rodada e o placar atualizado para todos os jogadores.
   - O ciclo se repete até o fim da partida.

5. **Finalização**
   - O servidor determina o vencedor e envia o resultado final.
   - Os jogadores podem optar por jogar novamente ou sair da sala.

## Observações

O multiplayer ainda não foi implementado totalmente mas a estrutura do banco de dados já está de acordo com a planejada.