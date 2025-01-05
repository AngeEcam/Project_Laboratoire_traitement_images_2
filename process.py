import pytesseract
import cv2
import numpy as np
from sklearn.cluster import KMeans


# Les chemins vers les images doivent être ajustés en fonction de votre répertoire de travail.
#my_Image_2 = r"/Users/spgb/Desktop/Projet_Ishihara/images/Ishihara_2.png"
#my_Image_3 = r"/Users/spgb/Desktop/Projet_Ishihara/images/Ishihara_3.jpg"
#my_Image_5 = r"/Users/spgb/Desktop/Projet_Ishihara/images/Ishihara_5.jpg"
#my_Image_16 = r"/Users/spgb/Desktop/Projet_Ishihara/images/Ishihara_16.jpg"
#my_Image_74 = r"/Users/spgb/Desktop/Projet_Ishihara/images/Ishihara_74.jpg"

#my_Image_2 = r"C:\Users\Simpa\OneDrive\Desktop\Traitement_image\Project_Laboratoire_traitement_images_2\images\Ishihara_2.png"
#my_Image_3 = r"C:\Users\Simpa\OneDrive\Desktop\Traitement_image\Project_Laboratoire_traitement_images_2\images\Ishihara_3.jpg"
#my_Image_5 = r"C:\Users\Simpa\OneDrive\Desktop\Traitement_image\Project_Laboratoire_traitement_images_2\images\Ishihara_5.jpg"
#my_Image_16 = r"C:\Users\Simpa\OneDrive\Desktop\Traitement_image\Project_Laboratoire_traitement_images_2\images\Ishihara_16.jpg"
#my_Image_74 = r"C:\Users\Simpa\OneDrive\Desktop\Traitement_image\Project_Laboratoire_traitement_images_2\images\Ishihara_74.jpg"


my_Image = my_Image_74

def read(img_to_read): 
    image = cv2.imread(img_to_read)
    return image

def classify_tones(image, n_clusters=2):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    value_channel = hsv_image[:, :, 2]
    value_channel = hsv_image[:, :, 2].reshape(-1, 1)  
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(value_channel)
    labels = kmeans.labels_.reshape(hsv_image.shape[:2]) 
    centers = kmeans.cluster_centers_.flatten()
    light_cluster = np.argmax(centers)  
    dark_cluster = 1 - light_cluster    
    light_tones = (labels == light_cluster).astype(np.uint8) * 255
    dark_tones = (labels == dark_cluster).astype(np.uint8) * 255
    return light_tones, dark_tones

def to_binary(image, threshold=128):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


def smooth_image(binary_image, method="median", kernel_size=5):
    if method == "median":
        return cv2.medianBlur(binary_image, kernel_size)
    
    elif method == "gaussian":
        return cv2.GaussianBlur(binary_image, (kernel_size, kernel_size), 0)
    
    elif method == "morphological":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        dilated = cv2.dilate(binary_image, kernel, iterations=1)
        eroded = cv2.erode(dilated, kernel, iterations=1)
        return eroded
    
    else:
        raise ValueError("Méthode inconnue : utilisez 'median', 'gaussian' ou 'morphological'")


def find_and_draw_contours(binary_image, min_contour_area=100):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
    image_with_contours = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_with_contours, filtered_contours, -1, (0, 255, 0), 2)
    return filtered_contours, image_with_contours


def extract_only_contours(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_image = np.zeros_like(binary_image)
    cv2.drawContours(contours_image, contours, -1, 255, 1)  
    return contours_image



def fill_contours(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_image = np.zeros_like(binary_image)
    #cv2.drawContours(filled_image, contours, -1, 0, thickness=cv2.FILLED)
    cv2.drawContours(filled_image, contours, -1, 255, thickness=cv2.FILLED)  # Remplir avec blanc (255)
    _, binarized_image = cv2.threshold(filled_image, 128, 255, cv2.THRESH_BINARY)


    return binarized_image


def invert_image(binary_image):
    inverted_image = cv2.bitwise_not(binary_image)
    return inverted_image


def preprocess_for_tesseract(binary_image):

    # Redimensionner l'image
    resized_image = cv2.resize(binary_image, (300, 300), interpolation=cv2.INTER_LINEAR)

    # Lisser l'image pour uniformiser les contours
    smoothed_image = cv2.GaussianBlur(resized_image, (3, 3), 0)

    # Centrer l'image
    height, width = smoothed_image.shape
    canvas = np.zeros((max(height, width), max(height, width)), dtype=np.uint8)
    x_offset = (canvas.shape[1] - width) // 2
    y_offset = (canvas.shape[0] - height) // 2
    canvas[y_offset:y_offset + height, x_offset:x_offset + width] = smoothed_image

    return canvas

def show(img_to_show, title='image'):
    cv2.imshow(title, img_to_show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

