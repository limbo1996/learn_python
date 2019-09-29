import requests
def get_one_page(url): #获取页面信息
        headers = {
            'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36(KHTML, like Gecko)Chrmoe/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()

#正则提取
import re
def parse_one_page(html):#分析第一页
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name".*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield{
            'index' : item[0],
            'image' : item[1],
            'title' : item[2],
            'actor' : item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score' : item[5] + item[6]
        }


