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

