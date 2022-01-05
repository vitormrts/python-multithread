from time import perf_counter, sleep, ctime, time
import threading

n = 5


def timer(name, delay, repeat):
    print(name + " Iniciou")

    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print(name + " Terminou")


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for i in range(n):
        timer(f"Timer {str(i)}", i, 2)
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    threads = []
    start = perf_counter()
    for i in range(n):
        t = threading.Thread(target=timer, args=(f"Timer {str(i)}", i, 2))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 3\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
