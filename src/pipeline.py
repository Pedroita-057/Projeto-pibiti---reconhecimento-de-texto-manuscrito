from preprocessing.image_preprocessing import preprocess_image
from model.htr_model import recognize_text
from evaluation.metrics import evaluate

raw_image = "data/raw/exemplo.png"
processed_image = "data/processed/exemplo.png"
reference_text_path = "data/annotations/exemplo.txt"

# Pré-processamento
preprocess_image(raw_image, processed_image)

# Reconhecimento
predicted_text = recognize_text(processed_image)

# Texto real
with open(reference_text_path, "r", encoding="utf-8") as f:
    reference_text = f.read()

# Avaliação
metrics = evaluate(predicted_text, reference_text)

print("Texto reconhecido:")
print(predicted_text)

print("\nAvaliação:")
print(metrics)
