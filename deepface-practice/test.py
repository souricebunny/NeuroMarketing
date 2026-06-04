from deepface import DeepFace
import os

folder = '/Users/ruhanigill/Desktop/deepface-practice/Pictures/ad'

for img in os.listdir(folder):
    if not img.endswith((".jpg", ".jpeg", ".png")):
        continue
    
    path = f"{folder}/{img}"
    print(f"Processing: {img}...")
    
    result = DeepFace.analyze(
        img_path=path,
        actions=['emotion'],
        enforce_detection=False,
        detector_backend='opencv'
    )
    
    print(f"Dominant: {result[0]['dominant_emotion']}")
    print("---")