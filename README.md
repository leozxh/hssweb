
---

# SGWeb 自动化测试框架

## 项目简介
SGWeb 是一个基于 Python 的 Web 自动化测试框架，主要用于模拟用户操作（如点击按钮、输入文本等）并验证网页功能的正确性。本框架依赖 Selenium 库与 Chrome 浏览器进行交互，适用于各种 Web 应用的功能测试和 UI 测试。

---

## 环境要求
- **操作系统**：Windows
- **芯片架构**：AMD64
- **Python版本**：3.8 或更高版本
- **命令解释器**：CMD
- **依赖工具**：
  - Selenium (`pip install selenium`)
  - ChromeDriver（需与Chrome浏览器版本匹配）

---

## 安装步骤

### 1. 安装 Python
下载并安装最新版本的 Python：[Python官网](https://www.python.org/downloads/)

### 2. 克隆项目或下载代码
将项目代码克隆到本地或直接下载压缩包。
```bash
git clone <repository_url>
```


### 3. 安装依赖库
在项目根目录下运行以下命令以安装所需依赖：
```bash
pip install -r requirements.txt
```


### 4. 配置 ChromeDriver
- 下载对应版本的 ChromeDriver：[ChromeDriver下载地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- 将 ChromeDriver 放置在系统环境变量中，或者指定路径供 Selenium 使用。

---

## 项目结构
以下是项目的目录结构说明：

```
sgweb/
├── baseView/                # 基础视图模块
│   ├── __init__.py
│   └── baseView.py          # 基础视图类
├── businessView/            # 业务视图模块
│   ├── __init__.py
│   ├── fontpageView.py      # 首页视图类
│   └── signinView.py        # 登录视图类
├── common/                  # 公共模块
│   ├── caps.py              # 能力配置文件
│   ├── common_fun.py        # 公共函数
│   └── elementlibrary.py    # 元素库
├── config/                  # 配置文件目录
│   └── log.conf             # 日志配置文件
├── data/                    # 数据文件目录
│   ├── account.json         # 账户数据
│   ├── email_config.json    # 邮件配置
│   └── env.json             # 环境配置
├── logs/                    # 日志文件目录
│   ├── runlog.log           # 运行日志
│   └── runlog.txt           # 运行日志文本
├── reports/                 # 报告文件目录
│   ├── history.json         # 历史记录
│   └── report.html          # 测试报告
├── run/                     # 运行脚本目录
│   ├── report.py            # 报告生成脚本
│   ├── start.py             # 启动脚本
│   └── screenshots/         # 截图目录
└── README.md                # 项目说明文档
```


### 目录说明
- **baseView**：包含基础视图类，提供通用的页面操作方法。
- **businessView**：包含具体的业务视图类，如首页视图和登录视图。
- **common**：包含公共模块，如能力配置、公共函数和元素库。
- **config**：存放配置文件，如日志配置。
- **data**：存放数据文件，如账户信息、邮件配置和环境配置。
- **logs**：存放运行日志文件。
- **reports**：存放测试报告文件，包括历史记录和 HTML 报告。
- **run**：存放运行脚本，包括报告生成脚本和启动脚本，以及截图目录。

---

## 使用说明

### 运行框架
1. 打开 CMD，进入项目目录。
2. 执行以下命令运行示例脚本：
   ```bash
   python run/start.py
   ```


### 示例功能
- 访问目标网站。
- 定位页面中的指定元素（通过 XPath）。
- 模拟用户点击操作。

> **注意**：确保目标网站已启动且网络连接正常。

---

## 贡献指南
欢迎贡献代码或提出改进建议！请遵循以下步骤：
1. Fork 本项目。
2. 创建新分支：`git checkout -b feature/your-feature-name`。
3. 提交更改并推送至您的仓库。
4. 提交 Pull Request。

---

## 联系方式
如需帮助或反馈问题，请联系项目维护者：zhaxuanhuan@163.com
