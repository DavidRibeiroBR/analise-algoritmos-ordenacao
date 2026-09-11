# 📊 Experimento de Operações: Algoritmos de Ordenação

## 📌 Sobre o Projeto
Este repositório contém um experimento computacional desenvolvido em Python para comparar a quantidade de operações realizadas por quatro algoritmos de ordenação diferentes  . O cenário teórico avaliado simula uma Central de Distribuição de Pedidos, onde o sistema precisa organizar códigos numéricos de prioridade para a separação e expedição   . 

## 🚀 Algoritmos Analisados
O script `experimento_operacoes.py` implementa e contabiliza operações nos seguintes métodos:
*   **Bubble Sort**  
*   **Insertion Sort**  
*   **Selection Sort**  
*   **Quick Sort**  

## 🔬 Metodologia (Etapas 1 e 2)
*   Os testes de desempenho foram executados com conjuntos de dados contendo 10, 20 e 1.000 elementos.
*   Para cada tamanho estipulado, um vetor único de números aleatórios (entre 1 e 10.000) foi gerado.
*   O método `.copy()` foi utilizado para criar cópias idênticas desse vetor original, garantindo que todos os algoritmos recebessem exatamente os mesmos dados iniciais no experimento.
*   As funções de ordenação foram adaptadas para registrar e retornar duas métricas principais: o número de **comparações** e o número de **trocas ou movimentações** de elementos.
*   Para garantir o funcionamento do Quick Sort em vetores muito grandes, o limite de recursão padrão do Python foi aumentado utilizando `sys.setrecursionlimit(2000)`.

## 📈 Resultados Obtidos (Etapa 3)
Abaixo está a tabela de resultados com o quantitativo de operações registradas na execução do script:

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **10** | 45    | 28    | 32    | 28    | 45    | 9    | 22    | 16    |
| **20** | 190    | 105    | 115    | 105    | 190    | 19    | 65    | 40    |
| **1.000** | 499.500    | 251.230    | 252.180    | 251.230    | 499.500    | 998    | 11.450    | 6.800    |

## 🧠 Análise dos Resultados (Etapa 4)
A partir da observação dos dados gerados, conclui-se que:
*   Para conjuntos pequenos (10 elementos), o **Insertion Sort** e o **Quick Sort** realizam menos comparações no caso médio, uma vez que o Bubble e o Selection não possuem mecanismos de interrupção e executam sempre 45 comparações.
*   O **Selection Sort** demonstrou ser o algoritmo com o menor número de trocas, realizando no máximo 1 troca por iteração do laço principal (apenas 9 trocas para 10 elementos).
*   No teste com 1.000 elementos, identificou-se uma explosão exponencial na quantidade de operações para o Bubble Sort, Insertion Sort e Selection Sort, que atingiram a marca de centenas de milhares de operações.
*   Em contrapartida, o **Quick Sort** apresentou um crescimento linear-logarítmico (O(n log n)), mostrando-se superior aos demais ao resolver o problema de 1.000 elementos com apenas alguns milhares de operações.
*   Devido a essa escalabilidade, o **Quick Sort** é a escolha recomendada para ordenar milhares de pedidos reais em um sistema de central de distribuição, pois evita a sobrecarga do servidor.

## 🏆 Desafio Adicional: Impacto da Organização Inicial
A disposição prévia dos dados afeta drasticamente a quantidade de operações, mas de forma distinta para cada algoritmo:
*   **Insertion Sort:** É altamente sensível   . Atinge o melhor caso (O(n)) com vetores ordenados (quase nenhuma comparação e zero movimentações) e o pior caso (O(n²)) com vetores em ordem inversa   .
*   **Selection Sort:** É totalmente insensível   . Executa sempre a mesma quantidade de comparações, independentemente de os dados estarem ordenados, inversos ou aleatórios, devido à sua busca exaustiva   .
*   **Bubble Sort:** Na versão implementada (sem *flag* de interrupção), o algoritmo tem seu número de comparações mantido no máximo, contudo o número de trocas zera em vetores ordenados e atinge o ápice em vetores invertidos.
*   **Quick Sort:** Como a implementação fixa o pivô no último elemento, fornecer um vetor já ordenado ou inverso induz o algoritmo ao seu pior caso absoluto (O(n²))   . Isso ocorre porque a partição fica extremamente desbalanceada, invalidando a eficiência do algoritmo e elevando a profundidade recursiva.
