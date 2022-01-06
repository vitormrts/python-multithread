from time import perf_counter
import concurrent.futures

n = 10


def cpu_heavy(n):
    count = 0
    for i in range(10**8):
        count += 1


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for i in range(n):
        cpu_heavy(i)
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    start = perf_counter()
    executor = concurrent.futures.ThreadPoolExecutor()
    futures = []
    for i in range(n):
        futures.append(executor.submit(cpu_heavy, i))
    for future in futures:
        future.result()
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 5\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
