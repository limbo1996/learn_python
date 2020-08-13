# Beautiful soup

用来解析`requests`库爬取返回地对象

```python
import requests
from bs4 import BeautifulSoup 

url = "http://python123.io/ws/demo.html"

r = requests.get(url)

demo = r.text

soup = BeautifulSoup(demo, "html.parser")# 选择解析方式，在初始化时就可以完成对不完整的HTML的修正补全

print(soup.prettify()) # 可以以更好阅读的方式输出HTML
```

```HTML
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```

以更加清楚的方式返回了爬取的网页源代码

## HTML格式

`html`就是各种标签对, 例如

> `<p></p>`

每个标签有一对，不同标签代表了不同意思

### 遍历标签

分为三种

* 上行遍历
* 下行遍历
* 平行遍历

```python
# 遍历标签
# 遍历子节点
# 
soup = BeautifulSoup(demo, "html.parser")

soup.head

soup.head.contents
soup.body.contents

for i in soup.body.children:
    print(i)

# 上行遍历
# .parent/.parents

soup.title.parent


# 平行遍历
soup.a.next_sibling
soup.a.next_sibling.next_sibling

soup.a.previous_sibling
```

### 格式化输出

`prettify`可以用来格式化输出

```python
soup.prettify()
print(soup.prettify())
```

```html
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```

### 节点选择器

#### 选择元素

```python
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error")


r = getHTML(url)

soup = BeautifulSoup(r, 'lxml')   # 在初始化时就可以完成对不完整的HTML字符串的修正

print(soup)
print(soup.prettify())
print(soup.title.string) # 输出title节点的字符串内容

print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p) # 选择的是第一个p标签，后面的没有选到
```

```html
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta content="text/html;charset=utf-8" http-equiv="content-type"/><meta content="IE=Edge" http-equiv="X-UA-Compatible"/><meta content="always" name="referrer"/><link href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/><title>百度一下，你就知道</title></head> <body link="#0000cc"> <div id="wrapper"> <div id="head"> <div class="head_wrapper"> <div class="s_form"> <div class="s_form_wrapper"> <div id="lg"> <img height="129" hidefocus="true" src="//www.baidu.com/img/bd_logo1.png" width="270"/> </div> <form action="//www.baidu.com/s" class="fm" id="form" name="f"> <input name="bdorz_come" type="hidden" value="1"/> <input name="ie" type="hidden" value="utf-8"/> <input name="f" type="hidden" value="8"/> <input name="rsv_bp" type="hidden" value="1"/> <input name="rsv_idx" type="hidden" value="1"/> <input name="tn" type="hidden" value="baidu"/><span class="bg s_ipt_wr"><input autocomplete="off" autofocus="" class="s_ipt" id="kw" maxlength="255" name="wd" value=""/></span><span class="bg s_btn_wr"><input class="bg s_btn" id="su" type="submit" value="百度一下"/></span> </form> </div> </div> <div id="u1"> <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a> <a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a> <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图</a> <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频</a> <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧</a> <noscript> <a class="lb" href="http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1" name="tj_login">登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品</a> </div> </div> </div> <div id="ftCon"> <div id="ftConw"> <p id="lh"> <a href="http://home.baidu.com">关于百度</a> <a href="http://ir.baidu.com">About Baidu</a> </p> <p id="cp">©2017 Baidu <a href="http://www.baidu.com/duty/">使用百度前必读</a>  <a class="cp-feedback" href="http://jianyi.baidu.com/">意见反馈</a> 京ICP证030173号  <img src="//www.baidu.com/img/gs.gif"/> </p> </div> </div> </div> </body> </html>

<!DOCTYPE html>
<!--STATUS OK-->
<html>
 <head>
  <meta content="text/html;charset=utf-8" http-equiv="content-type"/>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="always" name="referrer"/>
  <link href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/>
  <title>
   百度一下，你就知道
  </title>
 </head>
 <body link="#0000cc">
  <div id="wrapper">
   <div id="head">
    <div class="head_wrapper">
     <div class="s_form">
      <div class="s_form_wrapper">
       <div id="lg">
        <img height="129" hidefocus="true" src="//www.baidu.com/img/bd_logo1.png" width="270"/>
       </div>
       <form action="//www.baidu.com/s" class="fm" id="form" name="f">
        <input name="bdorz_come" type="hidden" value="1"/>
        <input name="ie" type="hidden" value="utf-8"/>
        <input name="f" type="hidden" value="8"/>
        <input name="rsv_bp" type="hidden" value="1"/>
        <input name="rsv_idx" type="hidden" value="1"/>
        <input name="tn" type="hidden" value="baidu"/>
        <span class="bg s_ipt_wr">
         <input autocomplete="off" autofocus="" class="s_ipt" id="kw" maxlength="255" name="wd" value=""/>
        </span>
        <span class="bg s_btn_wr">
         <input class="bg s_btn" id="su" type="submit" value="百度一下"/>
        </span>
       </form>
      </div>
     </div>
     <div id="u1">
      <a class="mnav" href="http://news.baidu.com" name="tj_trnews">
       新闻
      </a>
      <a class="mnav" href="http://www.hao123.com" name="tj_trhao123">
       hao123
      </a>
      <a class="mnav" href="http://map.baidu.com" name="tj_trmap">
       地图
      </a>
      <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">
       视频
      </a>
      <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">
       贴吧
      </a>
      <noscript>
       <a class="lb" href="http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1" name="tj_login">
        登录
       </a>
      </noscript>
      <script>
       document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');
      </script>
      <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">
       更多产品
      </a>
     </div>
    </div>
   </div>
   <div id="ftCon">
    <div id="ftConw">
     <p id="lh">
      <a href="http://home.baidu.com">
       关于百度
      </a>
      <a href="http://ir.baidu.com">
       About Baidu
      </a>
     </p>
     <p id="cp">
      ©2017 Baidu
      <a href="http://www.baidu.com/duty/">
       使用百度前必读
      </a>
      <a class="cp-feedback" href="http://jianyi.baidu.com/">
       意见反馈
      </a>
      京ICP证030173号
      <img src="//www.baidu.com/img/gs.gif"/>
     </p>
    </div>
   </div>
  </div>
 </body>
</html>

百度一下，你就知道
<title>百度一下，你就知道</title>
<class 'bs4.element.Tag'>
<head><meta content="text/html;charset=utf-8" http-equiv="content-type"/><meta content="IE=Edge" http-equiv="X-UA-Compatible"/><meta content="always" name="referrer"/><link href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/><title>百度一下，你就知道</title></head>
<p id="lh"> <a href="http://home.baidu.com">关于百度</a> <a href="http://ir.baidu.com">About Baidu</a> </p>
```

