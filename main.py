import requests
import time

def request_infinite(url, delay=0.1):
    while True:
        try:
            response = requests.get(url)
            print(f"Status: {response.status_code}, Conteúdo: {response.text[:100]}")
        except Exception as e:
            print(f"Erro ao fazer requisição: {e}")
        time.sleep(delay)


url = "https://er.pb.utfpr.edu.br/pboard/index.php"


request_infinite(url)
