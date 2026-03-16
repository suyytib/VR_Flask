# 使用官方Python基础镜像
FROM python:3.12.4-slim

# code不需要新建（docker执行时自建）
ADD ./dockerfiles    /code
# 设置code文件夹是工作目录
WORKDIR /code
# 安装依赖
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt
# 将Python脚本复制到容器中
CMD ["python", "/code/app.py"]