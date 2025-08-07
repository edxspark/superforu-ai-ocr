import os
from fastapi import UploadFile
from src.agent import PPaddleOCR, MarkItDownOCR, PPaddleOnnxOCR
from src.venum.DocTypeEnum import DocTypeEnum
from src.util import FileUtil, ImageUtil


def ocr_file(file: UploadFile):
    file_path = FileUtil.save_file(file)
    print("# OCR file_path=",file_path)
    docType = get_file_type(file_path)
    print(f"# OCR {docType} ....")

    context = ""
    if docType == DocTypeEnum.IMG.value:
        ImageUtil.resize_image(file_path, file_path, 960)
        #context = PPaddleOCR.ocr(file_path)
        context = PPaddleOnnxOCR.ocr(file_path)
    elif docType == DocTypeEnum.PDF.value:
        context = MarkItDownOCR.ocr(file_path)
    elif docType == DocTypeEnum.DOCX.value:
        context = MarkItDownOCR.ocr(file_path)
    elif docType == DocTypeEnum.XLSX.value:
        context = MarkItDownOCR.ocr(file_path)
    elif docType == DocTypeEnum.PPTX.value:
        context = MarkItDownOCR.ocr(file_path)
    else:
        context = "NOT_SUPPORTED_DOC_TYPE"
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
