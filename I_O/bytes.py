arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode="w+")

print(type(arquivo.buffer))

txt_bytes = bytes("Esse é um texto em bytes")

contato = bytes("20, Robsôn, robson@robson.com.br")
arquivo.buffer.write(contato)

arquivo.close()