livros = []

while True:
    print("\n1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar autor")
    print("4 - Mostrar quantidade")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        categoria = input("Categoria: ").strip()
        editora = input("Editora: ").strip()

        if titulo and autor and categoria and editora:
            livro = {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "editora": editora
            }

            livros.append(livro)
            print("Livro cadastrado com sucesso!")
        else:
            print("Preencha todos os campos.")

    elif opcao == "2":
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                print("\nTítulo:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Categoria:", livro["categoria"])
                print("Editora:", livro["editora"])

    elif opcao == "3":
        autor_busca = input("Digite o nome do autor: ").strip().lower()

        encontrado = False

        for livro in livros:
            if livro["autor"].lower() == autor_busca:
                print("\nTítulo:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Categoria:", livro["categoria"])
                print("Editora:", livro["editora"])
                encontrado = True

        if not encontrado:
            print("Nenhum livro encontrado para esse autor.")

    elif opcao == "4":
        print("Quantidade de livros cadastrados:", len(livros))

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")