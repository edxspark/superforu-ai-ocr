import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
QWEN_VL_BAILIAN_BASE_URL = os.getenv("QWEN_VL_BAILIAN_BASE_URL")
QWEN_VL_BAILIAN_API_KEY = os.getenv("QWEN_VL_BAILIAN_API_KEY")
QWEN_VL_BAILIAN_MODEL = os.getenv("QWEN_VL_BAILIAN_MODEL")


def chat_to_img(ocr_prompt,img_base64):
    print("BailianLLM.chat_to_img")
    client = OpenAI(
        api_key=QWEN_VL_BAILIAN_API_KEY,
        base_url=QWEN_VL_BAILIAN_BASE_URL
    )

    response = client.chat.completions.create(
        model=QWEN_VL_BAILIAN_MODEL,
        messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{ocr_prompt}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content