import cv2
import numpy as np
from onnxocr.onnx_paddleocr import ONNXPaddleOcr
model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)

def ocr(file_path):
    img = cv2.imread(file_path)
    result = model.ocr(img)
    ocr_results = []
    for line in result[0]:
        # 确保 line[0] 是 NumPy 数组或列表
        if isinstance(line[0], (list, np.ndarray)):
            # 将 bounding_box 转换为 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] 格式
            bounding_box = np.array(line[0]).reshape(4, 2).tolist()  # 转换为 4x2 列表
        else:
            bounding_box = []

        ocr_results.append({
            "text": line[1][0],  # 识别文本
            "confidence": float(line[1][1]),  # 置信度
            "bounding_box": bounding_box  # 文本框坐标
        })

    return ocr_results
