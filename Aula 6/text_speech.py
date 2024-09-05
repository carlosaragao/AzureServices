import os
from dotenv import load_dotenv
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig
from azure.identity import EnvironmentCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()
KEY_VAULT_NAME = os.getenv('KEY_VAULT_NAME')
KEY_URL = f"https://{KEY_VAULT_NAME}.vault.azure.net"

credencial = EnvironmentCredential()
client = SecretClient(vault_url=KEY_URL, credential=credencial)
retrieved_secret_key = client.get_secret("KEY")
retrieved_secret_region = client.get_secret("REGION")

KEY = retrieved_secret_key.value
REGION = retrieved_secret_region.value

speech_config = SpeechConfig(subscription=KEY, region=REGION)
speech_config.speech_synthesis_language = "pt-BR"
speech_config.speech_synthesis_voice_name = "pt-BR-ElzaNeural"

audio_filename = "output_audio.wav"

audio_config = AudioConfig(filename=audio_filename)

synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "Olá, bem-vindo ao nosso serviço de conversão de texto para fala!"

def text_to_speech(text):
    print("Convertendo texto para fala...")

    result = synthesizer.speak_text(text)

    if result.reason == result.reason.SynthesizingAudioCompleted:
        print(f"Fala sintetizada e salva em '{audio_filename}'")
    elif result.reason == result.reason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Conversão de Texto para Fala cancelada: {cancellation_details.reason}")
        print(f"Detalhes do erro: {cancellation_details.error_details}")

if __name__ == "__main__":
    text_to_speech(text)
