from unittest.mock import patch
from colecao.livros import consultar_livros

def test_consultar_livro_retorna_resultado_em_string():
    resultado = consultar_livros("Agatha chistie")
    assert type(resultado) == str

def test_consultar_livro_prepara_dados_com_mesmo_parametro_consultar_livro():
    with patch("colecao.livros.preparar_dados_pra_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")
