from asyncio import Queue

def do_stuff(q):
  while not q.empty():
    print(q.get())
    q.task_done()

q = Queue(maxsize=0)
print(q)
print(q.get())
for x in range(20):
  q.put(x)
  

do_stuff(q)