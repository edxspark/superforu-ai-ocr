#!/usr/bin/venv python
import os
import sys
from typing import Optional

from src.enum.DocTypeEnum import DocTypeEnum

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import AIOCRAgent
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Superforu AI OCR",
    version="1.2.1",
    description="""
    为AI大模型提供高质量文档解析能力
    支持格式: .jpg、.jpeg、.png、.pdf、.docx、.xlsx、.xls、.pptx
    返回格式：Markdown
    """,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Upload file
@app.post("/ai/ocr")
def ocr_file(file: UploadFile = File(...), prompt: Optional[str] = ""):
    print("#####ocr_file BEG")
    rt = None
    file_path = None
    try:
        result,file_path = AIOCRAgent.ocr_file(file, prompt)
        if result == DocTypeEnum.PPTX.NOT_SUPPORTED_DOC_TYPE.value:
            rt = {"status":"01","result":result}
        else:
            rt = {"status": "00", "result": result}
    except Exception as e:
        print(e)
        rt = {"status":"02","result":"ERROR"}
    finally:
        print(f"#####remove file:{file_path}")
        os.remove(file_path)
    print("#####ocr_file END")
    return rt


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=19108)
