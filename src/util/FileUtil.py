import os
import uuid
from io import BytesIO
from pathlib import Path
import requests
from fastapi import UploadFile
from dotenv import load_dotenv

load_dotenv()
STORAGE_PATH = os.getenv("STORAGE_PATH")


def save_file(file: UploadFile):
    file_name_uuid = str(uuid.uuid4())
    file_dir = f"{STORAGE_PATH}/upload"
    os.makedirs(file_dir, exist_ok=True)
    file_name, file_extension = os.path.splitext(file.filename)
    file_name_new = f"{file_name_uuid}{file_extension}"
    file_save_path = f"{file_dir}/{file_name_new}"
    with open(file_save_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_save_path


def download_pdf(pdf_url: str):
    print("#downloading={}".format(pdf_url))
    response = requests.get(pdf_url, stream=True)
    print("#downloaded.response.status.code={}".format(response.status_code))
    pdf_file_name = os.path.basename(pdf_url)
    filepath = ""
    if response.status_code == 200:
        download_dir = f"{STORAGE_PATH}/download/"
        os.makedirs(download_dir, exist_ok=True)
        filepath = os.path.join(download_dir, pdf_file_name)
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            print(f'#{pdf_file_name} Successfully Downloaded!')
        return True, filepath
    else:
        print(f'#Download Failure： {pdf_file_name}')
        print(f'#Download Failure：HTTP response status code: {response.status_code}')
        return False, filepath


def file_to_upload_file(file_path: str):
    print(f'#file_to_upload_file.file_path： {file_path}')
    file_path = Path(file_path)
    file_content = BytesIO(file_path.read_bytes())
    file = UploadFile(
        filename=file_path.name,
        file=file_content,
    )
    return file

