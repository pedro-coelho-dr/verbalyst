from gensim.models import KeyedVectors

# ========== CONFIGURAÇÃO ==========
path = "../models/word2vec_filtered.kv"  # Altere aqui para outro modelo .kv
palavra_secreta = "felicidade"
arquivo_resultado = "benchmark_word2vec_filtered.txt"

categorias = {
    "emocoes": ["felicidade", "alegria", "tristeza", "raiva", "medo", "odio", "euforia"],
    "transportes": ["carro", "onibus", "aviao", "moto", "bicicleta"],
    "profissoes": ["medico", "professor", "engenheiro", "advogado", "enfermeiro"]
}

# ========== FUNÇÕES ==========

def similaridade_media_categoria(model, palavras):
    total, pares = 0, 0
    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            if palavras[i] in model and palavras[j] in model:
                total += model.similarity(palavras[i], palavras[j])
                pares += 1
    return total / pares if pares > 0 else 0

def testar_analogias(model):
    saida = []
    analogias = [
        (["rei", "mulher"], ["homem"]),
        (["paris", "brasil"], ["franca"]),
        (["professor", "hospital"], ["escola"]),
    ]
    saida.append("Testes de analogia:")
    for pos, neg in analogias:
        try:
            result = model.most_similar(positive=pos, negative=neg, topn=1)
            saida.append(f"{pos[0]} - {neg[0]} + {pos[1]} ≈ {result[0][0]} ({result[0][1]:.4f})")
        except KeyError as e:
            saida.append(f"Palavra fora do vocabulário: {e}")
    saida.append("")
    return "\n".join(saida)

def testar_flexoes(model):
    saida = ["Teste de flexoes:"]
    pares = [
        ("felicidade", "felicidades"),
        ("carro", "carros"),
        ("andar", "andando"),
        ("bom", "boa"),
    ]
    for a, b in pares:
        if a in model and b in model:
            sim = model.similarity(a, b)
            saida.append(f"{a} ↔ {b}: {sim:.4f}")
        else:
            saida.append(f"{a} ou {b} fora do vocabulário")
    saida.append("")
    return "\n".join(saida)

def mostrar_extremos(model, palavra, n=5):
    saida = []
    if palavra not in model:
        return f"'{palavra}' fora do vocabulário\n"

    saida.append(f"Top {n} mais próximas de '{palavra}':")
    for similar, score in model.most_similar(palavra, topn=n):
        saida.append(f"{similar}: {score:.4f}")

    distantes = sorted(
        model.key_to_index.keys(),
        key=lambda w: model.similarity(w, palavra) if w != palavra else 1.0
    )[:n]
    saida.append(f"\nTop {n} mais distantes de '{palavra}':")
    for w in distantes:
        score = model.similarity(w, palavra)
        saida.append(f"{w}: {score:.4f}")
    saida.append("")
    return "\n".join(saida)

# ========== EXECUÇÃO ==========

print(f"Carregando modelo: {path}")
model = KeyedVectors.load(path, mmap='r')  # <-- carrega .kv corretamente
print("Modelo carregado com sucesso.\n")

resultados = []

# Top N mais próximas e distantes
resultados.append(mostrar_extremos(model, palavra_secreta))

# Similaridade entre categorias
for nome, palavras in categorias.items():
    score = similaridade_media_categoria(model, palavras)
    resultados.append(f"Similaridade media ({nome}): {score:.4f}")
resultados.append("")

# Flexões
resultados.append(testar_flexoes(model))

# Analogias
resultados.append(testar_analogias(model))

# Salvando tudo
with open(arquivo_resultado, "w", encoding="utf-8") as f:
    f.write("\n".join(resultados))

print(f"Benchmarks salvos em '{arquivo_resultado}'\n")

# ========== JOGO ==========

print("Adivinhe a palavra secreta.")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Palavra: ").strip().lower()

    if entrada == "sair":
        print(f"A palavra secreta era: {palavra_secreta}")
        break

    if entrada not in model:
        print("Palavra fora do vocabulário.\n")
        continue

    if entrada == palavra_secreta:
        print("Acertou!")
        break

    score = model.similarity(entrada, palavra_secreta)
    print(f"Similaridade com '{palavra_secreta}': {score:.4f}\n")
