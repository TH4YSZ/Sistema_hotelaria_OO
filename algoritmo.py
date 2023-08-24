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
            confirmar_cpf = Hotel(ccpf)
            confirmar_senha = Hotel(csenha)
        
     
        if menu == 2:
            print("teste")

        if menu == 3:
            a = 0
            
    except Exception as erro:
        print("Opção inválida.")