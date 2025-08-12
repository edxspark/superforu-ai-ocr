import os
import uuid
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


