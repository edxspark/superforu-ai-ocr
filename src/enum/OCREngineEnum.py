from enum import Enum

class OCREngineEnum(Enum):
    qwenvlollama = "qwenvl_ollama"
    qwenvlbailian = "qwenvl_bailian"
    paddleonnxocr = "paddleonnxocr"
    notengine = "not_engine"
