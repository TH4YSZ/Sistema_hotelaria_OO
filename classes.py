import datetime
import os
class Cliente():
    def __init__(self, nome, cpf, telefone, email, senha):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._senha = senha

class Hotel(Cliente):
    def __init__(self):
        self._Clientes = []

    def cliente(self, nome, cpf, telefone, email, senha):
        cliente = {"Nome:": nome, "CPF:": cpf, "Telefone:": telefone, "Email" :email, "Senha": senha} 
        self._Clientes.append(cliente)
        print("Cliente Cadastrado. Faça seu login.")
        os.system("pause")
        os.system("cls")
    
    def login(self, ccpf, csenha):
        for cliente in self._Clientes:
            if cliente['CPF:'] == ccpf and cliente['Senha'] == csenha:                
                print("Usuário válido. O que deseja fazer agora? \n[1] Reservar \n[2] Voltar \n[3] Sair")
                menuu = int(input("Digite a opção desejada: "))
                match menuu:
                    case 1:
                        Quartos.Marcar()
                        a = 1
                    case 2:
                        a = 1
                        break
                    case 3:
                        a = 0                        
                        break         
                    case _:
                        print ("Opção inválida")
            else:
                print("CPF ou senha inválido. Tente fazer o login novamente ou faça um cadastro.")
        return a
        
class Quartos(Hotel):
    
    def Marcar(self):
        menuquartos = int (input("[1] AP de luxo \n[2] AP Master \n[3] AP Simples \n[4] AP Simples Casal \n[5] AP Duplo \n[6] AP Duplo Casal \n[7] Voltar"))
        match menuquartos:
            case 1:
                APLuxo.ap_L()
            case 2:
                APMaster.ap_M()
            case 3:
                APSimples.ap_S()     
            case 4:
                APSimplesCasal.ap_SC()
            case 5:
                APDuplo.ap_D()
            case 6:
                APDuploCasal.ap_DC()
            case 7:
                os.system("cls")
    

class APLuxo (Quartos):
    def ap_L():
        APL = 0
        APL2 = 0
        print ("AP Luxo \n \nDescrição: \n- Espaçoso e Acolhedor; \n- Cama de Qualidade Superior; \n- Área de Estar; \n-Varanda Privativa; \n-Decoração Sofisticada \n-Tecnologia Avançada; \n Serviço de Quarto 24 Horas. \n \nPreço da diária: R$7000,00")
        quarto1 = int (input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto1:
            case 1:
                if APL == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*7000
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APL = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APL2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*7000
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APL2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.")  


class APMaster(Quartos):
    def ap_M():
        APM = 0
        APM2 = 0
        print("AP MASTER \n \nDescrição: \n- Espaço Amplo; \n- Área de Estar;  \n- Decoração Elegante; \n- Cama Luxuosa; \n- Banheiro Privativo; \n- Comodidades de luxo; \n- Vista Privilegiada; \n- Serviço Personalizado. \n \nPreço da diária: R$300,00.")
        quarto2 = int(input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto2:
            case 1:
                if APM == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*6200
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APM = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APM2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*6200
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APM2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.")    

class APSimples(Quartos):
    def ap_S():
        APS = 0
        APS2 = 0
        print ("AP Simples \n \nDescrição: \n- Espaço confortável; \n- Cama de solteiro \n- Mesa de trabalho \n-Banheiro privativo \n-Televisão \n-Serviço de limpeza diário. \n \nPreço da diária: R$1000,00")
        quarto3 = int (input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto3:
            case 1:
                if APS == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*1000
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APS = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APS2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*1000
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APS2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.")  

class APSimplesCasal():
    def ap_SC():
        APSC = 0
        APSC2 = 0
        print ("AP Simples \n \nDescrição: \n- Espaço confortável; \n- Cama King \n- Mesa de trabalho \n-Banheiro privativo \n-Televisão \n-Serviço de limpeza diário. \n \nPreço da diária: R$1500,00")
        quarto4 = int (input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto4:
            case 1:
                if APSC == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*1500
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APS = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APSC2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*1500
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APS2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.")
        

class APDuplo(Quartos):
    def ap_D():
        APD = 0
        APD2 = 0
        print("AP Duplo \n \nDescrição: \n- Camas Confortáveis; \n- Área de Estar;  \n- Banheiro Privativo; \n- Ar Condicionado ou Aquecimento; \n- TV e Wi-Fi; \n- Serviço de Quarto; \n- Vista. \n \nPreço da diária: R$2500,00.")
        quarto5 = int(input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto5:
            case 1:
                if APD == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*2500
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APD = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APD2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*2500
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APD2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.") 

class APDuploCasal(Quartos):
    def ap_DC():
        APDC = 0
        APDC2 = 0
        print("AP MASTER \n \nDescrição: \n- Espaço Amplo; \n- Área de Estar;  \n- Decoração Elegante; \n- Cama Luxuosa; \n- Banheiro Privativo; \n- Comodidades de luxo; \n- Vista Privilegiada; \n- Serviço Personalizado. \n \nPreço da diária: R$300,00.")
        quarto7 = int(input("[1] Quarto 1 \n[2] Quarto 2 \n[3] Voltar \nQual quarto deseja reservar?: "))
        match quarto7:
            case 1:
                if APDC == 0:
                    diaria = int(input("Número de dias: "))
                    valor_total = diaria*3000
                    print(f"O valor total da reserva é: R$, {valor_total}")
                    APDC = 1
                else:
                    print("Este quarto está indisponível.")
            case 2:
                if APDC2 == 0:
                    diaria2 = int(input("Número de dias: "))
                    valor_total2 = diaria2*3000
                    print(f"O valor total da reserva é: R$, {valor_total2}")
                    APDC2 = 1
                else:
                    print("Este quarto está indisponível.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                os.system("cls")
            case _:
                print("Opção inválida.")