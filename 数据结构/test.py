'''
该问题需要考虑的因素
1. 打印任务的属性：提交时间， 打印页数
2，打印队列的属性：打印任务队列
3. 打印机的属性：打印速度，是否忙
'''
from Queue import Queue
import random

class Printer:
  def __init__(self, ppm):
    self.pagerate = ppm # 打印速度
    self.currentTask = None # 打印任务
    self.timeRemaining = 0 # 打印时间倒计时
    
  def tick(self): # 打印1秒
    if self.currentTask != None:
      self.timeRemaining = self.timeRemaining - 1
      if self.timeRemaining <= 0:
        self.currentTask = None
        
  def busy(self):
    if self.currentTask != None:
      return True
    else:
      return False
    
  def startNext(self, newtask): # 打印新作业
    self.currentTask = newtask
    self.timeRemaining = newtask.getPages() * 60/self.pagerate # 页数除打印速度
  
  
class Task:
  def __init__(self, time):
    self.timestamp = time # 生成时间戳
    self.pages = random.randrange(1, 21) # 打印页数
    
  def getStamp(self):
    return self.timestamp
  
  def getPages(self):
    return self.pages
  
  def waitTime(self, currenttime):
    return currenttime - self.timestamp #等待时间 
 
 
  
def newPrintTask(): # 1/ 180的概率生成一个作业
  num = random.randrange(1, 181)
  if num == 180:
    return True
  else:
    return False
  
  
  
  
  
def simulation(numSeconds, pagesPerMinute):# 模拟多长时间和打印机模式
  
  labprinter = Printer(pagesPerMinute)
  printQueue = Queue()
  waitingtimes = []
  
  for currentSecond in range(numSeconds):
    
    if newPrintTask():
      task = Task(currentSecond)
      printQueue.enqueue(task)
    
    if (not labprinter.busy()) and (not printQueue.isEmpty()):
      nexttask = printQueue.dequeue() # 从等待队列中移除进入打印
      waitingtimes.append(nexttask.waitTime(currentSecond)) # 计算等待时间
      
      labprinter.startNext(nexttask)
    
    labprinter.tick()
  
  averageWait = sum(waitingtimes) / len(waitingtimes)
  
  print("Average Wait %f secs %d tasks remaining." % (averageWait, printQueue.size()))
  
  
  
  


for i in range(10):
  simulation(3600, 5)

 
    
