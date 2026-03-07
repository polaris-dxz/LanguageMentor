# 测试根目录，保证从项目根运行 pytest 时能导入 src 下模块
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

# 运行测试时工作目录设为项目根，以便 prompts/、content/ 等相对路径生效
import os
os.chdir(root)
