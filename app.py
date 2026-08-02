import sys
import os

# Garante que a pasta src/ seja encontrada pelos imports, 
# independente de onde o streamlit for executado
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

import streamlit as st
from PIL import Image

from preprocessing.image_preprocessing import preprocess_image
from model.htr_model import recognize_text
from evaluation.metrics import evaluate

st.set_page_config(page_title="Reconhecimento de Texto Manuscrito", layout="centered")

st.title("Reconhecimento de Texto Manuscrito (HTR)")
st.write("Envie uma imagem manuscrita para o sistema reconhecer o texto.")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg", "webp", "bmp", "gif"])

reference_text = st.text_area(
    "Texto de referência (opcional, para calcular CER/WER)",
    placeholder="Digite aqui o texto real da imagem, se quiser avaliar a precisão..."
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Imagem enviada", use_column_width=True)

    # Salva a imagem enviada temporariamente
    raw_path = "data/raw/temp_upload.png"
    processed_path = "data/processed/temp_upload.png"

    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    image = Image.open(uploaded_file).convert("RGB")
    image.save(raw_path)

    if st.button("Reconhecer texto"):
        with st.spinner("Processando..."):
            preprocess_image(raw_path, processed_path)
            predicted_text = recognize_text(processed_path)

        st.subheader("Texto reconhecido")
        st.write(predicted_text)

        if reference_text.strip():
            metrics = evaluate(predicted_text, reference_text)
            st.subheader("Avaliação")
            st.json(metrics)