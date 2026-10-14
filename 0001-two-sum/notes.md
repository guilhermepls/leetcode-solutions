# 1. Two Sum

**Link:** [LeetCode — Two Sum](https://leetcode.com/problems/two-sum/description/)

**Dificuldade:** Easy

## Contexto do problema

Dado um array de inteiros `nums` e um inteiro `target`, preciso retornar os índices de dois elementos em posições diferentes cuja soma seja igual a `target`.

**Regras:**

- Cada entrada tem exatamente uma solução.
- Não posso usar o mesmo elemento duas vezes, e os índices podem ser retornados em qualquer ordem.

## Ideia central

Percorrer o array uma única vez usando um hash map (dicionário) para verificar se o complemento do número atual já foi encontrado.

O complemento é o valor que falta para atingir o `target`:

`complemento = target - nums[i]`

## Funcionamento do hash map

- **Chave:** número encontrado anteriormente no array.
- **Valor:** índice desse número no array.

Assim, para cada elemento, calculo seu complemento e verifico se ele já está no dicionário. Se estiver, encontrei os dois números e posso retornar seus índices.

As operações de busca e inserção no hash map têm custo médio de `O(1)`. Esse custo é médio, e não garantido em todos os casos.

## Por que verificar antes de inserir?

Para cada índice `i`, sigo esta ordem:

1. Calculo o complemento: `target - nums[i]`.
2. Verifico se o complemento já existe no dicionário.
3. Se existir, retorno o índice do complemento e o índice atual.
4. Caso contrário, armazeno o número atual como chave e seu índice como valor.

Essa ordem evita usar o mesmo elemento duas vezes, pois o elemento atual ainda não está no dicionário durante a busca. Em outras palavras, o dicionário contém apenas elementos anteriores ao índice atual, e por isso os dois índices retornados sempre serão diferentes.

## Exemplo passo a passo

`nums = [3, 2, 4]` e `target = 6`.

- Índice 0 — valor 3: o complemento é `6 - 3 = 3`. Como o dicionário está vazio, armazeno `{3: 0}`.
- Índice 1 — valor 2: o complemento é `6 - 2 = 4`. Como o número `4` ainda não foi encontrado, armazeno `{3: 0, 2: 1}`.
- Índice 2 — valor 4: o complemento é `6 - 4 = 2`. Como `2` já está no dicionário, recupero seu índice (`1`) e retorno `[1, 2]`.

Se eu inserisse o número atual antes de verificar o complemento, no primeiro passo o número `3` encontraria a si mesmo, produzindo `[0, 0]`. Isso violaria a regra de não usar o mesmo elemento duas vezes.

## Meu erro e o que aprendi

Ao montar o `return`, confundi o valor usado como chave no hash map com o valor armazenado nessa chave.

Por exemplo, em `{2: 1}`:

- A chave `2` é o número encontrado no array.
- O valor `1` é o índice desse número.

```python
vistos = {2: 1}

complemento = 2

print(vistos[complemento])  # 1: índice do complemento
```

Consulto o dicionário pela chave (`complemento`) e uso o valor retornado (`1`) como índice na resposta. Para retornar a resposta correta, preciso dos índices dos dois números, e não dos próprios números.

## Complexidade

- **Tempo:** `O(n)`, pois percorro o array uma única vez e cada busca ou inserção no hash map custa `O(1)` em média.
- **Espaço:** `O(n)`, pois, no pior caso, o dicionário pode armazenar até `n` elementos.