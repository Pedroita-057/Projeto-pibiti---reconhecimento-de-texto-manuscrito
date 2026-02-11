import cv2
import os

def preprocess_image(input_path, output_path):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Binarização
    _, image = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Remove ruído leve
    image = cv2.medianBlur(image, 3)

    cv2.imwrite(output_path, image)
