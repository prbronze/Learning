import numpy as np

pesos = np.random.rand(3,10)
print(pesos)

ent1 = np.array([
        [1,1,1,0,0,0,0,0,0,0],
        [1,1,0,1,0,0,0,0,0,0],
        [1,1,0,0,1,0,0,0,0,0]]) 

ent2 = np.array([
        [0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,1,0,1,1],
        [0,0,0,0,0,1,0,0,1,1]])

ent3 = np.array([
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,0,1,1,0,1,0,0,0],
        [0,0,0,1,1,0,0,1,0,0]])

'''A escolha foi feita de maneira a manter um grau de sobreposição entre cada uma dos vetores de cada entrada.
Tendo 3 neurônios ativos consideramos então a possibilidade de permutar a posição de 1 dos 3 neurônios ativos.
Espera-se que dessa forma estas entradas sejam clusterizadas ao redor do mesmo neurônio.'''


def redeCompetitiva(X,W):
    '''Para cada entrada gera uma lista vazia de valores de entrada.
    Para cada neurônio calcula o produto vetorial em relacao a entrada e adiciona a esta lista
    printa os produtos notáveis'''
    for x in range(X.shape[0]):
        entrada = [[],[],[]]
        for w in range(W.shape[0]):
            entrada = np.append(entrada,np.dot(W[w],X[x]))
        print(f"\nResultados para a Entrada {w} : ", entrada)
        print('-'*50)
    print(' '*15,'//'*8,'Fim do conjunto de entradas','//'*8)

redeCompetitiva(pesos,ent1)
redeCompetitiva(pesos,ent2)
redeCompetitiva(pesos,ent3)

#Próximo passo é escrever um algoritmo para treinar esta rede
# de tal forma que os neurônios se agrupem formando clusters.

#ambos juntam todos em uma matriz
entradas = np.vstack([ent1,ent2,ent3])
#np.concatenate((ent1,ent2,ent3),axis=0)

<<<<<<< HEAD
def treinaCompetitiva(X,W):
=======

def treinaCompetitiva(X,W,*new_ent):
>>>>>>> 4fc8ad3292c22c1997273d9e61da8666cb2cd150
    #Treinar
    nExemplos = X.shape[0]
    for step in range(4000):
        ex = np.random.randint(nExemplos)
        h = np.dot(W,X[ex]) #lista de produto vetorial
        winner = h.argsort()[-1]
        alpha = 0.05 # convergindo de forma suave
        dw = alpha*(W[winner]*X[ex])
        W[winner] += dw
        #normalizando um a um
<<<<<<< HEAD
        for w in range(W.shape[0]):
            W[w] = W[w]/np.linalg.norm(W[w])

    #Imprimi pesos finais e posições destes pesos
    for w in range(W.shape[0]):
        print(f'Os pesos atualizados do neurônio {w+1} são:\n {W[w]}')
        print(f'Os dois maiores pesos neste caso estão localizados nas posições:\n {W.argsort()[w][:-3:-1]}\n')
    redeCompetitiva(entradas,pesos)
    #testar
=======
        for i in range(W.shape[0]):
            W[i] = W[i]/np.linalg.norm(W[i])

    
    for i in range(W.shape[0]):
        print(f'Os pesos atualizados do neurônio {i+1} são:\n {W[i]}')
        print(f'Os dois maiores pesos neste caso estão localizado nas posições:\n {W.argsort()[i][:-3:-1]}')
        #print(f'Os pesos finais do neurônio {i+1} são:\n {W.argsort()[i]}')
        #nos mostra que os 2 últimos valores de cada um dos vetores convergiu para somados pouco mais de 1

    #testar



treinaCompetitiva(entradas,pesos)

'''
for w in range(W.shape[0]):
        #'Para cada vetor peso (neurônio) faz'
        for step in range(10000):
            #'10000 iterações de treino randomizando uma das 9 entradas'
            ex = np.random.randint(nExemplos)
            h = np.dot(ent[ex],W[w])
            if h >= 0:
                r = 1
            else:
                r = 0
            #atualizar pesos
            0.1*(ent[ex]-W[x])
  return pesos
'''

>>>>>>> 4fc8ad3292c22c1997273d9e61da8666cb2cd150

treinaCompetitiva(entradas,pesos)
