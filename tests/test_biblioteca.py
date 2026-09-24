from src.biblioteca import adicionar_livro
from src.biblioteca import livro_valido


def test_adicionar_livro():
    livro = adicionar_livro("Clean Code", "Robert C. Martin")
    assert livro["titulo"] == "Clean Code"
    assert livro["autor"] == "Robert C. Martin"


def test_livro_valido():
    livro = adicionar_livro("Effective Java", "Joshua Bloch")
    assert livro_valido(livro) is True


def test_livro_invalido():
    livro = adicionar_livro("", "")
    assert livro_valido(livro) is False
