from simulation import *
from dataNumpy import *
from data import myTime
import sys
from selector import *
import numpy as np

if len(sys.argv) > 1:
    fileNumber = sys.argv[1]
    fileNumber = str(int(fileNumber) -1)

else:
    fileNumber = -1

DataSet = DataManager()
DataSet.createDataset("Data/Numpy/Abordagem3/Randoms/simulation_random_" + str(fileNumber) + ".csv", 53)


Simulate = Connection(50002)
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



    actuators = abordagem3_random()


    np_timeInfo = np.array([timeInfo])
    np_weather = np.array([weather])
    np_actuators = np.array([actuators])

    np_save = np.column_stack((np_timeInfo, np_weather, np_actuators))



    DataSet.sendToDataset(np_save)


    sendToMatlab = ', '.join(str(e) for e in actuators)
    connec[0].sendall(str.encode(sendToMatlab))


Simulate.close()
DataSet.saveDataset()
