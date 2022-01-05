from time import perf_counter, sleep, ctime, time
import threading
from queue import Queue
import requests


queue = Queue()


urls = ["http://google.com", "http://yahoo.com",
        "http://bing.com", "http://amazon.com"]


def get_url(queue, url):
    queue.put(requests.get(url))


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for url in urls:
        get_url(queue, url)
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    threads = []
    start = perf_counter()
    for url in urls:
        t = threading.Thread(target=get_url, args=(queue, url))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 4\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
