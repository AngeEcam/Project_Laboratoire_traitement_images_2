# Projet : Reconnaissance d'Images Ishihara

Ce projet vise à reconnaître des chiffres contenus dans des images du test Ishihara, un test couramment utilisé pour détecter le daltonisme. Grâce à des techniques de traitement d'image (OpenCV) et à l'OCR (Tesseract), ce projet traite les images, extrait les chiffres, et les reconnaît automatiquement. Il prend également en charge un flux vidéo pour une reconnaissance en temps réel.

---

## **Fonctionnalités**
- **Traitement des images Ishihara** :
  - Classification des tons clairs et foncés.
  - Extraction et binarisation des contours des chiffres.
  - Lissage et inversion des couleurs pour préparer les données pour l'OCR.
- **Reconnaissance des chiffres** :
  - Utilisation de Tesseract OCR pour identifier les chiffres extraits.
- **Flux vidéo** :
  - Reconnaissance de chiffres en temps réel à partir d'une vidéo ou de la caméra.

---

## **Installation**

### **1. Prérequis**
- **Python 3.12** (ou version compatible)
- **Tesseract OCR**
  - Installez Tesseract OCR selon votre système d'exploitation :
    - **macOS** : `brew install tesseract`
    - **Ubuntu/Linux** : `sudo apt install tesseract-ocr`
    - **Windows** : Téléchargez depuis [Tesseract Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki).

### **2. Configuration de l'environnement Python**
1. **Clonez ce dépôt ou copiez les fichiers dans un répertoire local** :
   ```bash
   git clone <URL_du_projet>
   cd <Nom_du_dossier>
   ```
2. **Créez un environnement virtuel Python** :
   ```bash
   python -m venv Ishihara
   ```
3. **Activez l'environnement virtuel** :
   - **Windows** :
     ```bash
     Ishihara\Scripts\Activate
     ```
   - **macOS/Linux** :
     ```bash
     source Ishihara/bin/activate
     ```
4. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
5. **Vérifiez que Tesseract est correctement configuré** :
   Assurez-vous que Tesseract est dans votre PATH (Windows uniquement) et que son chemin est correctement défini dans `recognize.py` :
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

---

## **Utilisation**

### **1. Reconnaissance d'une image**
Pour reconnaître un chiffre dans une image Ishihara, modifiez le chemin dans `process.py` et exécutez :
```bash
python static.py
```

### **2. Reconnaissance via flux vidéo**
Pour effectuer la reconnaissance en temps réel depuis une caméra ou un fichier vidéo :
1. Activez la caméra en modifiant le `video_source` dans `dynamic.py` :
   ```python
   process_video(video_source=0)  # 0 pour la caméra ou chemin vers une vidéo
   ```
2. Exécutez le script :
   ```bash
   python main.py
   ```
3. Appuyez sur Espace pour quitter le flux vidéo.

---

## **Structure du projet**
```
Projet_Ishihara/
│
├── main.py           # Script principal pour exécuter le projet
├── process.py        # Contient les fonctions de traitement d'image
├── recognize.py      # Implémente la reconnaissance via Tesseract OCR
├── requirements.txt  # Liste des dépendances nécessaires
├── README.md         # Documentation du projet
└── images/           # Contient les images de test Ishihara
```

---

## **Dépendances**
Installez les bibliothèques Python suivantes (déjà incluses dans `requirements.txt`) :
- `numpy`
- `opencv-python`
- `pytesseract`
- `scikit-learn`

---

## **Limitations**
- La qualité des résultats dépend fortement de la clarté de l'image et de la précision du prétraitement.
- Tesseract peut avoir des difficultés à reconnaître des chiffres mal formés ou avec des contours irréguliers.
```