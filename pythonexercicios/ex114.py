import requests

try:
    requisição = requests.get('http://pudim.com.br/')
except:
    print('\033[31mO site PUDIM.COM.BR não está acessível no momento.\033[m')
else:
    print('\033[34mO site PUDIM.COM.BR está acessível neste momento.\033[m')
