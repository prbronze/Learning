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


def redeCompetitiva(W,X):
    '''Para cada entrada gera uma lista de valores de entrada.
    Para cada neurônio calcula o produto vetorial em relacao a entrada.
    printa os produtos notáveis'''
    for i in range(X.shape[0]):
        entrada = [[],[],[]]
        for x in range(W.shape[0]):
            print(f'\nPesos neuronio {x}:\n',W[x])
            print(f'Entrada {i}:\n',X[i])
            entrada = np.append(entrada,np.dot(W[x],X[i]))
        print(f"\nResultados para a Entrada {i} : ", entrada)
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


def treinaCompetitiva(X,W):
    nExemplos = ent.shape[0]
    for x in range(W.shape[0]):
        '''Para cada vetor peso (neurônio) faz'''
        for step in range(10000):
            '''10000 iterações de treino randomizando uma das 9 entradas'''
            ex = np.random.randint(nExemplos)
            h = np.dot(ent[ex],W[x])
            if h >= 0:
                r = 1
            else:
                r = 0
            #atualizar pesos
  return pesos


