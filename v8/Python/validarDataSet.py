from data import *

arq0 = CSVManager()
arq0.openFile("../tester0.csv")

arq1 = CSVManager()
arq1.openFile("../tester1.csv")

list0 = arq0.readList()
list1 = arq1.readList()

iguais = []

linha = 1

while list0[0] != 'fim':
    dif = False
    #print ("list0: " + list0[14] + ", " + list0[16] + ", " + list0[18] + ", " + list0[20] + ", " + list0[22] + ", " + list0[24] + ", " + list0[26] + ", "+ list0[28])
    #print ("list1: " + list1[14] + ", "+ list1[16] + ", " + list1[18] + ", " + list1[20] + ", " + list1[22] + ", " + list1[24] + ", " + list1[26] + ", "+ list1[28])
    #print("---")


    for i in [14, 16, 18, 20, 22, 24, 26, 28]:
        if list0[i] != list1[i]:

            dif = True

    if dif == False:
        iguais.append(list0)
        print (linha)

    list0 = arq0.readList()
    list1 = arq1.readList()
    linha = linha + 1


print(len(iguais))

for item in iguais:
    print (item)
    print ('\n')
