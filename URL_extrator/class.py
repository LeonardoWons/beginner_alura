import re

class extrator_url:
    def __init__(self, url):
        self.url = url.strip()
        self.usable_url()
        self.alert()

    def url_str(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def usable_url(self):
        if not self.url:
            raise ValueError("The URL is empty")

        pattern_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = pattern_url.match(self.url)

        if not match:
            raise ValueError("The URL is not a URL")

    def get_url_base(self):
        url_find = self.url.find("?")
        url_base = self.url[:int(url_find)]
        return url_base

    def get_url_parametre(self):
        url_find = self.url.find("?")
        url_parametre = self.url[int(url_find) + 1:]
        return url_parametre
    
    def get_value_parametre(self, name_parametre):
        find_parametre = name_parametre
        i_parametre = self.get_url_parametre().find(find_parametre)
        i_value = i_parametre + len(find_parametre) + 1
        i_commercial = self.get_url_parametre().find("&", i_value)

        if i_commercial == -1:
            value = self.get_url_parametre()[i_value:]
        else:
            value = self.get_url_parametre()[i_value:i_commercial]
        return value
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        url_complet = (self.get_url_base(), " ", self.get_url_parametre())
        return url_complet 
    
    def __eq__(self, other):
        return self.url == other

    #def conversation(self,x, money):
        if (x == 1):
            money_convert = money * 5.5
        else:
            money_convert = money / 5.5
        
        return money_convert
    
    #def alert(self):
        print("If you transform dollar to real = 1 , if real to dollar = 0, and latter the money to convert")
