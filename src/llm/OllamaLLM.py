import os
from dotenv import load_dotenv
from ollama import Client
from src.util import StringUtil

load_dotenv()
QWEN_VL_MODEL = os.getenv("QWEN_VL_MODEL")
QWEN_VL_OLLAMA_URL = os.getenv("QWEN_VL_OLLAMA_URL")

def chat_to_img(ocr_prompt,img_base64):
    # 3. 识别图片
    response = Client(
        host=QWEN_VL_OLLAMA_URL
    ).chat(
        model=f"{QWEN_VL_MODEL}",
        messages=[
            {
                "role": "user",
                "content": ocr_prompt,
                "images": [img_base64]
            }
        ]
    )
    rt_context = response["message"]["content"]
    return StringUtil.replace_decorate_text(rt_context)