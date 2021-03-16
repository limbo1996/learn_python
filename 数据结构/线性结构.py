import time

time.time()
# 


# 
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
        
        
# 
def sumOfN2(n):
  start = time.time()
  theSum = (n * (n + 1)) / 2
  end = time.time()
  return theSum, end - start

for i in range(5):
  print("Sum is %d required %f seconds" 
        % sumOfN2(100000))
   
   
   
# Stack
from Stack import Stack
s = Stack()

print(s.isEmpty())
s.push(4)
s.push("dog")
print(s.peek())
s.pop()
s.peek()


