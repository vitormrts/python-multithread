from time import perf_counter, sleep, ctime, time
import threading

threads = []


def timer(name, delay, repeat):
    print(name + " Iniciou")

    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print(name + " Terminou")


start = perf_counter()
for i in range(5):
    timer(f"Timer {str(i)}", i, 2)

end = perf_counter()
print("Tempo total SEM threads: ", end - start)

start = perf_counter()

for i in range(5):
    t = threading.Thread(target=timer, args=(f"Timer {str(i)}", i, 2))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = perf_counter()
print("Tempo total COM threads: ", end - start)
