import os
from classes import *

hotel = Hotel()

a = 1
while a == 1:
    
    try:
        menu = int(input("BEM-VINDO MALTVAGO! \n[1] Login \n[2] Cadastro \n[3] Sair \nDigite a opção desejada: "))
        if menu == 1:
            os.system("cls")
            ccpf = int(input("Digite o CPF: "))
            csenha = input("Digite a senha: ")
            hotel.login(ccpf,csenha)
            
            

     
        if menu == 2:
            os.system("cls")
            print("Preencha as informações: \n")
            nome = input("Digite seu nome: ")
            telefone = int(input("Digite seu telefone: "))
            email = input("Digite seu E-mail: ")
            cpf = int(input("Digite seu cpf: "))
            senha = input("Digite sua senha :")
            hotel.cliente(nome, telefone, email, cpf, senha)
            

        if menu == 3:
            a = 0
            
    except Exception as erro:
        print(erro.__class__.__name__)