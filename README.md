# 文件重命名工具-韵网小工具

## 项目概述
本工具提供智能化文件批量重命名解决方案，支持从指定目录自动生成文件列表，并依据文本文件内容进行精准重命名操作。图形界面基于Python Tkinter开发，提供跨平台兼容性。

## 功能特点
- 智能标题爬取生成：自动扫描目录生成有序文件列表
- 批量重命名引擎：支持基于文本文件的批量重命名操作
- 可视化进度反馈：集成进度条和日志窗口实时显示操作状态
- 双模式验证机制：自动校验文件与标题数量匹配
- 操作安全保障：内置异常处理机制和错误提示

## 安装说明
### 源码运行
```bash
pip install -r requirements.txt
python gui_main.py
```

### 可执行文件
1. 下载dist目录下的`文件重命名工具-韵网小工具.exe`
2. 双击运行即可使用

## 使用教程
### 生成文件列表
1. 点击左侧"浏览"按钮选择目标文件夹
2. 点击"生成文件列表"按钮
3. 生成的`files.txt`将保存在目标目录

### 批量重命名
1. 右侧选择需要重命名的目标文件夹
2. 选择包含标题的txt文件
3. 点击"开始重命名"按钮
4. 在日志区域查看实时操作记录

## 注意事项
❗ 重命名操作不可逆，建议提前备份重要文件
❗ 确保标题文件与目标文件夹文件数量严格一致
❗ 支持常见格式

## 版权声明
© 2025 韵网科技 保留所有权利
遵循MIT开源协议，欢迎二次开发使用
