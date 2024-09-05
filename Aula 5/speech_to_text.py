import os
from dotenv import load_dotenv
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig

load_dotenv()
KEY = os.getenv("KEY")
REGION = os.getenv("REGION")

speech_config = SpeechConfig(subscription=KEY, region=REGION)
speech_config.speech_recognition_language = "pt-BR"

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, 'audio.wav')

audio_config = AudioConfig(filename=audio_path)

speech_recognizer = SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

def recognize_speech():
    print("Reconhecendo fala pelo arquivo de áudio.....")
    result = speech_recognizer.recognize_once()

    if result.reason == result.reason.RecognizedSpeech:
        print(f"Reconhecido: {result.text}")
    elif result.reason == result.reason.NoMatch:
        print("Nenhuma fala foi reconhecida")
    elif result.reason == result.reason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Reconhecimento de fala cancelado: {cancellation_details.reason}")


if __name__ == "__main__":
    recognize_speech()