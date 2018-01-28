import numpy as np
from data import *

from collections import Counter
#MONTA O HISTOGRAMA PARA AVALIAR O RESULTADO DA REDE
if (False):
    RNA_Saida = np.loadtxt("../Data/Out/network04_saida.csv", delimiter=',')
    l0 = []
    for linha in range(0, RNA_Saida.shape[0]):
        l1 = RNA_Saida.tolist()[linha]
        l2 = [] #lista de floats #.##
        for e in l1:
            a = float("%.2f" % e)
            l2.append(a)
        #print (l2)
        l0 = l0 +  l2

    l3 = np.array(l0)

    l4 = np.unique(l3)
    #print (l4)
    counter = 0
    for i in l4:
        counter = counter + np.count_nonzero(l3==i)
        print (str(i) + ": " + str(np.count_nonzero(l3==i)))

    print ("total: " + str(counter))


#CONTABILIZA O TOTAL DE HORAS EM CONFORTO A PARTIR DO RESULTADO DA RNA
if (False):
    limit = 1.5

    dataset = np.loadtxt("../Data/networkOutput.csv", delimiter=',')
    dataset = np.loadtxt("../Data/networkOutput.csv", delimiter=',')
    dataset = np.delete(dataset, 0, 0)
    dataset = np.delete(dataset, dataset.shape[0]-1, 0)

    count = 0

    selected = dataset[0, :]
    for line in range (0, dataset.shape[0]):
        if ( (dataset[line, 14] >= -limit and dataset[line, 14] <= limit) and (dataset[line, 16] >= -limit and dataset[line, 16] <= limit) and
             (dataset[line, 18] >= -limit and dataset[line, 18] <= limit) and
             (dataset[line, 24] >= -limit and dataset[line, 24] <= limit) and
             (dataset[line, 26] >= -limit and dataset[line, 26] <= limit) and (dataset[line, 28] >= -limit and dataset[line, 28] <= limit)):
            selected = np.row_stack((selected, dataset[line, :]))
            count += 1

    print ("conforto"+  ": " + str(count))

    selected = np.delete(selected, 0, 0)

    np.savetxt("../Data/Out/network08_resultado.csv", selected, delimiter=',')

#SELECIONA OS ARQUIVOS PELAS HEURISTICAS DA ABORDAGEM 3 Randoms
if (False):
    limit = 1.5
    for i in range(160, 165):
        dataset = np.loadtxt("../Data/Numpy/Abordagem3/Randoms/simulation_random_" + str(i) + ".csv", delimiter=',')
        dataset = np.delete(dataset, 0, 0)
        dataset = np.delete(dataset, dataset.shape[0]-1, 0)

        count = 0

        selected = dataset[0, :]
        for line in range (0, dataset.shape[0]):
            if ( (dataset[line, 14] >= -limit and dataset[line, 14] <= limit) and (dataset[line, 16] >= -limit and dataset[line, 16] <= limit) and
                 (dataset[line, 18] >= -limit and dataset[line, 18] <= limit) and
                 (dataset[line, 24] >= -limit and dataset[line, 24] <= limit) and
                 (dataset[line, 26] >= -limit and dataset[line, 26] <= limit) and (dataset[line, 28] >= -limit and dataset[line, 28] <= limit)):
                selected = np.row_stack((selected, dataset[line, :]))
                count += 1

        print (str(i) +  ": " + str(count))

        selected = np.delete(selected, 0, 0)
        """
        for linha in range (0, dataset.shape[0]):
            print ("===\t " + str(linha) + "\t===")
            for coluna in range (0, selected.shape[1]):
                print (str(coluna) + ": " + str(selected[linha, coluna]))
        """


        np.savetxt("../Data/Numpy/Abordagem3/Selected/dataSet_random_" + str(i) + ".csv", selected, delimiter=',')

