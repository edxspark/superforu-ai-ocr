
from paddleocr import PaddleOCR

def ocr(file_path):
    context = ""
    paddleocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False)
    result = paddleocr.predict(file_path)

    for res in result:
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")

    texts = result[0]["rec_texts"]
    for text in texts:
        context = context + text + " "
    return context

if __name__ == "__main__":
    ocr_result = ocr("test01.png")
    print(ocr_result)