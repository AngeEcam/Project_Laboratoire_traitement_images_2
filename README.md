# Project: Ishihara Image Recognition

This project aims to recognize numbers contained in Ishihara test images, a test commonly used to detect color blindness. Using image processing techniques (OpenCV) and OCR (Tesseract), this project processes images, extracts numbers, and recognizes them automatically. It also supports video streams for real-time recognition.

---

## **Features**
- **Ishihara Image Processing**:
  - Classification of light and dark tones.
  - Contour extraction and binarization of numbers.
  - Smoothing and color inversion to prepare data for OCR.
- **Number Recognition**:
  - Using Tesseract OCR to identify extracted numbers.
- **Video Stream**:
  - Real-time number recognition from a video or camera.

---

## **Installation**

### **1. Prerequisites**
- **Python 3.12** (or compatible version)
- **Tesseract OCR**
  - Install Tesseract OCR based on your operating system:
    - **macOS**: `brew install tesseract`
    - **Ubuntu/Linux**: `sudo apt install tesseract-ocr`
    - **Windows**: Download from [Tesseract Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki).

### **2. Python Environment Setup**
1. **Clone this repository or copy the files to a local directory**:
   ```bash
   git clone <project_url>
   cd <folder_name>
   ```
2. **Create a Python virtual environment**:
   ```bash
   python -m venv Ishihara
   ```
3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     Ishihara\Scripts\Activate
     ```
   - **macOS/Linux**:
     ```bash
     source Ishihara/bin/activate
     ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Verify Tesseract setup**:
   Ensure Tesseract is in your PATH (Windows only) and that its path is correctly set in `recognize.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

---

## **Usage**

### **1. Image Recognition**
To recognize a number in an Ishihara image, modify the path in `process.py` or `main.py` and run:
```bash
python main.py
```

### **2. Video Stream Recognition**
To perform real-time recognition from a camera or video file:
1. Enable the camera by modifying `video_source` in `main.py`:
   ```python
   process_video(video_source=0)  # 0 for camera or path to a video file
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Press Space to exit the video stream.

---

## **Project Structure**
```
Ishihara_Project/
│
├── main.py           # Main script to run the project
├── process.py        # Contains image processing functions
├── recognize.py      # Implements recognition using Tesseract OCR
├── requirements.txt  # List of required dependencies
├── README.md         # Project documentation
├── config.py         # (Optional) Configuration paths
└── images/           # Contains Ishihara test images
```

---

## **Dependencies**
Install the following Python libraries (already included in `requirements.txt`):
- `numpy`
- `opencv-python`
- `pytesseract`
- `scikit-learn`

---

## **Limitations**
- The quality of results strongly depends on the clarity of the image and the preprocessing accuracy.
- Tesseract may struggle with poorly formed numbers or irregular contours.

---

## **Contributions**
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.