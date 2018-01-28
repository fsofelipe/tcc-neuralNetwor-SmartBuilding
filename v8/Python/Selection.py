from data import *

path = "../Data/"
reader = CSVManager()
selection = CSVManager()

for num in range(1, 200):
    fileName = path + "Data/teste" + str(num) + ".csv"

    reader.openFile(fileName)
    selection.createFromName(path + "Selection")


    workingList = reader.readList()

    count = 0

    while workingList[0] != 'fim':
        PMVs = PMVmanipulator.getPMVs(workingList)
        #print PMVs

        if (PMVmanipulator.select(PMVs, 3.5)):
            count = count + 1

        workingList = reader.readList()

    #print fileName + ": " + str(count)
    print count
    reader.close()
