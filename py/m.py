import requests
import json
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

@app.get("/")
async def get_bing_image():
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    headers = {
        "Accept": "application/json"
    }
    
    # 发送请求获取必应图片信息
    response = requests.get(url, headers=headers, verify=False)
    data = json.loads(response.text)
    
    # 构建完整图片URL
    img_url = 'https://cn.bing.com' + data["images"][0]["urlbase"] + '_1080x1920.jpg'
    
    if img_url:
        # 获取图片内容
        img_response = requests.get(img_url, verify=False)
        img_data = io.BytesIO(img_response.content)
        
        # 直接返回图片内容
        return StreamingResponse(img_data, media_type="image/jpeg")
    else:
        return Response(content="error", media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)