#Concatena os diferentes arquivos em um unico
if (False):
    totalName = "../Data/Numpy/Abordagem3/dataset_total.csv"

    importFolder = "../Data/Numpy/Abordagem3/Selected/dataSet_"

    totalNP = np.loadtxt(importFolder + "All0" + ".csv", delimiter=',')
    print ("All0 = " + str(totalNP.shape))
    print ("totalNP = " + str(totalNP.shape))

    opened = np.loadtxt(importFolder + "All1" + ".csv", delimiter=',')
    print ("All1 = " + str(opened.shape))
    totalNP = np.row_stack((totalNP, opened))
    print ("totalNP = " + str(totalNP.shape))

    opened = np.loadtxt(importFolder + "SE" + ".csv", delimiter=',')
    print ("SE = " + str(opened.shape))
    totalNP = np.row_stack((totalNP, opened))
    print ("totalNP = " + str(totalNP.shape))

    print ("total antes dos randoms" + str(totalNP.shape))

    for fileN in range(0, 165):
        opened = np.loadtxt(importFolder + "random_" + str(fileN) + ".csv", delimiter=',')
        totalNP = np.row_stack((totalNP, opened))


    print ("total final" + str(totalNP.shape))

    np.savetxt(totalName, totalNP, delimiter=',')

#Divide em dataset de input e output (SEM AS TEMPERATURAS INTERNAS)
if (False):
    totalName = "../Data/Numpy/Abordagem3/dataset_total.csv"
    totalNP = np.loadtxt(totalName, delimiter=',')

    print(totalNP.shape)

    inputData = totalNP[:,3:14]
    print (inputData.shape)

    outputData = totalNP[:, 30:53]
    print (outputData.shape)

    np.savetxt("../Data/Numpy/Abordagem3/dataset_input.csv", inputData, delimiter=',')
    np.savetxt("../Data/Numpy/Abordagem3/dataset_output.csv", outputData, delimiter=',')

#Divide em dataset de input e output (COM TEMPERATURAS INTERNAS)
if (False):
    totalName = "../Data/Numpy/Abordagem3/dataset_total.csv"
    totalNP = np.loadtxt(totalName, delimiter=',')

    print(totalNP.shape)

    inputData = totalNP[:,3:14]
    print (inputData.shape)
    temps = np.column_stack((totalNP[:, 15], totalNP[:, 17], totalNP[:, 19], totalNP[:, 21], totalNP[:, 23], totalNP[:, 25], totalNP[:, 27], totalNP[:, 29]))
    print (temps.shape)

    inputData = np.column_stack((inputData, temps))

    print(inputData.shape)


    outputData = totalNP[:, 30:53]
    print (outputData.shape)

    np.savetxt("../Data/Numpy/Abordagem3/dataset_input.csv", inputData, delimiter=',')
    np.savetxt("../Data/Numpy/Abordagem3/dataset_output.csv", outputData, delimiter=',')

#retira as aberturas estaticas do conjunto X (para o treinamento da rede)
if (False):
    X = np.loadtxt("../Data/dataset_output.csv", delimiter=",")
    X = np.delete(X, 17, 1)
    X = np.delete(X, 14, 1)
    X = np.delete(X, 12, 1)
    X = np.delete(X, 11, 1)
    X = np.delete(X, 10, 1)
    X = np.delete(X, 8, 1)
    X = np.delete(X, 7, 1)
    X = np.delete(X, 6, 1)
    X = np.delete(X, 3, 1)
    X = np.delete(X, 0, 1)

    np.savetxt("../Data/dataset_output_13.csv", X, delimiter=',')

    print(X[100000, :])

#remove 0's e insere -1 d
if (False):
    X = np.loadtxt("../Data/dataset_output_13.csv", delimiter=",")
    print (X[1, :])
    X[X == 0] = -1
    print (X[1, :])
    np.savetxt("../Data/dataset_output_13_n.csv", X, delimiter=',')

if (True):
    dataset = np.loadtxt("../Data/Selected/dataSet_SE.csv", delimiter=",")

    print (dataset.shape)

    print (dataset[0, :])

    X = dataset[:, 0:30]
    Y = dataset[:, 30:]

    print (X.shape)
    print (Y.shape)

    np.savetxt("../Data/ds_SE_X.csv", X, delimiter=',')
    np.savetxt("../Data/ds_SE_Y.csv", Y, delimiter=',')
