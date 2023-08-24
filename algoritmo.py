import os
from classes import *

hotel = Hotel()

global a
a = 1
while a == 1:
    
    try:
        menu = int(input("BEM-VINDO MALTVAGO! \n[1] Login \n[2] Cadastro \n[3] Sair \nDigite a opção desejada: "))
        match menu:
            case 1:
                os.system("cls")
                ccpf = int(input("Digite o CPF: "))
                csenha = input("Digite a senha: ")
                a = hotel.login(ccpf,csenha)           
     
            case 2:
                os.system("cls")
                print("Preencha as informações: \n")
                nome = input("Digite seu nome: ")
                telefone = int(input("Digite seu telefone: "))
                email = input("Digite seu E-mail: ")
                cpf = int(input("Digite seu cpf: "))
                senha = input("Digite sua senha :")
                hotel.cliente(nome, telefone, email, cpf, senha)

            case 3:
                a = 0
            
            case _:
                print ("Opção inválida")
            
    except Exception as erro:
        print("Opção inválida.")
        os.system("pause")
        os.system("cls")