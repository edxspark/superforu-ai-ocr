
from markitdown import MarkItDown

def ocr(file_path):
    md = MarkItDown()
    result = md.convert(file_path)
    context = result.text_content
    return context