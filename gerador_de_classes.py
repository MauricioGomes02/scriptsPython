import os

caminhoRaiz = os.path.dirname(__file__)

def primeiraLetraMaiuscula(parametro):
    parametro = parametro[0:1].upper() + parametro[1:len(parametro)]
    return parametro


#Apaga se houver algum arquivo com o mesmo nome
if os.path.exists(caminhoRaiz + '\\' + 'renomear.py'):
    os.remove(caminhoRaiz + '\\' + 'renomear.py')
    print('Arquivo deletado!')

#Setar informações:
listaDeParametros = [{
    'NomeClasse': 'bulldog',
    'Atributos': [
        'comida',
        'qtdCoco',
        'tmpDormir',
        'tmpBrincar',
        'qtdLatido',
    ]},
    {'NomeClasse': 'bulldog',
    'Atributos': [
        'comida',
        'qtdCoco',
        'tmpDormir',
        'tmpBrincar',
        'qtdLatido',
    ]}
]
print(len(listaDeParametros))

#Cria arquivo renomear.py
arquivoParaEscrita = open(caminhoRaiz + '\\' + 'renomear.py', 'a')
conteudoArquivo = list()

contClass = 0
while contClass < len(listaDeParametros):
    conteudoArquivo.append('class ' + listaDeParametros[contClass]['NomeClasse'] + ':\n')

    #Linha def __init__
    contAtributos = 0
    stringCompletaDefInit = ''
    while contAtributos < len(listaDeParametros[contClass]['Atributos']):        
        if contAtributos == 0:
            stringCompletaDefInit = '    def __init__(self, ' + listaDeParametros[contClass]['Atributos'][contAtributos]
        elif contAtributos < len(listaDeParametros[contClass]['Atributos']) - 1:
            stringCompletaDefInit += ', ' + listaDeParametros[contClass]['Atributos'][contAtributos]
        else:
            stringCompletaDefInit += ', ' + listaDeParametros[contClass]['Atributos'][contAtributos] +  '):'
        contAtributos += 1
    conteudoArquivo.append(stringCompletaDefInit + '\n')
    
    #Linha Atributos
    contAtributos = 0
    while contAtributos < len(listaDeParametros[contClass]['Atributos']):
        conteudoArquivo.append('        self.' + listaDeParametros[contClass]['Atributos'][contAtributos] + ' = ' + listaDeParametros[contClass]['Atributos'][contAtributos] + '\n')
        contAtributos += 1

    #Linhas de get()
    contAtributos = 0
    while contAtributos < len(listaDeParametros[contClass]['Atributos']):
        conteudoArquivo.append('    def get' + primeiraLetraMaiuscula(listaDeParametros[contClass]['Atributos'][contAtributos]) + '(self):\n')
        conteudoArquivo.append('        return self.' + listaDeParametros[contClass]['Atributos'][contAtributos] + '\n')
        contAtributos += 1

    #Linhas de set()
    contAtributos = 0
    while contAtributos < len(listaDeParametros[contClass]['Atributos']):
        conteudoArquivo.append('    def set' + primeiraLetraMaiuscula(listaDeParametros[contClass]['Atributos'][contAtributos]) + '(self, ' + listaDeParametros[contClass]['Atributos'][contAtributos] + '):\n')
        conteudoArquivo.append('        self.' + listaDeParametros[contClass]['Atributos'][contAtributos] + ' = ' + listaDeParametros[contClass]['Atributos'][contAtributos] + '\n')
        contAtributos += 1
    conteudoArquivo.append('\n')
    contClass += 1

arquivoParaEscrita.writelines(conteudoArquivo)    
arquivoParaEscrita.close()