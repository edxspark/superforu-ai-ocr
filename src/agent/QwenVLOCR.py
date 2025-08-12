
import base64
import os
from src.enum.DocTypeEnum import DocTypeEnum
from src.enum.OCREngineEnum import OCREngineEnum
from src.llm import OllamaLLM, BailianLLM
from src.util import StringUtil, PDFUtil, SysUtil
from dotenv import load_dotenv

load_dotenv()
QWEN_VL_MODEL = os.getenv("QWEN_VL_MODEL")
QWEN_VL_OLLAMA_URL = os.getenv("QWEN_VL_OLLAMA_URL")

project_path_root = SysUtil.get_project_path_root()

def ocr(file_path, doc_type, prompt, ocr_engine):
    context = ""
    if doc_type == DocTypeEnum.IMG.value:
        context = ocr_img(file_path, prompt, ocr_engine)
    elif doc_type == DocTypeEnum.PDF.value:
        context = ocr_pdf(file_path, prompt, ocr_engine)
    else:
        context = DocTypeEnum.PPTX.NOT_SUPPORTED_DOC_TYPE.value
    return context


def ocr_pdf(file_path, prompt, ocr_engine):
    # PDF转图片集
    image_paths,image_directory = PDFUtil.pdf_to_images(file_path)
    # 识别图片内容拼接
    results = []
    index = 1
    pdf_length = len(image_paths)
    for img_path in image_paths:
        img_path_ab =f"{project_path_root}/{img_path}"
        print(f"{index}/{pdf_length}:", img_path_ab)
        result = ocr_img(img_path_ab,"", ocr_engine)
        context = StringUtil.replace_decorate_text(result)
        print(context)
        results.append(context)
        index += 1
    # 删除图片文件夹
    print("#删除图片文件夹")
    os.remove(image_directory)

    return ''.join(results)


def ocr_img(file_path, prompt, ocr_engine):
    prompt_default = """"
    You are a OCR AI, Proficient in extracting image content.
    plsease extract the text content from this image.
    
    # Recognition requirements
    - Only output image content
    
    # Output, do not output introductory or concluding language.
      markdown
    """
    # 1. 读取图片
    img_base64 =None
    with open(file_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    # 2. 设置prompt
    ocr_prompt = prompt_default if prompt == "" else prompt
    print("#img_ocr_prompt:", ocr_prompt)

    # 3. 识别图片
    context = ""
    if ocr_engine == OCREngineEnum.qwenvlollama.qwenvlollama.value:
        context = OllamaLLM.chat_to_img(ocr_prompt,img_base64)
    elif ocr_engine == OCREngineEnum.qwenvlbailian.qwenvlbailian.value:
        context = BailianLLM.chat_to_img(ocr_prompt,img_base64)
    else:
        context = OCREngineEnum.qwenvlbailian.qwenvlbailian.value
    return context



if __name__ == '__main__':
    project_path_root = SysUtil.get_project_path_root()
    img_file_path = f"{project_path_root}/storage/upload/imgs/page_1.jpg"
    result = ocr_img(img_file_path, "",OCREngineEnum.qwenvlbailian)
    print(result)