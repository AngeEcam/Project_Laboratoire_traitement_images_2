import cv2
import process
import recognize

def main():
    # Charger l'image
    image_path = process.my_Image #change the path in process.py for the images
    image = process.read(image_path)

    # Classifier les tons clairs et foncés
    light_tones, dark_tones = process.classify_tones(image, n_clusters=2)
    # Convertir les tons foncés en binaire
    binary_dark_tones = process.to_binary(dark_tones, threshold=128)
    # Lisser l'image binaire pour améliorer les contours
    smoothed_dark_tones = process.smooth_image(binary_dark_tones, method="morphological", kernel_size=5)
    # Extraire uniquement les contours
    contours_image = process.extract_only_contours(smoothed_dark_tones)
    # Remplir les contours et binariser
    filled_image = process.fill_contours(contours_image)
    # Inverser l'image
    inverted_image = process.invert_image(filled_image)
    # Reconnaître le chiffre avec Tesseract
    recognized_digit = recognize.recognize_with_tesseract(inverted_image)
    # Afficher les résultats
    print(f"Chiffre reconnu : {recognized_digit}")
    process.show(inverted_image, title="Image prête pour Tesseract")

if __name__ == "__main__":
    main()
