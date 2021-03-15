import requests

r = requests.get('https://search.jd.com/Search?keyword=ipad&enc=utf-8&wq=&pvid=1e8a937fe0c54ad686f61459ce1b6c28')


r.status_code

r.encoding

r.text



import time

time.time()
# 1970年1月1日开始，单位是秒


# 累计求和程序时间检测
def sumOfN(n):
  start = time.time()
  theSum = 0
  for i in range(1, n + 1):
    theSum = theSum + i
	
  end = time.time()
  return theSum, end - start


for i in range(5):
  print("Sum is %d required %f seconds" 
        % sumOfN(1000000))
        
        
        
        
# 无迭代算法
def sumOfN2(n):
  start = time.time()
  theSum = (n * (n + 1)) / 2
  end = time.time()
  return theSum, end - start

for i in range(5):
  print("Sum is %d required %f seconds" 
        % sumOfN2(100000))
    
