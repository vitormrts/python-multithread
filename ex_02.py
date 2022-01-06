import requests
from time import perf_counter
import threading
import os
import pathlib


n = 5

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'cats')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


def get_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    img_name = url.split('/')[-1]
    with open(f'{final_directory}/{img_name}', 'wb') as f:
        f.write(requests.get(url).content)
        print(f'{img_name} foi salvo')


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for i in range(n):
        get_cat()
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    threads = []
    start = perf_counter()
    for i in range(n):
        t = threading.Thread(target=get_cat)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 2\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
