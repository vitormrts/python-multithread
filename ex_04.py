from time import perf_counter, sleep, ctime, time
import threading
from queue import Queue
import requests

threads = []

queue = Queue()


def get_url(queue, url):
    queue.put(requests.get(url))


urls = ["http://google.com", "http://yahoo.com",
        "http://bing.com", "http://amazon.com"]


start = perf_counter()

for url in urls:
    get_url(queue, url)

end = perf_counter()
print("Tempo total SEM threads: ", end - start)

start = perf_counter()

for url in urls:
    t = threading.Thread(target=get_url, args=(queue, url))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = perf_counter()
print("Tempo total COM threads: ", end - start)
