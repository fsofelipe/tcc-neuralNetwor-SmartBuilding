import numpy as np
import random
#base, faixa de PMVs float
#tempExterna, temperatura externa
#dAmbientes, dados ambientes. Lista contendo todos os PMVs e temperaturas internas.
# lista alternada entre PMV e temp de cada comodo [par = PMV, impar = temp]
#[PMV, temp. (areaDeServico), ..., PMV, temp. (mezanino)]
#return, lista de acoes dos actuators tamanho = 23
def abordagem3_especialista(base, tempExterna, dAmbientes):
    if (len(dAmbientes) < 16):
        print("\tERROR | especialista: dados dos ambientes invalidos")
        return False

    ret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #SEMPRE FECHADAS
    ret[0] = 0 #portaServicoLeste
    ret[3] = 0 #portaCasalOeste (Dont Care)
    ret[6] = 0 #portaBanheiroOeste
    ret[10] = 0 #portaSolteiroSul
    ret[12] = 0 #portaSalaNorte

    #todas as portas internas SEMPRE ABERTAS, exceto as citadas:
    ret[4] = 1 #janelaCasalOeste (brise)
    ret[5] = 1 #janelaBanheiroLeste
    ret[7] = 1 #janelaJardimNorte
    ret[8] = 1 #janelaJardimLeste
    ret[11] = 1 #janelaSolteiroSul (brise)
    ret[14] = 1 #portaSalaLeste
    ret[17] = 1 #portaCozinhaLeste



    #AREA DE SERVICO
    if (dAmbientes[0] < (-base)): #desconforto para o frio
        if (tempExterna > dAmbientes[1]): #rua quente
            ret[1] = 1
    if (dAmbientes[0] > base): #desconforto para o calor
        if (tempExterna < dAmbientes[1]): #rua fria
            ret[1] = 1

    #CIRCULACAO
    #nao tem acoes a tomar


    #QUARTO CASAL
    if (dAmbientes[4] < (-base)): #desconforto para o frio
        if (tempExterna > dAmbientes[5]): #rua quente
            ret[2] = 1
    if (dAmbientes[4] > base): #desconforto para o calor
        if (tempExterna < dAmbientes[5]): #rua fria
            ret[2] = 1

    #BANHEIRO
    #nao tem acoes a tomar

    #JARDIM DE Inverno
    #nao tem acoes a tomar

    #QUARTO SOLTEIRO
    if (dAmbientes[10] < (-base)): #desconforto para o frio
        if (tempExterna > dAmbientes[11]): #rua quente
            ret[9] = 1
    if (dAmbientes[10] > base): #desconforto para o calor
        if (tempExterna < dAmbientes[11]): #rua fria
            ret[9] = 1

    #SALA/COZINHA
    if (dAmbientes[12] < (-base)): #desconforto para o frio
        if (tempExterna > dAmbientes[13]): #rua quente
            ret[13] = 1
            ret[15] = 1
            ret[16] = 1
            ret[18] = 1
    if (dAmbientes[12] > base): #desconforto para o calor
        if (tempExterna < dAmbientes[13]): #rua fria
            ret[13] = 1
            ret[15] = 1
            ret[16] = 1
            ret[18] = 1

    #MEZANINO
    if (dAmbientes[14] < (-base)): #desconforto para o frio
        if (tempExterna > dAmbientes[15]): #rua quente
            ret[19] = 1
            ret[20] = 1
            ret[21] = 1
            ret[22] = 1
    if (dAmbientes[14] > base): #desconforto para o calor
        if (tempExterna < dAmbientes[15]): #rua fria
            ret[19] = 1
            ret[20] = 1
            ret[21] = 1
            ret[22] = 1

    return ret

def abordagem3_random():
    ret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #SEMPRE FECHADAS
    ret[0] = 0 #portaServicoLeste
    ret[1] = float("%.2f"  % random.uniform(0, 1))
    ret[2] = float("%.2f"  % random.uniform(0, 1))
    ret[3] = 0 #portaCasalOeste (Dont Care)
    ret[4] = 1 #janelaCasalOeste (brise)
    ret[5] = 1 #janelaBanheiroLeste
    ret[6] = 0 #portaBanheiroOeste
    ret[7] = 1 #janelaJardimNorte
    ret[8] = 1 #janelaJardimLeste
    ret[9] = float("%.2f"  % random.uniform(0, 1))
    ret[10] = 0 #portaSolteiroSul
    ret[11] = 1 #janelaSolteiroSul (brise)
    ret[12] = 0 #portaSalaNorte
    ret[13] = float("%.2f"  % random.uniform(0, 1))
    ret[14] = 1 #portaSalaLeste
    ret[15] = float("%.2f"  % random.uniform(0, 1))
    ret[16] = float("%.2f"  % random.uniform(0, 1))
    ret[17] = 1 #portaCozinhaLeste
    ret[18] = float("%.2f"  % random.uniform(0, 1))
    ret[19] = float("%.2f"  % random.uniform(0, 1))
    ret[20] = float("%.2f"  % random.uniform(0, 1))
    ret[21] = float("%.2f"  % random.uniform(0, 1))
    ret[22] = float("%.2f"  % random.uniform(0, 1))


    #float("%.2f"  % random.uniform(0, 1))



    return ret

def abordagem3_all0():
    ret = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    return ret

def abordagem3_all1():
    ret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ret[0] = 0 #portaServicoLeste
    ret[1] = 1
    ret[2] = 1
    ret[3] = 0 #portaCasalOeste (Dont Care)
    ret[4] = 1 #janelaCasalOeste (brise)
    ret[5] = 1 #janelaBanheiroLeste
    ret[6] = 0 #portaBanheiroOeste
    ret[7] = 1 #janelaJardimNorte
    ret[8] = 1 #janelaJardimLeste
    ret[9] = 1
    ret[10] = 0 #portaSolteiroSul
    ret[11] = 1 #janelaSolteiroSul (brise)
    ret[12] = 0 #portaSalaNorte
    ret[13] = 1
    ret[14] = 1 #portaSalaLeste
    ret[15] = 1
    ret[16] = 1
    ret[17] = 1 #portaCozinhaLeste
    ret[18] = 1
    ret[19] = 1
    ret[20] = 1
    ret[21] = 1
    ret[22] = 1
    return ret
    return ret
