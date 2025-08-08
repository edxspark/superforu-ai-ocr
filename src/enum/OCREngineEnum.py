from enum import Enum

class OCREngineEnum(Enum):
    default = "default"
    qwenvl = "qwenvl"
    onnxocr = "onnxocr"
    paddleocr = "paddleocr"
    notengine = "not_engine"
