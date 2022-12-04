import random
import string

FRASE = ''
FRASE_LEN = 0
LETRAS = string.ascii_letters + ' ' + string.punctuation
GERACOES = 100
GERACAO_POPULACAO = 100

todasAsGeracoes = []

melhorString = {
    'string': '',
    'ponto': 0,
    'baseParaNovaGeracao': ''
}


def stringAleatoria(frase_len): #gerador de string aleatoria
    return ''.join(random.choice(LETRAS) for _ in range(frase_len))


def criarStringInicial():
    todasAsGeracoes.append([stringAleatoria(FRASE_LEN) for _ in range(GERACAO_POPULACAO)])


def construirNovaGeracao(melhor): #iteração do processo
    baseNovaGeracao = ''
    for i in range(FRASE_LEN):
        if FRASE[i] == melhor[i]:
            baseNovaGeracao = baseNovaGeracao + melhor[i]
        else:
            baseNovaGeracao = baseNovaGeracao + '*'
    melhorString['baseParaNovaGeracao'] = baseNovaGeracao


def mudarChar(frase, index, char): #troca o que tem antes e depois do caracter que está certo
    return frase[:index] + char + frase[index + 1:]


def trocarFaltaDeCombinacao():
    tempString = melhorString['baseParaNovaGeracao']
    for i, letra in enumerate(tempString):
        if letra == '*':
            tempString = mudarChar(tempString, i, random.choice(LETRAS))
    return tempString


def criarNovaGeracao():
    construirNovaGeracao(melhorString['string'])
    todasAsGeracoes.append([trocarFaltaDeCombinacao() for _ in range(GERACAO_POPULACAO)])


def atualizarMelhorString(frase, ponto):
    melhorString['string'] = frase
    melhorString['ponto'] = ponto


def pontuarString(frase):
    ponto = 0
    for i in range(FRASE_LEN):
        if FRASE[i] == frase[i]:
            ponto += 1
    return ponto


def correspondencia():
    ultimaGeracao = todasAsGeracoes[-1]
    for string in ultimaGeracao:
        ponto = pontuarString(string)
        if ponto > melhorString['ponto']:
            atualizarMelhorString(string, ponto)


def printMelhorString():
    print('Geração ' + str(len(todasAsGeracoes)))
    print('Melhor string até o momento: ' + melhorString['string'])


def gerador(frase):  # Função principal geradora de frases
    global FRASE
    FRASE = frase
    global FRASE_LEN
    FRASE_LEN = len(frase)
    criarStringInicial()
    correspondencia()
    printMelhorString()
    for _ in range(GERACOES):
        if melhorString['string'] == FRASE:
            printMelhorString()
            print('Frase formada em ' + str(len(todasAsGeracoes)) + ' gerações')
            return ''
        criarNovaGeracao()
        correspondencia()
        printMelhorString()


gerador(input('Digite uma frase:'))
