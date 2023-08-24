import datetime
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
    
    def login(self, ccpf, csenha):
        for cliente in self._Clientes:
            if cliente['CPF:'] == ccpf and cliente['Senha'] == csenha:                
                print("Usuário válido. O que deseja fazer agora?")
                print("[1] Reservar")
                print("[2] Desmarcar a reserva")
                print("[3] Voltar")
                print("[4] Sair")
                menuu = int(input("Qual opção deseja?: "))
                match menuu:
                    case 1:
                        Quartos.Reserva()
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
    
    def Marcar(self):
        checkin = {'cliente':data}
        data = input ("Digite a data para o check-in deste modo 'ANO/MÊS/DIAS ")
        
        marcado = datetime.datetime.strptime (data, "%Y-%m-%d").date()

        




    
    
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
        
        

# class APLuxo(Quartos):

#     # def __init__(self):
#     #     self.
# 

class APMaster(Quartos):
    self.Reserva = []
    descricao = "- Espaço Amplo; - Área de Estar;  - Decoração Elegante; - Cama Luxuosa; - Benheiro Privativo; - Comodidades de luxo; - Vista Privilegiada; - Serviço Personalizado."

# class APSimples(Quartos):

# class APSimplesCasal(Quartos):

# class APDuplo(Quartos):

# class APDuploCasal(Quartos):