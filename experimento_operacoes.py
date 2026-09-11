import random
import sys

# Aumenta o limite de recursão para evitar erros no Quick Sort com vetores muito grandes
sys.setrecursionlimit(2000)

def bubble_sort(vetor):
    comparacoes = trocas = 0
    tamanho_vetor = len(vetor)
    for i in range(tamanho_vetor):
        # Compara os maiores "flutuam" para o final
        for j in range(0, tamanho_vetor-i-1):
            comparacoes += 1
            if vetor[j] > vetor[j+1]:
                # Troca os elementos de posição se estiverem na ordem errada
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocas += 1
    return comparacoes, trocas

def insertion_sort(vetor):
    comparacoes = movimentacoes = 0
    # Começa do segundo elemento, assumindo que o primeiro já está "ordenado"
    for i in range(1, len(vetor)):
        valor_atual = vetor[i] # valor a ser inserido
        indice_anterior = i - 1
        # Desloca os elementos maiores que a chave para a direita
        while indice_anterior >= 0:
            comparacoes += 1
            if valor_atual < vetor[indice_anterior]:
                vetor[indice_anterior + 1] = vetor[indice_anterior]
                movimentacoes += 1
                indice_anterior -= 1
            else:
                break
        # Insere na posição correta encontrada
        vetor[indice_anterior + 1] = valor_atual
        movimentacoes += 1
    return comparacoes, movimentacoes

def selection_sort(vetor):
    comparacoes = trocas = 0
    tamanho_vetor = len(vetor)
    # Percorre o vetor buscando o menor elemento
    for i in range(tamanho_vetor):
        indice_menor = i
        # Encontra o índice do menor elemento no trecho que não foi ordenado
        for j in range(i+1, tamanho_vetor):
            comparacoes += 1
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j
        # Troca o menor elemento com o elemento da posição atual (i)
        if indice_menor != i:
            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
            trocas += 1
    return comparacoes, trocas

def quick_sort(vetor, indice_inicio, indice_fim):
    # Condição de parada da recursão
    if indice_inicio >= indice_fim:
        return 0, 0
        
    comparacoes = trocas = 0
    pivo = vetor[indice_fim] # Escolhe o último elemento como pivô para a partição
    indice_menores = indice_inicio - 1
    
    # Reorganiza o vetor: menores que o pivô ficam à esquerda, maiores à direita
    for j in range(indice_inicio, indice_fim):
        comparacoes += 1
        if vetor[j] <= pivo:
            indice_menores += 1
            vetor[indice_menores], vetor[j] = vetor[j], vetor[indice_menores]
            trocas += 1
            
    # Coloca o pivô na sua posição definitiva
    vetor[indice_menores + 1], vetor[indice_fim] = vetor[indice_fim], vetor[indice_menores + 1]
    trocas += 1
    indice_pivo = indice_menores + 1 # Índice final do pivô
    
    # Chama a ordenação recursivamente para as metades antes e depois do pivô
    comp_esquerda, trocas_esquerda = quick_sort(vetor, indice_inicio, indice_pivo - 1)
    comp_direita, trocas_direita = quick_sort(vetor, indice_pivo + 1, indice_fim)
    
    # Retorna a soma das operações locais com as operações das chamadas recursivas
    return comparacoes + comp_esquerda + comp_direita, trocas + trocas_esquerda + trocas_direita

def executar_experimento(lista_tamanhos):
    lista_resultados = []
    for tamanho_atual in lista_tamanhos:
        # Gera o vetor aleatório (de 1 a 10.000) uma única vez para este tamanho
        vetor_original = [random.randint(1, 10000) for _ in range(tamanho_atual)]
        
        linha_resultado = [tamanho_atual]
        # O .copy() garante que cada algoritmo ordene exatamente os mesmos dados iniciais (Etapa 1)
        linha_resultado.extend(bubble_sort(vetor_original.copy()))
        linha_resultado.extend(insertion_sort(vetor_original.copy()))
        linha_resultado.extend(selection_sort(vetor_original.copy()))
        linha_resultado.extend(quick_sort(vetor_original.copy(), 0, tamanho_atual - 1))
        
        # Guarda os resultados da execução deste tamanho
        lista_resultados.append(linha_resultado)
    return lista_resultados

# --- EXECUÇÃO DO EXPERIMENTO ---
lista_tamanhos = [10, 20, 1000] # Tamanhos definidos na Etapa 1
lista_resultados = executar_experimento(lista_tamanhos)

# impressão do cabeçalho da tabela
print(f"{'Tamanho':<8} | {'Bub C':<6} | {'Bub T':<6} | {'Ins C':<6} | {'Ins M':<6} | {'Sel C':<6} | {'Sel T':<6} | {'Qui C':<6} | {'Qui M':<6}")
print("-" * 85)

# Impressão linha a linha com os dados gerados
for resultado_atual in lista_resultados:
    print(f"{resultado_atual[0]:<8} | {resultado_atual[1]:<6} | {resultado_atual[2]:<6} | {resultado_atual[3]:<6} | {resultado_atual[4]:<6} | {resultado_atual[5]:<6} | {resultado_atual[6]:<6} | {resultado_atual[7]:<6} | {resultado_atual[8]:<6}")
