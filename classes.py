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
                print("Usuário válido. O que deseja fazer agora? \n[1] Reservar \n[2] Desmarcar a reserva \n[3] Voltar \n[4] Sair")
                menuu = int(input("Digite a opção desejada: "))
                match menuu:
                    case 1:
                        Quartos.Marcar()
                        a = 1
                    case 2:
                        Quartos.Desmarcar()
                        a = 1
                    case 3:
                        a = 1
                        break
                    case 4:
                        a = 0                        
                        break         
                    case _:
                        print ("Opção inválida")
            else:
                print("CPF ou senha inválido. Tente fazer o login novamente ou faça um cadastro.")
        return a
        
class Quartos(Hotel):

    def Reserva(self, checkin, checkout, valorfinal):
        self._checkin = checkin
        self._checkout = checkout
        self._valorfinal = valorfinal
        self.quartos = {'Ap de luxo': 200.00,' Ap Master': 150.00, ' Ap Simples': 100.00, 'Ap Simples Casal': 120.00, 'Ap Duplo': 130.00, 'Ap Duplo Casal': 140.00}
    
    def Marcar(self,Clientes):
        menuquartos = int (input("[1] AP de luxo \n[2] AP Master \n[3] AP Simples \n[4] AP Simples Casal \n[5] AP Duplo \n[6] AP Duplo Casal \n[7] Voltar"))
        match menuquartos:
            case 1:
                print (APMaster())
            case 2:
                print ("")
            case 3:
                print ("")
            case 4:
                print ("")
            case 5:
                print ("")
            case 6:
                print ("")
            case 7:
                os.system("cls")
        checkin = {Clientes:data}
        data = input ("Digite a data para o check-in deste modo 'ANO/MÊS/DIAS ")
        marcado = datetime.datetime.strptime (data, "%Y-%m-%d").date()
        if marcado in checkin:
            print("Essa data não está mais disponível, tente novamente.")
        else:
            print ("Check-in:",marcado,"Cliente",Cliente)
        print ("Estas são as opções de quarto: ")
        menuquartos = int (input("[1] AP de luxo \n[2] AP Master \n[3] AP Simples \n[4] AP Simples Casal \n[5] AP Duplo \n[6] AP Duplo Casal \n[7] Voltar"))
    
    
    def Desmascar(self):
        print


    def valorfinal():
        teste = 0
        
    
    def esta_disponivel(self, data_inicio, data_fim):
        for inicio_reserva, fim_reserva in self.reservas:
            if data_inicio < fim_reserva and data_fim > inicio_reserva:
                return False
        return True

    def listar_quartos (self):
        print ("Esses são nossos quartos disponíveis e seus preços:")
        
        
class APMaster(Quartos):
    print("AP MASTER \n \nDescrição: \n- Espaço Amplo; \n- Área de Estar;  \n- Decoração Elegante; \n- Cama Luxuosa; \n- Benheiro Privativo; \n- Comodidades de luxo; \n- Vista Privilegiada; \n- Serviço Personalizado. \n \nPreço da diária: R$200,00.")

    
# class APSimples(Quartos):

# class APSimplesCasal(Quartos):

# class APDuplo(Quartos):

# class APDuploCasal(Quartos):