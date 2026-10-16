# 912. Sort an Array

**Link:** [LeetCode — Sort an Array](https://leetcode.com/problems/sort-an-array/description/)

**Dificuldade:** Medium

## Contexto do problema

Dado um array de inteiros `nums`, preciso devolvê-lo ordenado de forma crescente, sem usar funções de ordenação prontas.

**Regras:**

- A solução deve rodar em `O(n log n)` de tempo.
- O enunciado pede o menor espaço possível, então o uso de memória pesa na escolha do algoritmo.

## Ideia central

Usar **merge sort**, uma técnica de divisão e conquista: dividir o array ao meio até sobrar um pedaço com 0 ou 1 elemento (que já está ordenado por definição) e depois juntar os pedaços ordenados, dois a dois, até reconstruir o array inteiro.

## Funcionamento

A solução tem duas funções, cada uma com uma responsabilidade:

- **`merge_sort(arr)`:** divide. Se `arr` tem 0 ou 1 elemento, devolve `arr` (caso base). Senão, calcula o `meio`, ordena a metade esquerda e a metade direita recursivamente e entrega as duas ao `merge`.
- **`merge(esq, dir)`:** junta. Recebe duas listas **já ordenadas** e monta uma terceira ordenada.

Na implementação com fatiamento (`arr[:meio]` e `arr[meio:]`), cada divisão cria novas listas. Por isso, embora o merge sort seja eficiente em tempo, ele não é um algoritmo de ordenação *in-place*.

Como o `merge` funciona:

1. Uso dois ponteiros, `i` (na esquerda) e `j` (na direita), ambos começando em 0.
2. Enquanto os dois ponteiros estiverem dentro das listas, comparo `esq[i]` com `dir[j]` e copio o menor para o `resultado`, avançando o ponteiro daquele lado.
3. Quando uma das listas termina, basta anexar os elementos restantes da outra com `extend`. Como ambas já estavam ordenadas e sempre escolhi o menor elemento disponível, todos os elementos copiados antes são menores ou iguais aos que sobraram. Isso também cobre valores repetidos, nos quais pode haver igualdade.

## Por que o caso base é `len(arr) <= 1`

A recursão precisa de um ponto de parada. Um array vazio ou com um único elemento já está ordenado, então não há nada a fazer. Cada chamada olha o tamanho do **pedaço** que recebeu, não o do array original. Sem esse caso base, a função se chamaria para sempre.

## Exemplo passo a passo

`nums = [4, 1, 3, 2]`

**Dividindo:**

- `[4, 1, 3, 2]` → `[4, 1]` e `[3, 2]`
- `[4, 1]` → `[4]` e `[1]`
- `[3, 2]` → `[3]` e `[2]`

**Juntando:**

- `merge([4], [1])`: comparo `4` com `1`, o menor é `1`. Copio `1`, e a direita acaba. Anexo o que sobrou da esquerda: `[1, 4]`.
- `merge([3], [2])`: da mesma forma, resulta em `[2, 3]`.
- `merge([1, 4], [2, 3])`:
  - `1 <= 2`: copio `1` → `[1]`
  - `4 <= 2`? Não, copio `2` → `[1, 2]`
  - `4 <= 3`? Não, copio `3` → `[1, 2, 3]`
  - A direita acabou. Anexo o `4` que sobrou → `[1, 2, 3, 4]`

## Complexidade

- **Tempo:** `O(n log n)`, pois o array é dividido em aproximadamente `log n` níveis e o trabalho total de intercalação em cada nível é `O(n)`.
- **Espaço auxiliar:** `O(n)` para as listas criadas nas divisões e intercalações, além de `O(log n)` na pilha de recursão. O espaço auxiliar total continua sendo `O(n)`.

O merge sort não é in-place nessa implementação. Algoritmos como o heap sort ordenam em `O(n log n)` usando `O(1)` de espaço auxiliar na implementação convencional, o que o torna uma boa alternativa para revisitar este problema.