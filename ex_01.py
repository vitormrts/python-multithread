import threading
from time import sleep, perf_counter

n = 20


def wait(secs, name):
    print(f"Esperando por {name}")
    sleep(secs)
    print(f"{name} terminou")


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for i in range(n):
        wait(0.2, i+1)
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    threads = []
    start = perf_counter()
    for i in range(n):
        t = threading.Thread(target=wait, args=(0.2, i+1))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 1\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
