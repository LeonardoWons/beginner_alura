import csv, pickle, json
from contato import Contato


def csv_para_contatos(caminho, encoding="latin_1"):
    contatos = []

    with open(caminho, encoding= encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for i in leitor:
            id, nome, email = i
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode="wb") as arquivo:
        pickle.dump( contatos, arquivo)


def pickle_para_contatos(caminho):
    with open(caminho, mode="rb") as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

def contatos_json(contatos, caminho):
    with open(caminho, mode= "w") as arquivo:
        json.dump(contatos, arquivo, default=_contato_json)
    #ou json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)
    #ai nao precisa do def de baixo

def _contato_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for i in contatos_json:
            c = Contato(i["id"], i["nome"], email=i["email"]) #ou  metodo desenpacotamento: c = Contato(**i)
            contatos.append(c)

    return contatos