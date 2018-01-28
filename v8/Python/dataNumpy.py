#data numpy structured
import numpy as np
import socket
import datetime
import time
import re
import random


#Objeto capaz de realizar todas as tarefas de arquivo CSV do projeto
class DataManager():

    #Carrega o dataset de um arquivo
    def openDataset(self, name):
        self.dataset = np.loadtxt(name, delimiter=",")
        self.datasetName = name

    def createDataset(self, name, rowSize):
        self.datasetName = name
        self.dataset = np.zeros((1, rowSize))

    def sendToDataset(self, row):
        if (row.shape[1] == self.dataset.shape[1]):
            self.dataset = np.row_stack((self.dataset, row))
            if (np.all(self.dataset[0, :] == 0)):
                self.dataset = np.delete(self.dataset, 0, 0)
            return True
        else:
            print("\tERROR | sendToDataset: formato errado")
            return False

    def saveDataset(self):
        if (len(self.datasetName) > 0):
            np.savetxt(self.datasetName, self.dataset, delimiter=',')
            return True
        else:
            print("\tERROR | saveDataset: Nome invalido")
            return False

class myTime():
    @staticmethod
    def getTimeInfo(seconds):
        d1 = datetime.datetime.fromtimestamp(10800+int(seconds))

        return [int(d1.month), int(d1.day), int(d1.hour)]
