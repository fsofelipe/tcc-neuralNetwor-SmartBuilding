import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import optimizers

np.random.seed(7)

from simulation import *
from dataNumpy import *
import sys

##########################################################################################################################

Input = pd.read_csv("Selected/v02_input_grande.csv")
Output = pd.read_csv("Selected/v02_output_grande.csv")

print("Data Set: " + str(len(Input)))
print("Test Set[30%]: " + str(int(len(Input)*0.3)))
print("Training Set [70%]: "+ str(int(len(Input)*0.7)))

X_training = Input[:-int(len(Input)*0.3)].as_matrix()
Y_training = Output[:-int(len(Input)*0.3)].as_matrix()

X_test = Input[int(len(Input)*0.7):].as_matrix()
Y_test = Output[int(len(Input)*0.7):].as_matrix()

##########################################################################################################################

model = Sequential()
model.add(Dense(15, input_shape=(13, ), kernel_initializer='random_normal'))
model.add(Dense(15, activation='relu'))
model.add(Dense(10, activation='sigmoid'))
model.summary()

print ("AQUI")

sgd = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.3, nesterov=True)

# For a mean squared error regression problem
model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['mae', 'acc'])

model.fit(X_training, Y_training, validation_data=(X_test, Y_test), epochs=3, batch_size=32)



##########################################################################################################################



Input = [
    'Hora',

    'TempExterna',
    'ArVeloc',
    'ArDirecao',
    'Umidade',

    'ArDensidade',
    'StatusChuva',

    'PMV_JardimInverno',
    'Temp_JardimInverno',

    'PMV_SalaCozinha',
    'Temp_SalaCozinha',

    'PMV_Mezanino',
    'Temp_Mezanino'
]

Output = [
    'PortaSalaNorte',
    'JanelaSalaNorte',
    'PortaSalaLeste',
    'JanelaSalaSul',
    'JanelaSalaOeste',

    'PortaCozinhaLeste',
    'JanelaCozinhaSul',

    'JanelaMezaninoNorte',
    'JanelaMezaninoSul',
    'JanelaMezaninoOeste'
]

arquivo = pd.DataFrame(columns= Input + Output)
while(True):
    res = input ("Podemos comecar? [sim/nao]")
    if (res.lower() == "sim" or res.lower() == "nao"):
        break


if (res.lower() == "sim"):
    ## SIMULACAO
    Simulate = Connection(50001)
    connec = Simulate.start()


    while True:
        data = connec[0].recv(1024)

        if not data:
            break

        #dados direto do matlab em string
        fromMatlab = data.decode("utf-8")

        #lista com
        dataAndTime = fromMatlab.split(",")

        weatherInText = dataAndTime[0].replace("[", "")
        weatherInText = weatherInText.replace("]", "")

        timeInfo = myTime.getTimeInfo(int(dataAndTime[1]))


        #Gera uma lista com os dados climatologicos
        weather = []
        for x in weatherInText.split(" "):
            weather.append(float(x))

        ##        Hora, TempExterna,
        """
        'Hora',
        'TempExterna', 'ArVeloc', 'ArDirecao', 'Umidade', 'ArDensidade', 'StatusChuva',
        'PMV_JardimInverno', 'Temp_JardimInverno',
        'PMV_SalaCozinha', 'Temp_SalaCozinha',
        'PMV_Mezanino', 'Temp_Mezanino'
        """


        inputRN = [timeInfo[2], weather[0], weather[1], weather[2], weather[3], weather[7], weather[8],
                    weather[19], weather[20], weather[23], weather[24], weather[25], weather[26]]
        np_inputRN = np.array([inputRN])


        """
        ###ACTUATORS DEVEM RECEBER O PREDICT DA REDE
        np_inputRN_normalized = preprocessing.normalize(np_inputRN, norm='l1')

        np_inputRN_normalized = np.delete(np_inputRN_normalized, 6, 1)

        print ("INPUT RN | data:" + str(timeInfo))
        print (np_inputRN_normalized)
        """
        np_outputRN = model.predict(np_inputRN, verbose=0)





        np_timeInfo = np.array([timeInfo[2]])
        np_weather = np.array([weather])

        sendList = np_outputRN.tolist()[0]
        """
        'PortaSalaNorte',
        'JanelaSalaNorte',
        'PortaSalaLeste',
        'JanelaSalaSul',
        'JanelaSalaOeste',

        'PortaCozinhaLeste',
        'JanelaCozinhaSul',

        'JanelaMezaninoNorte',
        'JanelaMezaninoSul',
        'JanelaMezaninoOeste'
        """
        aux = np.array([sendList])

        np_save = np.column_stack((np_timeInfo, np_weather, aux))

        l = pd.Series(np_save, index = Input + Output)


        sendToMatlab = ', '.join(str(float("%.2f" % e)) for e in sendList )

        print("OUTPUT")

        connec[0].sendall(str.encode(sendToMatlab))

        arquivo = arquivo.append(l, ignore_index=True)


    Simulate.close()

print ("FIM!")
