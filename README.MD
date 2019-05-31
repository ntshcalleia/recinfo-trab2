# Trabalho 2
**Aluna:** Natasha Monteiro da Rocha  
**Artigo escolhido:** [BitFunnel: Revisiting Signatures for Search](https://danluu.com/bitfunnel-sigir.pdf)  

Durante as aulas aprendemos o que são listas invertidas, que costumam ser muito usadas em sistemas de recuperação de informação para indexar coleções. Listas invertidas são úteis porque elas ocupam apenas o espaço necessário, além de ser fácil encontrar todos os documentos que contém um único termo. Encontrar todos os documentos que contém um conjunto de termos, no entanto, é mais custoso, pois precisamos percorrer a lista de cada um dos termos para encontrar a interseção entre elas.

Suponha que temos uma coleção com N documentos e M termos no total. No pior caso essa complexidade é de O(NM) para listas invertidas, o que é um problema. Existe uma alternativa que faz isso em tempo "constante" O(N): associar a cada termo uma "assinatura" - uma sequência fixa de bits que representa o mesmo -, e representar cada documento pela união da assinatura de todos os seus termos.

Visando reduzir custos operacionais, a Microsoft implementou um novo sistema de busca baseado em tais assinaturas, o BitFunnel. Comparado com o sistema baseado em listas invertidas que ele substituiu, o BitFunnel conseguiu melhorar a capacidade de busca dos servidores da Microsoft em cerca de 10x.

Minha proposta é:
1. Representar uma coleção *(a decidir)* por assinaturas baseadas em filtro de Bloom, similar ao BitFunnel;
2. Realizar consultas conjuntivas e verificar a frequência de falsos positivos.
3. Fazer o mesmo com listas invertidas e comparar o desempenho.