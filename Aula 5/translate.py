import os
from dotenv import load_dotenv
from azure.cognitiveservices.speech import AudioConfig
from azure.cognitiveservices.speech.translation import SpeechTranslationConfig, TranslationRecognizer

load_dotenv()
KEY = os.getenv("KEY")
REGION = os.getenv("REGION")

translation_config = SpeechTranslationConfig(subscription=KEY, region=REGION)
translation_config.speech_recognition_language = "pt-BR"
translation_config.add_target_language("fr")

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, 'audio.wav')

audio_config = AudioConfig(filename=audio_path)

recognizer = TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)

def translate_speech():
    print("Traduzindo fala do arquivo de áudio...")
    result = recognizer.recognize_once()

    if result.reason == result.reason.TranslatedSpeech:
        print(f"Fala reconhecida: {result.text}")
        print(f"Tradução para inglês: {result.translations["fr"]}")
    elif result.reason == result.reason.NoMatch:
        print("Nenhuma fala foi reconhecida")
    elif result.reason == result.reason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Tradução de fala cancelada: {cancellation_details.reason}")
        print(f"Detalhes do erro: {cancellation_details.error_details}")

if __name__ == "__main__":
    translate_speech()
