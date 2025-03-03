import requests
import json
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

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
        # 重定向到图片URL
        return RedirectResponse(url=img_url)
    else:
        return Response(content="error", media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)