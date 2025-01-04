import pytesseract
import process

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def recognize_with_tesseract(image):
    """
    Utilise Tesseract pour reconnaître un chiffre dans une image prétraitée.
    """
    # Prétraiter l'image
    processed_image = process.preprocess_for_tesseract(image)

    # Configurer Tesseract pour ne reconnaître que les chiffres
    custom_config = r'--oem 3 --psm 10 digits'
    recognized_text = pytesseract.image_to_string(processed_image, config=custom_config)

    return recognized_text.strip()