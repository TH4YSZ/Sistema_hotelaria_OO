class Cliente():
    def __init__(self, nome, cpf, telefone, email, senha):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._senha = senha



class Hotel():
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
            else:
                print("CPF ou senha inválido. Tente fazer o login novamente ou faça um cadastro.")
      
        
class Quartos(Hotel):

    def Reserva(self, checkin, checkout, valorfinal):
        self._checkin = checkin
        self._checkout = checkout
        self._valorfinal = valorfinal
        self.quartos = {'Ap de luxo': 200.00,' Ap Master': 150.00, ' Ap Simples': 100.00, 'Ap Simples Casal': 120.00, 'Ap Duplo': 130.00, 'Ap Duplo Casal': 140.00}
    

    def listar_quartos (self):
        print ("Esses são nossos quartos disponíveis e seus preços:")
        

# class APLuxo(Quartos):

#     # def __init__(self):
#     #     self.
# 

class APMaster(Quartos):
    self.Reserva = []
    self.Descricao = "Este quarto possui hidromassagem"

    def getDescricao():
        return Descricao


# class APSimples(Quartos):

# class APSimplesCasal(Quartos):

# class APDuplo(Quartos):

# class APDuploCasal(Quartos):
