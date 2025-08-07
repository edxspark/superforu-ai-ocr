
import base64
import ollama

from src.enum.DocTypeEnum import DocTypeEnum
from src.util import StringUtil


def ocr(file_path, doc_type, prompt):
    context = ""
    if doc_type == DocTypeEnum.IMG.value:
        context = ocr_img(file_path, prompt)
    elif doc_type == DocTypeEnum.PDF.value:
        context = ocr_pdf(file_path, prompt)
    else:
        context = DocTypeEnum.PPTX.NOT_SUPPORTED_DOC_TYPE.value
    return context


def ocr_pdf(file_path, prompt):
    return ""


def ocr_img(file_path, prompt):
    prompt_default = """"
    Extract the text content from this image.
    # Output
      markdown
    """
    # 1. 读取图片
    img_base64 =None
    with open(file_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    # 2. 设置prompt
    ocr_prompt = prompt
    if prompt == "":
        ocr_prompt = prompt_default
    else:
        ocr_prompt = prompt

    print("#img_ocr_prompt:", ocr_prompt)
    # 3. 识别图片
    response = ollama.chat(
        model="qwen2.5vl:latest",
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



