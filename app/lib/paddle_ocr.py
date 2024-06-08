import base64
from paddleocr import PaddleOCR
import matplotlib.pyplot as plt
from PIL import Image
import io
import os
import time

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True)


def paddle_ocr_from_base64(image_base64_data: str):
    """
    Perform OCR on an image encoded in Base64 format.

    Args:
        base64_str (str): Base64 encoded image string.

    Returns:
        result: OCR results from PaddleOCR.
    """
    # Decode the base64 string
    img_data = base64.b64decode(image_base64_data)
    img = Image.open(io.BytesIO(img_data))
    start_time = time.perf_counter()
    # Save the image to a temporary file
    temp_img_path = "temp_image.png"
    img.save(temp_img_path)

    # Perform OCR using PaddleOCR
    result = ocr.ocr(temp_img_path, cls=True)
    end_time = time.perf_counter()
    # Delete the temporary file
    os.remove(temp_img_path)
    elapsed_time = end_time - start_time
    return [result, elapsed_time * 1000]
