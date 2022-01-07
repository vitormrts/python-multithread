from time import perf_counter
import requests
import concurrent.futures

urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]


def page_exists(url, timeout=10):
    response = requests.get(url=url, timeout=timeout)
    status = "unknown"
    if response.status_code == 200:
        status = "OK"
    elif response.status_code == 404:
        status = "Não existe"
    return f'{url} - {status}'


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for url in urls:
        print(page_exists(url))
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    start = perf_counter()
    executor = concurrent.futures.ThreadPoolExecutor()
    futures = []
    for url in urls:
        futures.append(executor.submit(page_exists, url))
    for future in futures:
        print(future.result())
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 3\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
