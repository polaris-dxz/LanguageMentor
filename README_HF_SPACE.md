---
title: LanguageMentor
emoji: 🎓
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# LanguageMentor

在线英语私教：场景对话、自由对话与词汇学习。运行于 Docker，支持 Hugging Face Space。

## 本地运行

```bash
docker build -t language-mentor .
docker run -p 7860:7860 language-mentor
```

访问 http://localhost:7860。

## 说明

- 默认使用 Ollama 本地模型（需在 Space 或本机配置 `OLLAMA_MODEL` 等环境变量）。
- 在 Hugging Face Space 部署时，可在 Space 设置中配置变量与密钥。
