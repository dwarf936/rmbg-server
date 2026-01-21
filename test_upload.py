import base64
import requests
import json

# 读取图片文件并转换为base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()
        base64_str = base64.b64encode(img_data).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_str}"

# 测试图片路径
image_path = "1.jpg"

# 转换图片为base64
base64_image = image_to_base64(image_path)
print(f"图片转换完成，base64长度: {len(base64_image)}")

# 准备请求数据
payload = {
    "base64": base64_image
}

# 发送请求
url = "http://127.0.0.1:3030/run"
headers = {"Content-Type": "application/json"}

print("发送请求中...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    print(f"响应状态码: {response.status_code}")
    print(f"响应内容: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
except Exception as e:
    print(f"请求失败: {str(e)}")
