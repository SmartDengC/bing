# Bing Picture

必应照片

## 一、简单快速部署 

将文件夹压缩后，并推送到服务器

```shell
zip -r bing.zip bing -x "./bing/.venv/*"
```

服务器目录结构：

```shell
.
├── app
│   ├── main.py
│   ├── php
│   ├── py
│   ├── README.md
│   └── requirements.txt
├── Dockerfile
└── requirements.txt
```

Dockerfile内容：

```dockerfile
# 从官方Python基础镜像开始
FROM python:3.9

# 将当前工作目录设置为/code
WORKDIR /code

# 将符合要求的文件复制到/code目录中
COPY ./requirements.txt /code/requirements.txt

# 安装需求文件的包依赖项
# --no-cache-dir 表示pip不要在本地保存下载的包，因为只有当pip再次运行以安装相同的包时才会这样，但在与容器一起工作时情况并非如此
# --upgrade 表示告诉pip升级软件包，如果已经安装
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 将./app目录复制到/code目录中
# 由于其中包含更改最频繁的所有代码，因此docker缓存不会疫情用于此操作或者任何后续步骤，因此，将其放在Dockerfile接近最后的位置非常重要，以优化容器镜像的构建时间
COPY ./app /code/app

# 设置命令来运行uvicorn服务区，CMD接受一个字符串列表，每个字符串都是你在命令行中输入的内容，并用空格分割
# 该命令将从当前工作目录运行，即你上面使用WORKDIR /code设置的同一/code目录
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

requirements.txt内容

```shell
annotated-types==0.7.0
anyio==4.8.0
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
dnspython==2.7.0
email_validator==2.2.0
exceptiongroup==1.2.2
fastapi==0.115.11
fastapi-cli==0.0.7
h11==0.14.0
httpcore==1.0.7
httptools==0.6.4
httpx==0.28.1
idna==3.10
Jinja2==3.1.5
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
pydantic==2.10.6
pydantic_core==2.27.2
Pygments==2.19.1
python-dotenv==1.0.1
python-multipart==0.0.20
PyYAML==6.0.2
requests==2.32.3
rich==13.9.4
rich-toolkit==0.13.2
shellingham==1.5.4
sniffio==1.3.1
some-package==0.1
starlette==0.46.0
typer==0.15.2
typing_extensions==4.12.2
urllib3==2.3.0
uvicorn==0.34.0
uvloop==0.21.0
watchfiles==1.0.4
websockets==15.0
```

构建docker镜像

```shell
docker build -t bing-py .
```

运行docker容器

```shell
docker run --name bing -p 8001:8000 -itd bing-py
```

## 二、访问地址

运行之后就可以使用 
