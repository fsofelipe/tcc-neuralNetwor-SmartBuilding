import socket
import datetime

class Connection():



    def __init__(self, port):
        self.startTime = datetime.datetime.now()
        self.endTime = datetime.datetime.now()
        HOST = 'localhost'
        PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(1)

    def start(self):
        print("PYTHON || simulacao.py: Iniciando simulacao\nPYTHON || simulacao.py: Esperando inicializacao do BCVTB")
        conn, addr = self.s.accept()
        print("PYTHON || simulation.py: Recebendo dados")

        return [conn, addr]

    def close(self):
        self.endTime = datetime.datetime.now()
        self.s.close()
        print("PYTHON || simulacao.py: SIMULACAO CONCLUIDA")
        print("PYTHON || simulacao.py: TEMPO DA SIMULACAO: " + str(self.endTime - self.startTime))
