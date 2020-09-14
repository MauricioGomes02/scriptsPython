class Raiz:
    def __init__(self, indice, radiciando, precisao):
        self.indice = indice
        self.radiciando = radiciando
        self.casasDecimais = precisao

    def separaCasasDecimais(self):
        listaAgrupamento = []
        casas = self.casasDecimais

        cont = 0
        while cont < casas:
            listaAgrupamento.append('0' * self.indice)
            cont += 1
        
        return listaAgrupamento
    
    def procuraNumeroElevadoAoIndiceMaisProximo(self):
        valor = self.radiciando
        cont = 0
        while (cont ** self.indice) <= valor:
            cont += 1
        return cont - 1

    def calculaRaiz(self):
        valor = self.radiciando        
        listaAgrupamento = self.separaCasasDecimais()
        NumeroElevadoAoIndiceMaisProximo = self.procuraNumeroElevadoAoIndiceMaisProximo()
        resultadoRaiz = NumeroElevadoAoIndiceMaisProximo
        resultadoRaizStr = str(NumeroElevadoAoIndiceMaisProximo) + '.'

        cont = 0
        while cont < len(listaAgrupamento):
            conjuntoFantasma = self.indice * resultadoRaiz
            
            if cont == 0:
                resultadoSubtracao = valor - (resultadoRaiz ** self.indice)
            else:
                resultadoSubtracao = valor - conjuntoFantasmaMultiplicar

            resultadoSubtracaoFormatado = int(str(resultadoSubtracao) + listaAgrupamento[cont])

            i = 0
            while True:
                if (int(str(conjuntoFantasma) + str(i))) * i > resultadoSubtracaoFormatado and i != 0:
                    i -= 1
                    break
                i += 1

            numeroFantasma = str(i)
            conjuntoFantasmaMultiplicar = int(str(conjuntoFantasma) + numeroFantasma) * int(numeroFantasma)
            valor = int(str(resultadoSubtracao ) + listaAgrupamento[cont])
            
            resultadoRaiz = int(str(resultadoRaiz) + numeroFantasma)
            resultadoRaizStr = resultadoRaizStr + numeroFantasma

            cont += 1
        
        return [float(resultadoRaizStr), resultadoRaizStr]

raiz = Raiz(3,27,2)
# Primeiro parâmetro = Índice da raíz, Segundo parâmetro = Radiciando da raíz, Terceiro parâmetro = Número de casas decimais.
print(raiz.calculaRaiz())
# Retorna em [float, string]
