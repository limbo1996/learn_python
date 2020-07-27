# Beautiful soup

用来解析`requests`库爬取返回地对象

```python
import requests
from bs4 import BeautifulSoup 

url = "http://python123.io/ws/demo.html"

r = requests.get(url)

demo = r.text

soup = BeautifulSoup(demo, "html.parser")# 选择解析方式

print(soup.prettify())
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

