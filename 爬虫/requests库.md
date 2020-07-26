# requests库

`requests.request()`构造一个请求

`requests.get()` 获取HTML网页的主要方法

`requests.head()`获取HTML的头信息

`requests.post()`向HTML提交POST

`requests.put()`向HTML 提交PUT

`requests.patch()`向HTML提交局部修改请求

`requests.delete()`向HTML提交删除请求

## `GET`

```python
import requests
# 访问百度网页
r = requests.get('http://www.baidu.com')
# 查看状态码
r.status_code # 200 代表成功
 
r.encoding = 'utf-8'

r.text
```

## 通用代码框架

```go
# 通用框架
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态码不是200， 引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
```

这样保证了请求的正确，如果发生异常会返回

## Robots协议

告知爬虫什么内容可以爬取

### 遵守方式

 自动识别robot.txt