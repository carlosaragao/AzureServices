import os
from dotenv import load_dotenv
from azure.identity import EnvironmentCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()
KEY_VAULT_NAME = os.getenv('KEY_VAULT_NAME')
KEY_URL = f"https://{KEY_VAULT_NAME}.vault.azure.net"

credencial = EnvironmentCredential()
client = SecretClient(vault_url=KEY_URL, credential=credencial)

secret_key_name = "KEY"
retrieved_secret = client.get_secret(secret_key_name)

print(f"Valor do segredo {secret_key_name}: {retrieved_secret.value}")

secret_region_name = "REGION"
retrieved_secret_region = client.get_secret(secret_region_name)

print(f"Valor do segredo {secret_region_name}: {retrieved_secret_region.value}")