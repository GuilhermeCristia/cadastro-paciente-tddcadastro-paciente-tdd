from src.paciente import Paciente

def mostrar_menu():
    print("\n--- Sistema de Cadastro de Pacientes ---")
    print("1. Cadastrar novo paciente")
    print("2. Listar pacientes cadastrados")
    print("3. Sair")
    return input("Escolha uma opção: ")

def cadastrar_paciente():
    print("\n--- Novo Cadastro ---")
    
    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (AAAA-MM-DD): ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    genero = input("Gênero (Masculino/Feminino/Outro/Prefiro não informar): ")
    email = input("Email: ")
    
    try:
        paciente = Paciente(nome, data_nasc, cpf, telefone, genero, email)
        print(f"\n✅ Paciente {paciente.nome_completo} cadastrado com sucesso!")
        return paciente
    except ValueError as e:
        print(f"\n❌ Erro no cadastro: {e}")
        return None

def main():
    pacientes = []
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            paciente = cadastrar_paciente()
            if paciente:
                pacientes.append(paciente)
        
        elif opcao == "2":
            print("\n--- Pacientes Cadastrados ---")
            if not pacientes:
                print("Nenhum paciente cadastrado ainda.")
            else:
                for i, paciente in enumerate(pacientes, 1):
                    print(f"\nPaciente {i}:")
                    print(f"Nome: {paciente.nome_completo}")
                    print(f"CPF: {paciente.cpf}")
                    print(f"Data Nasc.: {paciente.data_nascimento}")
                    print(f"Telefone: {paciente.telefone}")
                    print(f"Gênero: {paciente.genero}")
                    print(f"Email: {paciente.email}")
        
        elif opcao == "3":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()