import time
for i in range(1, 10):
  print('Hello world')
  time.sleep(1)

def hell():
  pass

def print():
  s = time.perf_counter()
  time.sleep(5)
  print(time.perf_counter()-s)
