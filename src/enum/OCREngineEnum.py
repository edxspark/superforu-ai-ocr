from enum import Enum

class OCREngineEnum(Enum):
    default = "default"
    qwenvl = "qwenvl"
    paddleonnxocr = "paddleonnxocr"
    notengine = "not_engine"
