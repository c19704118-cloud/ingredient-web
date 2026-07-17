肤质分析小工具
基于python FLASk开发的护肤品成分检测网页
功能特点：
1.粉白径向渐变星星背景，柔和美丽
2.中间功能框完全独立，不影响操作
3.支持中英文护肤品成分识别，自动分析油敏肌适配性

本地运行教程：
1. 安装依赖库
   bash
   pip install flask
2.启动项目：python app.py
3.浏览器访问地址：http://127.0.0.1:5000
项目文件结构：
ingredient_web
├─ app.py              # 后端逻辑代码
├─ static/style.css    # 页面渐变、星星背景样式
└─ templates/index.html # 前端网页框架

点击 **Commit changes** 保存文档，注意：
1. 文件夹名称必须是 `static` 和 `templates`，大小写不能写错，否则网页样式失效
2. 拖拽上传时，不要直接拖整个大文件夹，分开拖拽单个文件、两个子文件夹
3. 全部上传完成后，仓库主页就能看到完整项目代码
