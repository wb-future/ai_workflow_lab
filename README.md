# ai_workflow_lab

AI 编程与机器人学习实践项目。

本项目用于记录 50 个学习日的 Python、AI 编程、机器学习、强化学习及机器人相关实践。每天的练习代码独立保存，完成后通过 Git 提交并同步到 GitHub，以便持续记录学习过程和代码版本。

## 项目环境

- 操作系统：Ubuntu 24.04（WSL）
- 开发工具：Visual Studio Code
- 编程语言：Python 3
- 版本控制：Git
- 代码托管：GitHub
- Python 运行环境：WSL Ubuntu 自带的 Python 3
- 当前阶段：D01–D10 使用现有 `python3` 学习标准库
- 环境管理计划：D13 学习 Miniforge/Mamba，目前尚未创建项目虚拟环境

## 文件结构

```text
ai_workflow_lab/
├── lessons/
│   └── day01.py       # D01 练习草稿，尚未正式验收
├── hello.py           # 本地练习文件，暂不纳入首次 Git 提交
├── README.md          # 项目说明文档
└── .gitignore         # Git 忽略规则
```

说明：

- `lessons/`：存放每天独立编写的学习代码。
- `day01.py`：第一天的 Python 基础练习。
- `hello.py`：最初的 Python 入门程序。
- `README.md`：记录项目目标、环境及运行方法。
- `.gitignore`：指定 Git 不需要跟踪的文件和目录。
- `.venv/`：未来可能创建的本地 Python 虚拟环境，已在 `.gitignore` 中设置忽略规则。

## 开发环境

本项目在 WSL Ubuntu 24.04 环境下开发，使用 VS Code 连接 WSL 进行代码编辑和运行。

在 VS Code 中打开项目后，使用 Ubuntu 终端执行 Python 程序。

查看 Python 版本：

```bash
python3 --version
```

查看 Python 解释器路径：

```bash
which python3
```

## 运行 Python 程序

确保终端当前目录为项目根目录 `ai_workflow_lab/`。

### 1. 运行初始程序

```bash
python3 hello.py
```

### 2. 运行第一天学习练习

```bash
python3 lessons/day01.py
```

本项目当前入门练习主要使用 Python 标准库，不需要安装第三方依赖。

## 验证结果

初始程序 `hello.py` 应输出三项内容：

1. 欢迎信息。
2. 当前 Python 版本。
3. 电脑本地当前日期和时间。

实际输出取决于运行环境和本地系统时间。

运行结束后，可以通过以下命令检查程序退出码：

```bash
echo $?
```

正常结束时退出码为：

```text
0
```

## 每日学习与代码管理

本项目采用每天独立编写、运行验证、Git 提交和 GitHub 同步的学习方式。

每日基本流程：

1. 学习当天的 Python 或 AI 相关知识。
2. 在 `lessons/` 目录中创建当天独立的 Python 文件。
3. 自己编写代码，不只依赖复制现成代码。
4. 在 Ubuntu 终端运行程序。
5. 检查输出结果，完成当天练习。
6. 使用 Git 提交当天的代码和相关文档。
7. 将本地提交同步到 GitHub。

每日代码文件命名规则：

```text
lessons/day01.py
lessons/day02.py
lessons/day03.py
...
lessons/day50.py
```

## 项目学习目标

通过 50 个学习日的持续实践，逐步掌握：

- Python 编程基础与工程开发能力。
- Git、GitHub 和代码版本管理。
- NumPy 与 PyTorch 深度学习基础。
- DQN、PPO、SAC 等强化学习算法。
- MuJoCo 机器人仿真。
- Diffusion Policy 及机器人策略学习。
- AI 编程工具、Skills、MCP 等开发技术。

最终目标是具备独立阅读、编写、运行、调试和修改 AI 与机器人相关代码的能力。

---

## 作者与维护者

- 作者（Author）：wb
- 维护者（Maintainer）：wb
- 项目性质：个人 AI 编程与机器人技术学习项目
- AI 辅助工具：ChatGPT、Codex（用于教学、解释和代码审查）

**项目原则：每天学习、独立编码、运行验证、Git 提交、GitHub 备份。**