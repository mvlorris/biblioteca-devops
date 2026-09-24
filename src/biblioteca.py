def adicionar_livro(titulo, autor):
    return {
        "titulo": titulo,
        "autor": autor
    }


def livro_valido(livro):
    return (
        livro is not None
        and livro.get("titulo") != ""
        and livro.get("autor") != ""
    )


def buscar_livro(titulo, livros):
    if not titulo:
        return None

    for livro in livros:
        if livro.get("titulo") == titulo:
            return livro

    return None
