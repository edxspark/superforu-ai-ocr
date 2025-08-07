# Superforu AI OCR
AI大模型高质量文档解析OCR   
    支持格式: .jpg、.jpeg、.png、.pdf、.docx、.xlsx、.xls、.pptx   
    返回格式：Markdown

# 开发指南    
```bash

git checkout superforu-ai-ocr
conda create --name superforu-ai-ocr python=3.11
conda activate superforu-ai-ocr
pip install -r requirements.txt
python src/App.py
uvicorn src.App:app --host 0.0.0.0 --port 19108
```
API Docs: http://127.0.0.1:19108/docs


# 大模型识别引擎安装
## Qwen VL
1. 安装Ollama
2. ollama run qwen2.5vl


# Docker 部署
```bash
docker build -t superforu-ai-ocr:1.0.0 .
docker save superforu-ai-ocr:1.0.0 > superforu-ai-ocr.tar
docker load -i superforu-ai-ocr.tar

cd docker
docker compose up -d

```

