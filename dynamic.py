import cv2
import process
import recognize

def process_video(video_source=0):
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir le flux vidéo.")
        return

    while True:
        # Lire une frame de la vidéo
        ret, frame = cap.read()
        if not ret:
            print("Fin du flux vidéo.")
            break

        
        frame = cv2.resize(frame, (640, 480))

        
        try:
            # Classifier les tons clairs et foncés
            light_tones, dark_tones = process.classify_tones(frame, n_clusters=2)

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

            # Ajouter le résultat sur la frame
            cv2.putText(frame, f"Chiffre Reconnu : {recognized_digit}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print(f"Erreur dans le traitement : {e}")

        # Afficher la frame en temps réel
        cv2.imshow("Flux vidéo - Reconnaissance de chiffres", frame)

        # Quitter avec la touche Espace
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video(video_source=0)  