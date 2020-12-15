from datetime import datetime
dateTimeObj = datetime.now()
zona1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
zona2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
zona3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lugares_zona1 = 0
lugares_zona2 = 0
lugares_zona3 = 0
def getTime():
 dateTimeObj = datetime.now()
 print(" Dia e Hora:",dateTimeObj)
 diaSemana = dateTimeObj.today().weekday()   # 0 é seg, 1 terca
 print("diaSemana ", diaSemana)
 # Access the member variables of datetime object to print date & time information
 #print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
def estacionar():
    hora = dateTimeObj.hour
    diaSemana = dateTimeObj.today().weekday()   # 0 é seg, 1 terca
    if diaSemana < 5:
        print("Parque aberto das 9h às 20h")
        if hora >= 9 and hora <= 20:
            print("Parque aberto!")
            print("Deseja estacionar?")
            print("1-Sim")
            print("2-Não")
            opcao_estacionar = int(input('Insira a opção prentendia: '))
            if opcao_estacionar == 1:
                print("A Zona 1 tem o custo de 1.15€ / hora e a duração máxima de 45 minutos")
                print("A Zona 2  tem o curso de 1€ / hora e a duração máxima de 2 horas")
                print("A Zona 3 tem o custo de 0.62€ /hora e não possui duração máxima")
                print("Prefere estacionar em que zona?")
                print("1 - Zona 1")
                print("2 - Zona 2")
                print("3 - Zona 3")
                opcao_zona = int(input('Insira a opção prentendia: '))
                zonas(opcao_zona)
            elif opcao_estacionar == 2:
                menu_inicial()
            else:
                print("Opção inválida, voltando ao menu inicial!")
                menu_inicial()
        else:
            print("Parque fechado!")
            menu_inicial()
    elif diaSemana == 5:
        print("Parque aberto das 9h às 15h")
        if hora >= 9 and hora <= 15:
            print("Parque aberto!")
            print("Deseja estacionar?")
            print("1-Sim")
            print("2-Não")
            opcao_estacionar = int(input('Insira a opção prentendia: '))
            if opcao_estacionar == 1:
                print("A Zona 1 tem o custo de 1.15€ / hora e a duração máxima de 45 minutos")
                print("A Zona 2  tem o curso de 1€ / hora e a duração máxima de 2 horas")
                print("A Zona 3 tem o custo de 0.62€ /hora e não possui duração máxima")
                print("Prefere estacionar em que zona?")
                print("1 - Zona 1")
                print("2 - Zona 2")
                print("3 - Zona 3")
                opcao_zona = int(input('Insira a opção prentendia: '))
                zonas(opcao_zona)
            elif opcao_estacionar == 2:
                menu_inicial()
            else: 
                print("Opção inválida, voltando ao menu inicial!")
                menu_inicial()
        else:
            print("Parque fechado!")
            menu_inicial()
    else:
        print("Parque aberto todo o dia!")
        print("Deseja estacionar?")
        print("1-Sim")
        print("2-Não")
        opcao_estacionar = int(input('Insira a opção prentendia: '))
        if opcao_estacionar == 1:
            print("O parque é de graça aos domingos!")
            print("Prefere estacionar em que zona?")
            print("1 - Zona 1")
            print("2 - Zona 2")
            print("3 - Zona 3")
            opcao_zona = int(input('Insira a opção prentendia: '))
            zonas(opcao_zona)
        elif opcao_estacionar == 2:
            menu_inicial()
        else:
            print("Opção inválida, voltando ao menu inicial!")
            menu_inicial()
def zonas(zona_estacionar):
    global zona1, zona2, zona3
    global lugares_zona1,lugares_zona2, lugares_zona3
    for i in range(0,len(zona1),1):
        if (zona1[i] == 0):
            lugares_zona1 += 1
    for i in range(0,len(zona2),1):
        if (zona2[i] == 0):
            lugares_zona2 += 1
    for i in range(0,len(zona3),1):
        if (zona3[i] == 0):
            lugares_zona3 += 1
    if zona_estacionar == 1:
        for i in range(0,len(zona1),1):
            if (zona1[i] == 0):
                zona1[i] = 1
                print("Lugar disponível na Zona 1!")
                lugares_zona1 -= 1
                break
        menu_inicial()
    elif zona_estacionar == 2:
        for i in range(0,len(zona2),1):
            if (zona2[i] == 0):
                zona2[i] = 1
                print("Lugar disponível na Zona 1!")
                lugares_zona2 -= 1
                break
        menu_inicial()
    elif zona_estacionar == 3:
        for i in range(0,len(zona3),1):
            if (zona3[i] == 0):
                zona3[i] = 1
                print("Lugar disponível na Zona 1!")
                lugares_zona3 -= 1
                break
        menu_inicial()
    else:
        print("Opção inválida, voltando ao menu inicial!")
        menu_inicial()
        return
    menu_inicial()
def Cliente():
    print("1 - Estacionar")
    print("2 - Ver Zonas")
    print("3 - Ver Histórico")
    print("4 - Voltar")
    print("0 - Sair")
    opcao_cliente = int(input('Insira a opção desejada: '))
    if (opcao_cliente == 1):
        estacionar()
    elif (opcao_cliente == 2):
        print ("Zona 1: ", lugares_zona1, " lugares", "Zona 2: ",lugares_zona2, "lugares", "Zona 3: ", lugares_zona3, " lugares")
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
getTime()
menu_inicial()