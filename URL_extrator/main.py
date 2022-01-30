url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

url = url.strip()

if url == "":
    raise ValueError("The url is empty")

url_find = url.find("?")
url_base = url[:int(url_find)]
url_parametre = url[int(url_find) + 1:]

find_parametre = "quantidade"
i_parametre = url_parametre.find(find_parametre)
i_value = i_parametre + len(find_parametre) + 1

i_commercial = url_parametre.find("&", i_value)
if i_commercial == -1:
    value = url_parametre[i_value:]
else:
    value = url_parametre[i_value:i_commercial]

print(value)