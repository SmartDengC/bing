import requests
import json
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
import uvicorn
from py.m_302 import get_bing_image as get_bing_image_302

app = FastAPI(title="必应每日壁纸")

@app.get("/")
def read_root():
    return {"Hello": "http://132.232.242.223:8001/docs#/"}

@app.get("/1366x768")
async def get_small_window_picture():
    """重定向到必应每日壁纸"""
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

@app.get("/1920x1080")
async def get_desktop_image():
    """获取桌面版壁纸(1920x1080)"""
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers, verify=False)
    data = json.loads(response.text)
    img_url = 'https://cn.bing.com' + data["images"][0]["urlbase"] + '_1920x1080.jpg'
    
    if img_url:
        return RedirectResponse(url=img_url)
    else:
        return Response(content="error", media_type="text/plain")

@app.get('/1080x1920')
async def get_phone_bing_image():
    """获取移动端壁纸(302)"""
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
    uvicorn.run(app, host="0.0.0.0", port=8000)