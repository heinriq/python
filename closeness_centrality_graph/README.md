# Analise de Proximidade em grafo
Análise de proximidade 

No algoritmo em python se percorre o arquivo .dat, nele é criado um dicionário para representar o grafo.
Na função do coeficiente de proximidade se cria outra lista com todos os vertices para que, em um laço de repetição, por busca exaustiva, se crie o menor caminho do vertice v que está sendo percorrido até cada um dos vertices, isso se repete para todos os vertices.

Em seguida a função retorna um dicionário com os vertices e seus respectivos valores de proximidade.

O código contém comentários para as funções, este é apenas um resumo para explicação.

## Como executar(Windows):

1-Baixe o python versão 2.7

2-Navegue pelo cmd até o local onde está a pasta descompactada nomeada Semantix

3- No diretório onde estiver alocado o script execute o comando
```
python closeness.py
```
4- Se o python estiver instaldo corretamente, será impresso na tela os coeficientes de proximidade em ordem ascendente.

## Como executar(Linux):

1- Instale o python versão 2.7

2- Navegue pelo bash até o diretorio onde está a pasta descomapctada

3- No diretorio onde está alocado o script execute o comando: 
```
python closeness.py
```

4- Se o python estiver instaldo corretamente, será impresso na tela os coeficientes de proximidade em ordem ascendente.
