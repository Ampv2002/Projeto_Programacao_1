from datetime import datetime
def Cliente():
    print("1 - Estacionar")
    print("2 - Ver Zonas")
    print("3 - Ver Histórico")
    print("4 - Voltar")
    print("0 - Sair")
    opcao_cliente = int(input('Insira a opção desejada: '))
    if (opcao_cliente == 1):
        pass
    elif (opcao_cliente == 2):
        pass
    elif (opcao_cliente == 3):
        pass
    elif (opcao_cliente == 4):
        menu_inicial()
    elif (opcao_cliente == 0):
        exit()
def Admnistrador():
    print("1 - Ver Zonas")
    print("2 - Ver Histórico")
    print("3 - Ver Máquinas")
    print("4 - Voltar")
    print("0 - Sair")
    opcao_adm = int(input('Insira a opção desejada: '))
    if (opcao_adm == 1):
        pass
    elif (opcao_adm == 2):
        pass
    elif (opcao_adm == 3):
        pass
    elif (opcao_adm == 4):
        menu_inicial()
    elif (opcao_adm == 0):
        exit()  
def menu_inicial():
    print("Bem-Vindo - Sistema de Parquímetros ")
    print("1 - Admnistrador")
    print("2 - Cliente")
    print("3 - Opções")
    print("0 - Sair")
    opcao_uti = int(input('Insira a opção prentendia: '))
    if(opcao_uti == 1):
        Admnistrador()
    elif (opcao_uti == 2):
        Cliente()
    elif (opcao_uti == 3):
        pass
    elif (opcao_uti == 0):
        pass
    else:
        pass
menu_inicial()
def getTime():
 dateTimeObj = datetime.now()
 print(" Dia e Hora:",dateTimeObj)
 # Access the member variables of datetime object to print date & time information
 #print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
getTime()
def zonas():
    zona1 = [1.15,0.45]
    zona2 = [1,2]
    zona3 = [0.62,0]

