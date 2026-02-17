# Aqui são todas as importações

# aqui é o redimenensionamento, normalização, remoção de ruído da iamgem.
from preprocessing.image_preprocessing import preprocess_image

#nessa fase carrega o modelo treinado
from model.htr_model import recognize_text

#aqui é a função que carrega a métrica de avaliação
from evaluation.metrics import evaluate


#os caminhos para os arquivos de entrada e saída
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
