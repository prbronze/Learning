Em <strong>palavras1.py</strong> um programa que utiliza um padrão de regex para procurar num corpus textual passado como primeiro argumento junto ao programa. Cria-se uma lista de palavras e a contagem de palavras é retornada.

No script <strong>palavras3.py</strong> atualizamos o algoritmo para agora receber um arquivo de stopwords em Português filtrando do dicionário de frequências <em>frequencies</em>. O algoritmo permite interação com o usuário ao pedir um input referente ao ranking das <em>N</em> palavras que o usuário deseja ver printadas na tela.

Para ambos os casos o arquivo é passado como primeiro argumento em sequência ao chamar a função via <em>sys.argv[1]</em>.

A obra escolhida para conduzir estas análises é <em>A Semana</em> do ícone <strong>Machado de Assis</strong>.

-

Em <strong>graph2.py</strong> é implementada uma contagem de arestas de palavras, o programa aceita um arquivo de stopwords para eliminação de palavras menos relevantes. Da forma que está construída a lógica as stopwords não são eliminadas, se e somente se ambas as palavras não estiverem contidas na lista de stopwords é que a tupla em questão é considerada como uma aresta.

Em "O carro bateu no poste" se 'no' é uma stopword a aresta (bateu,poste) não é registrada, isso pode ser problemático para análises futuras.

