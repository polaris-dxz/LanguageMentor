# LanguageMentor

LanguageMentor 是一款基于 LLaMA 3.1 或 GPT-4o-mini 的在线英语私教系统，提供英语对话练习和场景化学习训练。用户可以选择不同的场景，或直接与对话代理人进行自由对话，模拟真实生活中的英语交流场景，提升语言能力。

## 产品设计

- 核心功能：
  - 基础教学：涵盖词汇积累、语法学习、阅读理解和写作技巧等基础内容。
  - 对话式训练：模拟真实场景的对话练习，提升学生的口语表达能力和听力理解能力。
- 用户学习路径：
  - 初学者：注重词汇和基础语法的学习，通过简单对话练习提高自信心。
  - 中级学员：结合复杂语法和高级词汇，进行更深入的阅读和写作训练。
  - 高级学员：重点练习口语和听力，通过模拟真实场景的对话提升实战能力。
- 课程设计：
  - 词汇积累：采用词根词缀法和常用词汇表，帮助学生高效记忆单词。
  - 语法学习：通过系统的语法讲解和练习，夯实学生的语法基础。
  - 阅读理解：提供不同难度的阅读材料，训练学生的阅读速度和理解能力。
  - 写作技巧：指导学生如何进行段落和文章的结构化写作。

## 产品演示

https://github.com/user-attachments/assets/6298a8e4-28fc-4a60-badc-59bff16b315e

## 快速开始

以下是快速开始使用 LanguageMentor 的步骤：

1. **克隆仓库**

   ```bash
   git clone https://github.com/DjangoPeng/LanguageMentor.git
   cd LanguageMentor
   ```

2. **创建 Python 虚拟环境**
   使用 miniconda 或类似 Python 虚拟环境管理工具，创建一个项目专属的环境，取名为`lm`：

   ```bash
   conda create -n lm python=3.12
   ```

   激活虚拟环境

   ```bash
   conda activate lm
   ```

3. **配置开发环境**
   然后运行以下命令安装所需依赖：

   ```bash
   pip install -r requirements.txt
   ```

   根据需要配置你的环境变量，例如 `OpenAI_API_KEY` 等。

   **使用 uv（推荐）**
   若已安装 [uv](https://github.com/astral-sh/uv)，可在项目根目录执行：

   ```bash
   uv venv                    # 创建虚拟环境 .venv
   source .venv/bin/activate  # 激活（Windows: .venv\Scripts\activate）
   uv pip install -r requirements.txt
   ```

   项目内已配置 `uv.toml` 使用清华镜像，安装更快。之后运行应用同下。

4. **运行应用**
   启动应用程序：

   ```bash
   python src/main.py
   ```

5. **开始体验**
   打开浏览器，访问 `http://localhost:7860`，开始跟着 LanguageMentor 一起学习英语！

### 故障排除：Pillow 安装失败（找不到 jpeg）

若安装依赖时出现 `The headers or library files could not be found for jpeg`，说明 Pillow 在从源码编译时缺少系统库。可任选其一：

- **推荐**：使用 Python 3.10～3.12（项目推荐 3.12，与 `.python-version` 一致），这些版本通常有 Pillow 预编译包，无需编译。
- **从源码编译时**：在 macOS 上需先安装 libjpeg，再安装依赖：

  ```bash
  brew install jpeg
  pip install -r requirements.txt
  ```

  若 `brew install` 报权限错误，需先修复 Homebrew 目录权限（需输入密码）：

  ```bash
  sudo chown -R $(whoami) /opt/homebrew /Users/duxizhi/Library/Logs/Homebrew
  ```

   运行画面：
   ![gradio_demo](images/gradio.png)

   对话练习：
   ![gradio_demo_0](images/gradio_0.png)
   ![gradio_demo_1](images/gradio_1.png)

## 单元测试

项目包含单元测试与覆盖率要求（目标 80%），便于开发与 CI 使用。

1. **安装开发依赖**

   ```bash
   pip install -r requirements-dev.txt
   ```

2. **运行测试与覆盖率**

   ```bash
   # 推荐：使用脚本（在项目根目录执行）
   bash scripts/run_tests.sh
   ```

   或直接使用 pytest：

   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
   python -m pytest tests/ -v --cov=src --cov-report=term-missing --cov-fail-under=80
   ```

   覆盖率报告会输出到终端；另可生成 HTML 报告：`--cov-report=html`，查看 `htmlcov/index.html`。

## Docker 构建与容器化部署

使用 Docker 可在本机或服务器一键运行，无需单独配置 Python 环境。

1. **构建镜像**（在项目根目录执行）

   ```bash
   docker build -t language-mentor .
   ```

2. **运行容器**

   ```bash
   docker run -p 7860:7860 language-mentor
   ```

   访问 http://localhost:7860。如需使用本地 Ollama 模型，可挂载 socket 并设置环境变量，例如：

   ```bash
   docker run -p 7860:7860 -e OLLAMA_MODEL=deepseek-r1:latest --add-host=host.docker.internal:host-gateway language-mentor
   ```

   （若 Ollama 运行在宿主机，需在容器内配置可访问的 Ollama 地址。）

## 发布到 Hugging Face Space

便于学术交流与分享，可将 LanguageMentor 以 Docker 形式发布到 [Hugging Face Spaces](https://huggingface.co/spaces)。

1. **创建 Space**
   - 登录 [Hugging Face](https://huggingface.co)，进入 [Create new Space](https://huggingface.co/new-space)。
   - 选择 **Docker** 作为 SDK，填写 Space 名称与可见性。

2. **推送代码**
   - 将本仓库克隆到本地（若尚未克隆），确保包含 `Dockerfile`、`requirements.txt`、`src/`、`content/`、`prompts/`。
   - 在 Space 仓库中，将 README 的 YAML 头设置为 Docker 并指定端口（或直接使用仓库内的 `README_HF_SPACE.md` 内容作为 Space 的 README）：
     ```yaml
     ---
     title: LanguageMentor
     emoji: 🎓
     sdk: docker
     app_port: 7860
     ---
     ```
   - 将本地代码推送到该 Space 仓库（`git push` 到 `https://huggingface.co/spaces/<你的用户名>/<Space 名>`）。

3. **构建与运行**
   - Space 会根据 `Dockerfile` 自动构建并运行，构建完成后即可在浏览器中打开 Space 链接使用。
   - 若需使用 Ollama 等外部模型，可在 Space 的 **Settings → Variables and secrets** 中配置环境变量（如 `OLLAMA_MODEL`、Ollama 服务地址等）。

4. **分享**
   - 将 Space 链接分享给他人即可体验，便于课程演示或论文复现。

## 贡献

欢迎对本项目做出贡献！你可以通过以下方式参与：

- 提交问题（Issues）和功能请求
- 提交拉取请求（Pull Requests）
- 参与讨论和提供反馈

## 许可证

本项目采用 Apache 2.0 许可证，详情请参阅 [LICENSE](LICENSE) 文件。
