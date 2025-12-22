# biblioteca.py
# BiblioTech - Sistema de Gerenciamento de Biblioteca

livros = []  # Lista para armazenar os livros: [{'titulo': , 'autor': , 'ano': , 'quantidade': }]

def menu():
    while True:
        print("\n" + "="*40)
        print("    BIBLIOTECH - GERENCIAMENTO DE LIVROS")
        print("="*40)
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

def cadastrar_livro():
    print("\n--- Função cadastrar_livro ainda não implementada ---")

def listar_livros():
    print("\n--- Função listar_livros ainda não implementada ---")

def emprestar_livro():
    print("\n--- Função emprestar_livro ainda não implementada ---")

def devolver_livro():
    print("\n--- Função devolver_livro ainda não implementada ---")

if __name__ == "__main__":
    print("Bem-vindo ao BiblioTech!")
    menu()
