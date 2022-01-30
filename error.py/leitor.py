class LeitorDeArquivo:

    def __init__(self, arquivo_pra_ler):
        self.arquivo = arquivo_pra_ler
        #raise FileNotFoundError
        print(f"Abrindo o arquivo {self.arquivo}")

    def ler_prox_linha(self):
        raise IOError
        print("lendo linha")
        return "linha lida"

    def fechar(self):
        print("fechando arquivo")

    def __enter__(self):
        return self

    def __exit__(self, type, valor, traceback):
        print("fechando arquivo")