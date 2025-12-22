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
    print("\n" + "-"*30)
    print("    CADASTRO DE NOVO LIVRO")
    print("-"*30)
    
    while True:
        titulo = input("Título do livro: ").strip()
        if titulo == "":
            print("Erro: O título não pode ser vazio!")
        else:
            break
    
    while True:
        autor = input("Autor do livro: ").strip()
        if autor == "":
            print("Erro: O autor não pode ser vazio!")
        else:
            break
    
    while True:
        try:
            ano = int(input("Ano de publicação (1500-2025): ").strip())
            if 1500 <= ano <= 2025:
                break
            else:
                print("Erro: O ano deve estar entre 1500 e 2025!")
        except ValueError:
            print("Erro: Digite um ano válido (número inteiro)!")
    
    while True:
        try:
            quantidade = int(input("Quantidade de exemplares: ").strip())
            if quantidade > 0:
                break
            else:
                print("Erro: A quantidade deve ser maior que 0!")
        except ValueError:
            print("Erro: Digite uma quantidade válida (número inteiro)!")
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "quantidade": quantidade
    }
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    print("\n--- Função listar_livros ainda não implementada ---")

def emprestar_livro():
    print("\n--- Função emprestar_livro ainda não implementada ---")

def devolver_livro():
    print("\n--- Função devolver_livro ainda não implementada ---")

if __name__ == "__main__":
    print("Bem-vindo ao BiblioTech!")
    menu()
