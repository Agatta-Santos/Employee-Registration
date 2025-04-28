import csv
from datetime import datetime

def cadastrar_funcionario():
    nome = input("Nome do Funcionário: ")
    cargo = input("Cargo do Funcionário: ")
    data_admissao = input("Data de Admissão (DD/MM/AAAA): ")

    # Valida a data
    try:
        data_admissao = datetime.strptime(data_admissao, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida! Usando data atual.")
        data_admissao = datetime.now().date()

    # Armazenar no arquivo CSV
    with open('funcionarios.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, cargo, data_admissao])

    print(f"Funcionário {nome} cadastrado com sucesso!")

def listar_funcionarios():
    try:
        with open('funcionarios.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\nLista de Funcionários Cadastrados:")
            for row in reader:
                print(f"Nome: {row[0]}, Cargo: {row[1]}, Data de Admissão: {row[2]}")
    except FileNotFoundError:
        print("Nenhum funcionário cadastrado ainda.")

def menu():
    while True:
        print("\n1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Iniciar o menu
menu()
