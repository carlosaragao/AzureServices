import os
from dotenv import load_dotenv
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig

load_dotenv()
KEY = os.getenv("KEY")
REGION = os.getenv("REGION")

speech_config = SpeechConfig(subscription=KEY, region=REGION)
speech_config.speech_synthesis_language = "pt-BR"
speech_config.speech_synthesis_voice_name = "pt-BR-ElzaNeural"

# Vozes disponíveis
# pt-BR-FranciscaNeural (Feminino)
# pt-BR-AntonioNeural (Masculino)
# pt-BR-BrendaNeural (Feminino)
# pt-BR-DonatoNeural (Masculino)
# pt-BR-ElzaNeural (Feminino)
# pt-BR-FabioNeural (Masculino)
# pt-BR-GiovannaNeural (Feminino)
# pt-BR-HumbertoNeural (Masculino)
# pt-BR-JulioNeural (Masculino)
# pt-BR-LeilaNeural (Feminino)
# pt-BR-LeticiaNeural (Feminino)
# pt-BR-ManuelaNeural (Feminino)
# pt-BR-NicolauNeural (Masculino)
# pt-BR-ThalitaNeural (Feminino)
# pt-BR-ValerioNeural (Masculino)
# pt-BR-YaraNeural (Feminino)
# pt-BR-ThalitaMultilingualNeural

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
