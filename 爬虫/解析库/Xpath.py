#实例
from lxml import etree
text = '''
<div>
<ul>
<li class ='item-0'><a href='link1.html'>first item</a></i>
<li class ='item-1'><a href='link2.html'>second item</a></i>
<li class ='item-inactive'><a href='link3.html'>third item</a></i>
<li class ='item-1'><a href='link4.html'>fourth item</a></i>
<li class ='item-0'><a href='link5.html'>fifth item</a>
</ul>
</div>
'''#最后一个li是没有封闭的，但是etree模块可以自动修正
html = etree.HTML(text)#使用HTML类进行初始化
result = etree.tostring(html)#修正，但是得到的是bytes类型
print(result.decode('utf-8'))#使用decode方法转化为str

#所有节点
#一般使用//开头的XPath规则来选取所有符合的节点
#例如
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//*')
print(result2)
#当然也可以指定节点名
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//li')
print(result2)
print(result2[0])
#------------------------------------------------
#子节点
#使用/或者//查找子节点或者子孙节点
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//li/a')#即选取的是所有li节点的所有a子节点
print(result2)

#此处的/选取的直接子节点，如果要获取所有的子孙节点则使用//
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//ul//a')#注意ul下是没有直接的a子节点的
print(result2)
#------------------------------------------------
#父节点
#父节点则使用..
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//a[@href="link4.html"]/../@class')#选取属性href为link4.html的a节点的父节点，并且找到它的属性
print(result2)
## 还有一种方式的parent::
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result2)#结果相同
#---------------------------------------------
#属性匹配
#使用符号@进行属性过滤
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//li[@class="item-0"]')
print(result2)
#---------------------------------------------
#文本获取
#只用Xpath中的text()方法获取节点中的文本
from lxml import etree
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode('utf-8')
result2 = html.xpath('//li[@class="item-0"]/a/text()')
print(result2)




