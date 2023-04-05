#Mostra a relação entre determinados textos, como um detector de plágio

import re

def le_assinatura():
#Essa primeira função retorna a "assinatura de um texto", que são seus traços linguísticos, que será como iremos relacionar os textos

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    ass_cp = [wal, ttr, hlr, sal, sac, pal]

    return ass_cp

def le_textos():
#A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento

    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
#A função recebe um texto e devolve uma lista das sentenças dentro do texto

    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentencas):
#A função recebe uma sentenca e devolve uma lista das frases dentro da sentença

    return re.split(r'[,:;]+', sentencas)

def separa_palavras(frase):
#A função recebe uma frase e devolve uma lista das palavras dentro da frase

    return frase.split()

def n_palavras_unicas(lista_palavras):
#Essa função recebe uma lista de palavras e devolve o numero de palavras que aparecem uma única vez

    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
#Essa função recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
#Essa função recebe a "assinatura" de dois textos e compara a similaridade entre eles, que seria a média da diferença dos valores

    dif1 = abs(as_a[0] - as_b[0])
    dif2 = abs(as_a[1] - as_b[1])
    dif3 = abs(as_a[2] - as_b[2])
    dif4 = abs(as_a[3] - as_b[3])
    dif5 = abs(as_a[4] - as_b[4])
    dif6 = abs(as_a[5] - as_b[5])

    similaridade = (dif1 + dif2 + dif3 + dif4 + dif5 + dif6) / 6

    return similaridade
def calcula_assinatura(texto):
#Essa função recebe o texto a ser testado e devolve a "assinatura" do mesmo

    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    soma_tam_palavras = 0
    caracteres = 0
    carac_frase = 0
   
    for i in range(len(sentencas)):
        frases += separa_frases(sentencas[i])
        caracteres += len(separa_sentencas(texto)[i])
        
    for i in range(len(frases)):
      palavras += separa_palavras(frases[i])
      carac_frase += len(frases[i])

    for i in range(len(palavras)):
      soma_tam_palavras += len(palavras[i])

    #Esses são as fórmulas para calcular os traços do texto
    tam_medio_pa = soma_tam_palavras / len(palavras)
    ty_token = n_palavras_diferentes(palavras) / len(palavras)
    hp_legor = n_palavras_unicas(palavras) / len(palavras)
    tam_medio_sen = caracteres / len(separa_sentencas(texto))
    complex_sen = len(frases) / len(sentencas)
    tam_medio_frase = carac_frase / len(frases)

    return [tam_medio_pa, ty_token, hp_legor, tam_medio_sen, complex_sen, tam_medio_frase]

def avalia_textos(textos, ass_cp):
#Essa função recebe uma lista de textos e uma assinatura e devolve o número do texto (na lista) com maior probabilidade de ser um plágio
   
    inf = []
    
    for texto in textos:

        ass_texto = calcula_assinatura(texto)
        inf.append(compara_assinatura(ass_texto, ass_cp))

    menor = inf[0]
    texto_comprometido = 1

    for i in range(1, len(inf)):
        if (menor > inf[i]):
            c = i
    return texto_comprometido