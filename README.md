
# Amazon Engineering Challenge — Árvores Binárias Balanceadas

**Nome:** Gabriel Garcia de Lima  
**Disciplina:** Estrutura de Dados Básicos II (EDB 2)  
**Período:** 2026.2

## Sobre o projeto

Projeto de comparação de algoritmos de árvore binária feito para a disciplina de Estrutura de Dados Básicos II (EDB 2), 2026.2.

O trabalho implementa e compara estruturas de busca binária, com foco nas **árvores AVL** e **Rubro-Negra**, utilizando a variante **Left-Leaning Red-Black Tree (LLRB)**. A comparação considera operações de inserção, busca e remoção, além de métricas como altura, rotações, inversões de cores e tempo de execução.

## Organização do projeto

- `structures/bst.py`: implementação da árvore binária de busca (BST), utilizada como base para as demais estruturas.
- `structures/avl.py`: implementação da árvore AVL.
- `structures/RB.py`: implementação da árvore Rubro-Negra na variante LLRB.
- `main.py`: menu interativo para executar operações nas árvores.
- `test.py`: testes das implementações.
- `analysis_comparativa_avl_llrb.ipynb`: notebook de comparação e análise de desempenho, com tabelas e gráficos.

## Análise comparativa

Os experimentos avaliam as estruturas com sequências de valores **crescentes, decrescentes e aleatórias**, comparando inserção, buscas bem-sucedidas e malsucedidas e remoção. Os resultados incluem medições de tempo e indicadores relacionados ao balanceamento das árvores.

## Uso de IA

A IA foi utilizada para auxiliar na implementação do código. Ela serviu como um *pipeline* do que deveria ser implementado, além de ter tirado dúvidas e corrigido trechos do código que estavam sendo problemáticos.

Como o principal objetivo do trabalho era **aprender sobre a implementação dos algoritmos**, os arquivos `test.py` e `analysis_comparativa_avl_llrb.ipynb` foram feitos com uso mais intensivo de IA, uma vez que não eram o foco principal do trabalho e para permitir uma melhor gestão do tempo. O arquivo Main que elabora uma interface CLI para uso das árvores foi feita via vibecoding.