#### 提取信息

##### `string`

```python
print(soup.title.string) # 输出title节点的字符串内容
```

>  百度一下，你就知道

可以用来获取文本的值。

其他属性的值可以使用不同的方式来提取

###### 获取名称

可以用`name`属性获取节点的名称

```python
print(soup.title.name)
```

> title

###### 获取属性

一个节点可能有不同的属性使用`attrs`获取所有的属性

```python
print(soup.meta.attrs)
{'http-equiv': 'content-type', 'content': 'text/html;charset=utf-8'}
```

返回字典，于是可以用字典的方式访问键得到值

```python
print(soup.meta.attrs["http-equiv"])
content-type
```

当然这样有点繁琐，可以使用相对简介的方法

```python
print(soup.meta["http-equiv"])
content-type
```

可以直接使用标签名字加属性名称就可以返回值

##### 嵌套选择

```python
print(soup.head)
print(soup.head.title)
```

可以向下选择节点

输出

```html

<head><meta content="text/html;charset=utf-8" http-equiv="content-type"/><meta content="IE=Edge" http-equiv="X-UA-Compatible"/><meta content="always" name="referrer"/><link href="http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/><title>百度一下，你就知道</title></head>


<title>百度一下，你就知道</title>
```

#### 关联选择

即`子节点`,`父节点`,`兄弟节点`

###### 子节点和子孙节点

访问子节点可以调用`contents`属性

```python
print(soup.p.contents)
[' ', <a href="http://home.baidu.com">关于百度</a>, ' ', <a href="http://ir.baidu.com">About Baidu</a>, ' ']
```

列表中的每个元素都是`p`节点的直接节点。如果有孙子节点并不会单独列出来。

同样的可以使用`children`属性

```python
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
```

```python
<list_iterator object at 0x0000023A0B9DD9C8>
```

```python
0  
1 <a href="http://home.baidu.com">关于百度</a>
2  
3 <a href="http://ir.baidu.com">About Baidu</a>
4  
```

返回地是生成器类型

要得到所有的子孙节点，可以使用`descendants`属性

```python
print(soup.p.descendants)

for i, child in enumerate(soup.p.descendants):
    print(i, child)
    
<generator object Tag.descendants at 0x0000023A0B9DF248>

0  
1 <a href="http://home.baidu.com">关于百度</a>
2 关于百度
3  
4 <a href="http://ir.baidu.com">About Baidu</a>
5 About Baidu
6  
```

返回地依旧是生成器类型，返回节点可以看到所有的子孙节点都被单独列出来了

###### 父节点和祖先节点

想要获取某个节点的父节点，可以使用`parent`属性

先查看一下`a`节点

```python
print(soup.a)
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
```

查看其父节点

```python
print(soup.a.parent)
<div id="u1"> <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a> <a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a> <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图</a> <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频</a> <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧</a> <noscript> <a class="lb" href="http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1" name="tj_login">登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品</a> </div>
```

父节点是`div`，输出`div`的所有内容

调用所有的祖先节点可以使用`parents`属性

#### 提取信息

```python
print(soup.meta)
print(soup.meta.attrs["content"])
```

```python
<meta content="text/html;charset=utf-8" http-equiv="content-type"/>

text/html;charset=utf-8
```

```python
print(soup.title)
<title>百度一下，你就知道</title>

print(soup.title.string)
百度一下，你就知道
```

返回是单个节点时，可以直接使用`string`或者`attrs`获取内容。

当返回是多个节点的生成器，可以转换为list，或者构建循环来获取内容

#### 方法选择器

##### `find_all()`

用来查询所有符合条件的元素

```python
 print(soup.find_all(name='span'))
    
    
[<span class="bg s_ipt_wr"><input autocomplete="off" autofocus="" class="s_ipt" id="kw" maxlength="255" name="wd" value=""/></span>, <span class="bg s_btn_wr"><input class="bg s_btn" id="su" type="submit" value="百度一下"/></span>]
```

返回地是列表

```python
for span in soup.find_all(name='span'):
    for i in span.find_all(name='input'):
        print(i.attrs['value'])
```

```python

百度一下
```

##### `attrs`

```python
print(soup.find_all(attrs={'class':'mnav'}))


[<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>, <a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>, <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图</a>, <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频</a>, <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧</a>]
```

根据属性的值来筛选

##### `text`

使用`text`来匹配文本，可以是字符串或者正则表达式

```python
 print(soup.find_all(text=re.compile('百度')))
 
['百度一下，你就知道', '关于百度', '使用百度前必读']
```

除此之外还有`fand`方法，返回地是匹配的第一个元素