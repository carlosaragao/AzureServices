from dotenv import load_dotenv
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()
KEY = os.environ.get('KEY')
ENDPOINT = os.environ.get('ENDPOINT')

client = ImageAnalysisClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY)
)

result = client.analyze_from_url(
    image_url="https://github.com/carlosaragao.png",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True
)

print("Image analysis results:")
# Print caption results to the console
if result.caption is not None:
    print(" Caption:")
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

# Print text (OCR) analysis results to the console
if result.read is not None and any(result.read.blocks):
    print(" Read:")
    for line in result.read.blocks[0].lines:
        print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
        for word in line.words:
            print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")