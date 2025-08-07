from enum import Enum


class DocTypeEnum(Enum):
    PDF = "PDF"
    IMG = "IMG"
    DOCX = "DOCX"
    XLSX = "XLSX"
    PPTX = "PPTX"
    NOT_SUPPORTED_DOC_TYPE = "NOT_SUPPORTED_DOC_TYPE"
