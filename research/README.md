
## Introdução

### O que é Word Embeddings?


### Por que usar WordEmbeddings?


### escolha: http://www.nilc.icmc.usp.br/embeddings

NILC - Núcleo Interinstitucional de Linguística Computacional

NILC-Embeddings é um repositório destinado ao armazenamento e compartilhamento de vetores de palavras (do inglês, word embeddings) gerados para a Língua Portuguesa.

O treinamento dos vetores ocorreu em algoritmos como Word2vec [1], FastText [2], Wang2vec [3] e Glove [4]. Mais detalhes sobre o projeto podem ser encontrados em: 




### teste: FastText SKIP-GRAM 300 dimensões

justificativa: O modelo FastText é um dos mais populares para a tarefa de word embedding, e o modelo Skip-Gram é conhecido por capturar relações semânticas entre palavras. A escolha de 300 dimensões é um bom compromisso entre desempenho e eficiência computacional.

resultado:
- tempo de carregamento: médio  
- impressões:  

```bash
Palavra: carro
Similaridade com 'felicidade': 0.2985

Top 5 mais próximas de 'felicidade':
  velicidade: 0.8136
  alegria: 0.7776
  infelicidade: 0.7707
  helicidade: 0.7474
  flicidade: 0.7278

Top 5 mais distantes de 'felicidade':
  00/iv: -0.1556
  00/ix: -0.1419
  0/ix: -0.1394
  ttm: -0.1348
  lpg: -0.1278
```
        

### teste: SKIP-GRAM 100 dimensões

justificativa:  
O modelo Skip-Gram é conhecido por capturar relações semânticas entre palavras. A escolha de 100 dimensões é um bom compromisso entre desempenho e eficiência computacional, especialmente para tarefas que não exigem uma representação tão rica quanto a de 300 dimensões.

resultado:
- tempo de carregamento: rápido  
- impressões:  

```bash
Palavra: carro
Similaridade com 'felicidade': 0.0081

Top 5 mais próximas de 'felicidade':
  alegria: 0.7991
  bondade: 0.7793
  vaidade: 0.7710
  alma: 0.7568
  tranqüilidade: 0.7555

Top 5 mais distantes de 'felicidade':
  foifixado: -0.3984
  construçio: -0.3735
  ex-usaf: -0.3726
  aftigo: -0.3633
  no.s: -0.3613
```