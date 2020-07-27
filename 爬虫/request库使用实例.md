# 实例

## 爬取京东商品页面

```python
# 实例一， 爬取京东页面商品
import requests

# 使用框架
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)       
    except:
        print("链接未成功")
    
url = "https://item.jd.com/2967929.html"

url2 = "http://www.baidu.com"
getHTML(url)
getHTML(url2)
```

## 爬取亚马逊网站商品信息

```python
url3 = "https://www.amazon.cn/dp/B07KK8LT9V/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=iphone&qid=1595771749&sr=8-1"
getHTML(url3)# 链接未成功 ？？？
```

产生了错误，主要是网站对头信息检查是否是来自浏览器的请求

### 模拟一个浏览器

```python
kv = {"User-Agent" : "Mozilla/5.0"}
r = requests.get(url3, headers=kv)
r.status_code # 200
r.text
```

访问成功

整合代码

```python
def getHTMLmodel(url):
    try:
        kv = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except:
        print("链接未成功")

```

## 百度搜索关键词提交

百度提供了接口

> http://www.baidu.com/s?wd=keyword

只要替换`keyword`基于可以实现向百度提交关键词

```python
wd = {"wd" : "python"}
r = requests.get("http://www.baidu.com/s", 
                 params=wd)
r.status_code #200
r.request.url # 'http://www.baidu.com/s?wd=python'
len(r.text) # 564276 返回地很大

# 整合代码
def getHTMLkv(url, keyword):
    try:
        kv = {"wd" : keyword}
        r = requests.get(url, params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("链接未成功")
```

## 网络照片的爬取和储存

```python
import requests
import os

url = 'https://www.nationalgeographic.com/content/dam/animals/2020/07/glacier-bear/glacier-bear-111dscf0068.adapt.945.1.jpg'
root = "D://pics//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("链接失败")
```

