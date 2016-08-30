import time

def asyncMap(tasks, callback):
  count = 0
  results = []

  def anon(val):
    nonlocal count 

    results.append(val)
    count += 1
    if (count < len(tasks)):
      next()
    else:
      callback(results)

  def next():
    tasks[count]( anon )

  next()


def one(cb):
  time.sleep(0.3)
  cb('one'),

def two(cb):
  time.sleep(0.1)
  cb('two')
  

tasks = [ one, two ]

def lastCallback(results):
  print(results)

asyncMap(tasks, lastCallback)
