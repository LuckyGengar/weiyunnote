# weiyunnote
A Python code for fetching Tencent Weiyun shared notes.  
用于提取微云笔记内容的Python代码

### 依赖安装
```bash
pip install requests beautifulsoup4
```

### 使用方法
```Python
from weiyunnote import get_weiyun_note

get_weiyun_note(url, password="", only_title=False)
```
| 参数         | 类型   | 默认值   | 说明                                                          |
| :----------- | :----- | :------- | :------------------------------------------------------------ |
| `url`        | `str`  | **必填** | 微云笔记的分享链接 (例如 `https://share.weiyun.com/FsonvDt7`) |
| `password`   | `str`  | `""`     | 如果笔记设置了访问密码，请在此填入                            |
| `only_title` | `bool` | `False`  | 设为 `True` 则只返回笔记标题，不返回正文                      |