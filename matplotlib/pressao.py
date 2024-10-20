#visualizar dados de pressão atmosférica
#marciana no espaço temporal de um sol marciano.

import json
import matplotlib.pyplot as plt

arquivo = open('../VIKING_I_LANDER/sol_pressao.json', 'r', encoding="utf-8")
dados = arquivo.read()
arquivo.close()

AUSENCIA = -9.999
dadosTratados = json.loads( dados )

def mediaAproximadaIterativa( listaDeListas, campoAlvo=0 ):
    somaIncremental = 0
    for elemento in listaDeListas:
        if elemento[campoAlvo] != AUSENCIA:
            somaIncremental += elemento[campoAlvo]
    return somaIncremental / len(listaDeListas)

media = mediaAproximadaIterativa( dadosTratados, 1 )

def converterMilibarParaPascal( milibares ):
    return milibares*100

#extrai dado de pressão do arquivo de texto formatado via shell Bash
def obterPressao():
    pressoes = []
    for elemento in dadosTratados:
        if elemento[1] != AUSENCIA:
            pressoes.append( converterMilibarParaPascal( elemento[1] ) )
        else:
            pressoes.append( converterMilibarParaPascal( media ) ) #GAMBIARRA
    return pressoes

plt.title("pressão atmosférica média por sol Marciano")
plt.ylabel("pressão média diária (Pascais)")
plt.xlabel("Sois Marcianos")
plt.plot( obterPressao() )
plt.grid()
plt.show()
