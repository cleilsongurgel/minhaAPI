import requests
from faker import Faker

def inserir_registros_api(api_url, quantidade_registros=1):
    """
    Insere registros fictícios em uma API usando a biblioteca Faker
    
    Parâmetros:
    api_url (str): URL da API para envio dos dados
    quantidade_registros (int): Quantidade de registros a serem criados e inseridos
    """
    
    fake = Faker('pt_BR')  # Configuração para dados em português do Brasil

    for _ in range(quantidade_registros):
        # Geração dos dados fictícios
        registro = {
            "nome": fake.name(),
            "conta_corrente": str(fake.random_number(digits=6, fix_len=True)),
            "saldo": round(fake.pyfloat(min_value=1000, max_value=10000, right_digits=2), 2),
            "email": fake.email(),
            "telefone": fake.numerify('119########')  # Formato 11 + 9 dígitos
        }

        try:
            response = requests.post(api_url, json=registro)
            response.raise_for_status()  # Verifica se houve erro na requisição
            
            print(f"Registro inserido com sucesso! ID: {response.json().get('id', 'Não informado')}")
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao inserir registro: {str(e)}")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    API_URL = "http://172.26.45.223/contas"  # Substituir pela URL real da API
    inserir_registros_api(API_URL, 1000)  # Insere 5 registros