from pathlib import Path

import fitz
import os


def pdf_to_images(pdf_file_path: str):
    pdf_file_name = Path(pdf_file_path).stem
    pdf_save_dir = os.path.dirname(pdf_file_path)
    image_directory = f"{pdf_save_dir}/{pdf_file_name}_imgs"
    os.makedirs(image_directory, exist_ok=True)

    pdf = fitz.open(pdf_file_path)
    image_paths = []
    for page_number in range(len(pdf)):
        page = pdf[page_number]
        pix = page.get_pixmap()
        image_file_path = f'{image_directory}/page_{page_number + 1}.jpg'
        image_paths.append(image_file_path)
        pix.save(image_file_path)
    return image_paths,image_directory
