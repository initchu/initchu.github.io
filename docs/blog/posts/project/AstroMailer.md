---
title: AstroMailer 一个每日早安邮件发送器
authors: [chuchengzhi]
tags: 
    - project
date: 2024-12-17 00:00:00
categories:
  - project
---

# AstroMailer 🌌

**AstroMailer** 是一个**每日早安邮件发送器**，它通过集成 **NASA 天文每日一图（APOD）、词霸金句和百度翻译 API**，为用户带来浪漫、温暖的早安邮件。

github地址: [AstroMailer](https://github.com/initchu/AstroMailer)

## 功能概述

- 📧 **每日发送早安邮件**
    - 附带 **NASA** 天文每日一图及其解释。
    - 包含词霸**每日金句**（中英双语）。
    - 邮件支持**中英文翻译**，并使用简洁优雅的 **HTML** 样式设计。
- 🌌 **随机背景色和样式**
    - 邮件中的句子和背景配色采用动态随机生成，让每一天的邮件都有独特的风格。
    - 🔄 **缓存**机制
	 - 使用 **diskcache** 缓存 **NASA** 图片和内容，减少重复 API 请求。

## 项目架构

**AstroMailer** 的主要功能分为以下模块：

1. **邮件发送模块**
    - 使用 smtplib 实现邮件的发送。
	 - 支持 HTML 格式化邮件内容。
2. **API 调用模块**
    - 集成 NASA APOD API 获取每日天文图片和描述。
    - 集成百度翻译 API 翻译图片描述为中文。
    - 使用词霸 API 获取每日金句。
3. **定时任务模块**
    - 使用 schedule 实现每天早上 8 点自动发送邮件。
4. **缓存模块**
    - 使用 diskcache 缓存数据，避免频繁调用 API。

## 运行截图

📧 邮件示例    

![](https://initchu.oss-cn-hangzhou.aliyuncs.com/2024/12/18/17345141645606.jpg)

## 技术栈

- 编程语言: Python 3.10+
- 主要依赖:
    - smtplib: 发送邮件
    - schedule: 定时任务调度
    - diskcache: 本地缓存
    - requests: 调用 API
    - PyYAML: 解析配置文件
    
- API:
    - [NASA APOD API](https://api.nasa.gov/)
    - [百度翻译 API](https://fanyi-api.baidu.com/)
    - [词霸 API](https://open.iciba.com/dsapi/)

## 安装与运行

**1. 克隆项目**

```bash
git clone https://github.com/initchu/AstroMailer.git
cd AstroMailer
```

**2. 创建虚拟环境并安装依赖**

```bash
# 创建虚拟环境
python3 -m venv myvenv

# 激活虚拟环境
source myvenv/bin/activate  # macOS/Linux
myvenv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

**3. 配置环境**

在 `resources/config.yaml` 文件中配置你的 `API` 密钥和邮件账户信息。

示例配置文件 `config.yaml`：

```yaml
api_key:
  nasa: "你的NASA_API_KEY"
  baidu_translate:
    appid: "你的百度翻译APPID"
    secret_key: "你的百度翻译SECRET_KEY"

email:
  name: "AstroMailer"
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  sender: "your_email@example.com"
  password: "your_email_password"
  recipients:
    - "recipient1@example.com"
    - "recipient2@example.com"
```

**4. 启动服务**

直接运行

```bash
python src/main.py
```

docker

```bash
docker-compose up -d
```

## 贡献指南

欢迎贡献代码！如果你想为 **AstroMailer** 提交新的功能或修复 bug，请按照以下步骤操作：

1. Fork 仓库。
2. 创建新分支：

```bash
git checkout -b feature/your-feature-name
```

3. 提交代码并创建 Pull Request。

## 开源协议

本项目采用 [Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0)。

---

感谢使用 AstroMailer，让宇宙的浪漫点亮你的每一天！✨
