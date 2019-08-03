import sys
import re

regex = r"[-'a-zA-ZÀ-ÖØ-öø-ÿ0-9]+"   # raw string

if __name__ == '__main__':
    fileName = sys.argv[1]
    
    # leitura das stopwords
    stopwordsPTfile = open("stopwords-pt.txt",'r')
    stopwords       = set([]) 

    for s in stopwordsPTfile.readlines():
        stopwords.add(s.strip().lower())

    # leitura do documento
    document = open(fileName,'r',encoding='utf8')
    content  = document.read()

    # identificacao de palavras
    words       = re.findall(regex, content)
    frequencies = dict([])

    # quantidade de vezes no documento
    for w in words:
        w = w.lower()
        if w not in stopwords:
            if w not in frequencies:
                frequencies[w] = 0
            frequencies[w] += 1
    print (f"Tokens: {len(words)}\nVocabulario: {len(frequencies)}")

    #Retornar as N palavras mais frequentes
    N = input("Insira quais as N palavras (número inteiro) mais frequentes você deseja ver: ")
    while True:
        try:
            N = int(N)
        except ValueError:
            N = input('Entrada inválida. Passe um número inteiro: ')
        else:
            break

    print(f"As {N} palavras mais frequentes são: ")
    fs = sorted(frequencies, key=frequencies.get, reverse=True)
    for i in range(0,N):
        print (f"{i+1}ª--> {frequencies[fs[i]]} {fs[i]}")


