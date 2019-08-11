import sys
import re

#regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ]+"   # raw string
regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ0-9]+"   # raw string

if __name__ == '__main__':
    fileName = sys.argv[1]
    weight   = int(sys.argv[2])

    #O programa aceita stopwords se quisermos
    try:
        stopwordsfile = input('Passe o arquivo das stopwords se houver: ')
        stopwordsfile = open(stopwordsfile,'r')
        stopwords     = set([])
        for s in stopwordsfile.readlines():
            stopwords.add(s.strip().lower())
    except IOError:
        stopwords = 0
        pass
    
    document = open(fileName,'r',encoding='utf8')
    content  = document.read()
    
    Words    = re.findall(regex, content)
    Edges    = dict([])

    if stopwords != 0:
        #Neste implementação o algoritmo ignora a contagem caso alguma das
        #palavras da aresta estiver contida na lista de stopwords
        for i in range(0, len(Words)-1):
            if Words[i] not in stopwords and Words[i+1] not in stopwords:
                edge = (Words[i], Words[i+1])
                if edge not in Edges:
                    Edges[edge] = 0
                Edges[edge] += 1
    else:
        for i in range(0, len(Words)-1):
            edge = (Words[i], Words[i+1])
            if edge not in Edges:
                Edges[edge] = 0
            Edges[edge] += 1

    
    # criando o grafo direcionado (digraph)
    txtGraph = "\ndigraph{"
    
    for v in Edges.keys():
        if Edges[v]>=weight:
            txtGraph += '\n "{}" -> "{}"[label="{}"]'. format(v[0], v[1], Edges[v])
    txtGraph += "\n}"

    print(txtGraph)
    print(f"\nAcima seguem as 'arestas' de palavras com ocorrência superior a {weight} repetições.")

    print ( "\nQuantidade de palavras: {}".format(len(Words)) )   
    print ( "Quantidade de arestas : {}".format(len(Edges)) )   

