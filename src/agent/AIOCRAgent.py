import os
from fastapi import UploadFile
from paddleocr import PaddleOCR

from src.agent import PPaddleOCR, MarkItDownOCR, OnnxOCR, QwenVLOCR
from src.enum.DocTypeEnum import DocTypeEnum
from src.enum.OCREngineEnum import OCREngineEnum
from src.util import FileUtil, ImageUtil
from dotenv import load_dotenv
load_dotenv()
OCR_ENGINE = os.getenv("OCR_ENGINE")

def ocr_file(file: UploadFile, prompt):
    file_path = FileUtil.save_file(file)
    print("# OCR file_path=",file_path)
    doc_type = get_file_type(file_path)
    print(f"# OCR {doc_type} ....")

    context = ""
    if doc_type == DocTypeEnum.IMG.value:
        ImageUtil.resize_image(file_path, file_path, 960)
        if OCR_ENGINE == OCREngineEnum.default.value or OCR_ENGINE == OCREngineEnum.onnxocr.value:
            context = OnnxOCR.ocr(file_path)
        elif OCR_ENGINE == OCREngineEnum.paddleocr.value:
            context = PPaddleOCR.ocr(file_path)
        elif OCR_ENGINE == OCREngineEnum.qwenvl.value:
            context = QwenVLOCR.ocr(file_path, doc_type, prompt)
        else:
            context = OCREngineEnum.notengine


    elif doc_type == DocTypeEnum.PDF.value:
        context = MarkItDownOCR.ocr(file_path)
    elif doc_type == DocTypeEnum.DOCX.value:
        context = MarkItDownOCR.ocr(file_path)
    elif doc_type == DocTypeEnum.XLSX.value:
        context = MarkItDownOCR.ocr(file_path)
    elif doc_type == DocTypeEnum.PPTX.value:
        context = MarkItDownOCR.ocr(file_path)
    else:
        context = DocTypeEnum.PPTX.NOT_SUPPORTED_DOC_TYPE.value
    print("# OCR context=",context)
    return context,file_path


def get_file_type(file_path: str) -> str:
    doc_type = '.' + file_path.split('.')[-1] if '.' in file_path else ''
    if doc_type == '.docx':
        return DocTypeEnum.DOCX.value
    elif doc_type == '.png' or doc_type == '.png' or doc_type == '.jpg' or doc_type == '.jpeg':
        return DocTypeEnum.IMG.value
    elif doc_type == '.pdf':
        return DocTypeEnum.PDF.value
    elif doc_type == '.pdf':
        return DocTypeEnum.PDF.value
    elif doc_type == '.xlsx' or doc_type == '.xls':
        return DocTypeEnum.XLSX.value
    elif doc_type == '.pptx':
        return DocTypeEnum.PPTX.value
    else:
        return "NOT_SUPPORTED_DOC_TYPE"
