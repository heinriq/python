edges = open("edges.dat", "r")

grafo = {}

for line in edges:
    u, v = line.split()
    if u not in grafo:
        grafo[u] = {}
        grafo[u][v] = {}
    else:
        grafo[u][v] = {}

    if v not in grafo:
        grafo[v] = {}
        grafo[v][u] = {}
    else:
        grafo[v][u] = {}


#CoeficienteDeProximidade: Funcao que retorna um dicionario com o coeficiente de proximidade de cada vertice
#grafo: dicionario dos vertices e suas arestas
#vertice: parametro opcional que caso seja usado, ira trazer o coeficiente de uma aresta especifica

def CoeficienteDeProximidade(grafo, vertice=None):
    closeness_centrality = {}
    vertices = []

    for key, value in grafo.iteritems():
        vertices.append(key)

    for v in vertices:
        MenorCaminho = Verify_MenorCaminho(grafo,v)
        SomaDoMenorCaminho = sum(MenorCaminho.values())
        if SomaDoMenorCaminho > 0.0 and len(grafo) > 1:
            closeness_centrality[v] = (len(MenorCaminho)-1.0) / SomaDoMenorCaminho
            mult = (len(MenorCaminho)-1.0) / ( len(grafo) - 1 )
            closeness_centrality[v] *= mult
        else:
            closeness_centrality[v] = 0.0
    if vertice is not None:
        return closeness_centrality[u]
    else:
        return closeness_centrality

#Verificador do menor caminho: ira usar busca exaustiva para encontrar o menor caminho
#grafo: o dicionario completo do grafo, vertices e arestas
#vertice: o vertice que se deseja descobrir o menor caminho

def Verify_MenorCaminho(grafo, vertice):
    visitados={}                  
    nivel=0              
    proximo={vertice:1}
    while proximo:
        atual=proximo  
        proximo={}
        for v in atual:
            if v not in visitados:
                visitados[v]=nivel
                proximo.update(grafo[v])
        nivel+=1
    return visitados
for key, value in sorted(CoeficienteDeProximidade(grafo).iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
