# Verbalyst NLP Model Filtering Pipeline

Este script organiza a criação de um modelo Word2Vec filtrado e limpo para uso no back-end do projeto Verbalyst. A pipeline aplica diversos filtros para garantir um vocabulário compacto, frequente, padronizado e representado no modelo semântico.

## Etapas do Pipeline

1. **Extração de palavras frequentes**
   - Entrada: arquivo de frequência (`lemas.totalbr.freq.txt`)
   - Saída: top 10.000 palavras com no mínimo 2 letras
   - Formato: apenas palavras (1 por linha), extraídas a partir do campo de lemas

2. **Filtragem cruzada com dicionário léxico**
   - Entrada: dicionário léxico (`br-utf8.txt`)
   - Mantém apenas palavras que também existam no dicionário léxico

3. **Normalização**
   - Remoção de acentos, cedilhas e conversão para minúsculas
   - Remove duplicatas após a normalização

4. **Filtragem cruzada com dicionário normalizado**
   - Entrada: `br-sa.txt` (dicionário sem acentos)
   - Mantém apenas palavras encontradas também no dicionário sem acentos

5. **Filtragem do modelo Word2Vec**
   - Carrega modelo `.txt` original (`word2vec_skip_100.txt`)
   - Aplica a mesma normalização nas palavras do modelo
   - Filtra o modelo mantendo apenas as palavras normalizadas restantes
   - Remove duplicatas
   - Saída: modelo final salvo como `.kv` (`word2vec_filtered.kv`)

6. **Log e verificações**
   - Log de todas as etapas é impresso no terminal
   - Arquivo final contém apenas palavras com representação vetorial no modelo

## Resultado Atual

8021 palavras

## Organização de Arquivos

- `main.py`: script principal da pipeline
- `config.py`: caminhos de entrada/saída
- `frequency.py`: manipulação de listas de frequência
- `filters.py`: intersecções e filtros com dicionários
- `normalize.py`: normalização de palavras
- `model_utils.py`: manipulação do modelo Word2Vec
- `io_utils.py`: funções auxiliares de leitura/escrita

## Requisitos

- `gensim`
- `numpy`

## Execução

```bash
python src/main.py
```

## Referências:
- [Lema Frequency](https://www.linguateca.pt/acesso/ordenador.php)
- [Model](http://nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc) 
- [Dicionarios](https://www.ime.usp.br/~pf/dicios/)