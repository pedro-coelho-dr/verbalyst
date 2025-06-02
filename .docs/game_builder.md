# Verbalyst Game Builder

Este documento descreve o funcionamento da funcionalidade **game_builder** do projeto Verbalyst, responsável por gerar os arquivos de jogos a partir do modelo semântico treinado. O processo constrói, para cada palavra-alvo, um conjunto de dicas e dados auxiliares que serão utilizados no backend do jogo.

## Etapas do Game Builder

1. **Carregamento do Modelo**
   - Entrada: modelo Word2Vec treinado (`models/verbalyst_v1.kv`)
   - O modelo é carregado em memória para cálculo de similaridades e projeções.

2. **Carregamento do Vocabulário e Alvos**
   - Entrada: lista de palavras-alvo (`targets.txt`)
   - O vocabulário é extraído do próprio modelo.
   - As palavras-alvo são lidas do arquivo de texto.

3. **Construção de Jogos**
   - Para cada palavra-alvo:
     - **Cálculo de Distâncias:**  
       Calcula a similaridade entre a palavra-alvo e todas as palavras do vocabulário, ordenando por proximidade semântica.
     - **Seleção de Dicas:**  
       Seleciona dicas (hints) entre as palavras mais próximas, dividindo em faixas e sorteando uma de cada faixa para garantir diversidade.
     - **Cálculo de Coordenadas:**  
       Projeta a palavra-alvo e as dicas em duas dimensões usando PCA, normalizando as distâncias para visualização e uso no frontend/backend.
     - **Montagem dos Dados:**  
       Organiza os dados das dicas e de todas as palavras candidatas, incluindo palavra, distância, e coordenadas.

4. **Exportação dos Jogos**
   - Cada jogo é salvo como um arquivo `.json` numerado sequencialmente na pasta de saída (`data/`).
   - O vocabulário utilizado também é salvo em arquivos separados para referência.

## Organização de Arquivos

- `main.py`: script principal que executa todo o processo de geração dos jogos.
- `config.py`: define caminhos do modelo, arquivos de entrada e parâmetros.
- `src/target.py`: carrega as palavras-alvo.
- `src/hint.py`: seleciona as dicas para cada jogo.
- `src/distance.py`: calcula as distâncias semânticas entre palavras.
- `src/coordinates.py`: projeta as palavras em 2D para visualização.
- `src/export.py`: salva os jogos e vocabulários em arquivos.
- `src/__init__.py`: facilita a importação das funções principais.


## Resultado

- Arquivos de jogos em formato `.json` na pasta `data/`, cada um contendo:
  - Palavra-alvo
  - Lista de dicas (hints) com distâncias e coordenadas
  - Lista de todas as palavras candidatas com distâncias e coordenadas
- Arquivos de vocabulário utilizados em cada execução

## Observações

- O processo garante que apenas palavras presentes no modelo são utilizadas.
- As dicas são selecionadas para cobrir diferentes níveis de proximidade semântica.
- As coordenadas são normalizadas para facilitar a visualização e uso no frontend.
