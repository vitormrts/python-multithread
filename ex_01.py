import threading
from time import sleep, perf_counter

threads = []


def wait(secs, name):
    print(f"Esperando por {name}")
    sleep(secs)
    print(f"{name} terminou")


start = perf_counter()

for i in range(20):
    wait(0.2, i+1)

end = perf_counter()
print("Tempo total SEM threads: ", end - start)

start = perf_counter()

for i in range(20):
    t = threading.Thread(target=wait, name=i+1, args=(0.2, i+1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = perf_counter()
print("Tempo total COM threads: ", end - start)
