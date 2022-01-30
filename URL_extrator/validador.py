import re

def usable_url(self):
    if not self.url:
        raise ValueError("The URL is empty")
    
    pattern_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
    match = pattern_url.match(self.url)
    if not match:
        raise ValueError("The URL is not a URL")
