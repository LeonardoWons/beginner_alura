from I_O.csv_for_py import csv_para_contatos
import csv_for_py


try:
    #contatos = csv_for_py.csv_para_contatos("I_O/contatos.csv")
   
    #csv_for_py.contatos_para_pickle(contatos, "I_O/contatos.pickle")
    #contatos = csv_for_py.pickle_para_contatos("I_O/contatos.pickle")
    
    #csv_for_py.contatos_json(contatos, "I_O/contatos.json")
    #contatos = csv_for_py.json_para_contatos("I_O/contatos.json")


    for i in contatos:
        print(f"{i.id} - {i.nome} - {i.email}")

except FileNotFoundError:
    print("Arquivo não encontrado")

except PermissionError:
    print("Permissão negada")
