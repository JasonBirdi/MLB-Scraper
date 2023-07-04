import requests
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Jason/AppData/Local/Programs/Tesseract-OCR'
import io

class ImageProcessor:
    def download_image(self, url):
        response = requests.get(url)
        return Image.open(io.BytesIO(response.content))

    def extract_text(self, image):
        return pytesseract.image_to_string(image)
