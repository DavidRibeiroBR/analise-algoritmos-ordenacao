# 📊 Experimento de Operações: Algoritmos de Ordenação

## 📌 Sobre o Projeto
Este repositório contém um experimento computacional desenvolvido em Python para comparar a quantidade de operações realizadas por quatro algoritmos de ordenação diferentes[cite: 2, 3]. O cenário teórico avaliado simula uma Central de Distribuição de Pedidos, onde o sistema precisa organizar códigos numéricos de prioridade para a separação e expedição[cite: 2]. 

## 🚀 Algoritmos Analisados
O script `experimento_operacoes.py` implementa e contabiliza operações nos seguintes métodos:
*   **Bubble Sort**[cite: 2, 3]
*   **Insertion Sort**[cite: 2, 3]
*   **Selection Sort**[cite: 2, 3]
*   **Quick Sort**[cite: 2, 3]

## 🔬 Metodologia (Etapas 1 e 2)
*   Os testes de desempenho foram executados com conjuntos de dados contendo 10, 20 e 1.000 elementos[cite: 2, 3].
*   Para cada tamanho estipulado, um vetor único de números aleatórios (entre 1 e 10.000) foi gerado[cite: 2, 3].
*   O método `.copy()` foi utilizado para criar cópias idênticas desse vetor original, garantindo que todos os algoritmos recebessem exatamente os mesmos dados iniciais no experimento[cite: 2, 3].
*   As funções de ordenação foram adaptadas para registrar e retornar duas métricas principais: o número de **comparações** e o número de **trocas ou movimentações** de elementos[cite: 2, 3].
*   Para garantir o funcionamento do Quick Sort em vetores muito grandes, o limite de recursão padrão do Python foi aumentado utilizando `sys.setrecursionlimit(2000)`[cite: 2, 3].

## 📈 Resultados Obtidos (Etapa 3)
Abaixo está a tabela de resultados com o quantitativo de operações registradas na execução do script[cite: 2]:

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **10** | 45[cite: 2] | 28[cite: 2] | 32[cite: 2] | 28[cite: 2] | 45[cite: 2] | 9[cite: 2] | 22[cite: 2] | 16[cite: 2] |
| **20** | 190[cite: 2] | 105[cite: 2] | 115[cite: 2] | 105[cite: 2] | 190[cite: 2] | 19[cite: 2] | 65[cite: 2] | 40[cite: 2] |
| **1.000** | 499.500[cite: 2] | 251.230[cite: 2] | 252.180[cite: 2] | 251.230[cite: 2] | 499.500[cite: 2] | 998[cite: 2] | 11.450[cite: 2] | 6.800[cite: 2] |

## 🧠 Análise dos Resultados (Etapa 4)
A partir da observação dos dados gerados, conclui-se que:
*   Para conjuntos pequenos (10 elementos), o **Insertion Sort** e o **Quick Sort** realizam menos comparações no caso médio, uma vez que o Bubble e o Selection não possuem mecanismos de interrupção e executam sempre 45 comparações[cite: 2].
*   O **Selection Sort** demonstrou ser o algoritmo com o menor número de trocas, realizando no máximo 1 troca por iteração do laço principal (apenas 9 trocas para 10 elementos)[cite: 2].
*   No teste com 1.000 elementos, identificou-se uma explosão exponencial na quantidade de operações para o Bubble Sort, Insertion Sort e Selection Sort, que atingiram a marca de centenas de milhares de operações[cite: 2].
*   Em contrapartida, o **Quick Sort** apresentou um crescimento linear-logarítmico ($O(n \log n)$), mostrando-se brutalmente superior aos demais ao resolver o problema de 1.000 elementos com apenas alguns milhares de operações[cite: 2].
*   Devido a essa escalabilidade, o **Quick Sort** é a escolha recomendada para ordenar milhares de pedidos reais em um sistema de central de distribuição, pois evita a sobrecarga do servidor[cite: 2].

## 🏆 Desafio Adicional: Impacto da Organização Inicial
A disposição prévia dos dados afeta drasticamente a quantidade de operações, mas de forma distinta para cada algoritmo[cite: 2]:
*   **Insertion Sort:** É altamente sensível[cite: 2]. Atinge o melhor caso ($O(n)$) com vetores ordenados (quase nenhuma comparação e zero movimentações) e o pior caso ($O(n^2)$) com vetores em ordem inversa[cite: 2].
*   **Selection Sort:** É totalmente insensível[cite: 2]. Executa sempre a mesma quantidade de comparações, independentemente de os dados estarem ordenados, inversos ou aleatórios, devido à sua busca exaustiva[cite: 2].
*   **Bubble Sort:** Na versão implementada (sem *flag* de interrupção), o algoritmo tem seu número de comparações mantido no máximo, contudo o número de trocas zera em vetores ordenados e atinge o ápice em vetores invertidos[cite: 2].
*   **Quick Sort:** Como a implementação fixa o pivô no último elemento, fornecer um vetor já ordenado ou inverso induz o algoritmo ao seu pior caso absoluto ($O(n^2)$)[cite: 2]. Isso ocorre porque a partição fica extremamente desbalanceada, invalidando a eficiência do algoritmo e elevando a profundidade recursiva[cite: 2].

## 💻 Como Executar o Experimento
1.  Certifique-se de ter o interpretador Python instalado[cite: 3].
2.  Faça o download ou clone este repositório contendo o arquivo `experimento_operacoes.py`[cite: 3].
3.  Execute o script no terminal ou em sua IDE favorita:
    ```bash
    python experimento_operacoes.py
    ```
