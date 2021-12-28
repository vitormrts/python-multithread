import requests
from time import perf_counter
import threading

threads = []


def get_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    img_name = url.split('/')[-1]
    with open(img_name, 'wb') as f:
        f.write(requests.get(url).content)
        print(f'{img_name} foi salvo')


start = perf_counter()

for i in range(5):
    get_cat()

end = perf_counter()
print("Tempo total SEM threads: ", end - start)

start = perf_counter()

for i in range(5):
    t = threading.Thread(target=get_cat)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = perf_counter()
print("Tempo total COM threads: ", end - start)
