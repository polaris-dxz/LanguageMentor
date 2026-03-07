# LanguageMentor 容器化部署（支持本地与 Hugging Face Space）
# Python 版本与 .python-version 保持一致
FROM python:3.12-slim

# Hugging Face Space 要求使用 UID 1000 避免权限问题
RUN useradd -m -u 1000 user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app
USER user

# 依赖
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 应用代码与资源
COPY --chown=user src ./src
COPY --chown=user content ./content
COPY --chown=user prompts ./prompts

# Gradio 默认 7860，HF Space 会映射此端口
ENV GRADIO_SERVER_NAME=0.0.0.0
EXPOSE 7860

# 工作目录为项目根，以便 prompts/、content/ 相对路径正确
WORKDIR $HOME/app
CMD ["python", "src/main.py"]
