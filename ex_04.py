from time import perf_counter
import threading
import concurrent.futures
import math

primes = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    115280095190773,
    1099726899285419,
]


def is_prime(n):
    if n < 2:
        return f'{n} não é primo'
    if n == 2:
        return f'{n} é primo'
    if n % 2 == 0:
        return f'{n} não é primo'

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return f'{n} não é primo'
    return f'{n} é primo'


def without_threads():
    print("SEM THREADS")
    start = perf_counter()
    for prime in primes:
        print(is_prime(prime))
    end = perf_counter()
    print("Tempo total SEM threads: ", end - start)


def with_threads():
    print("COM THREADS")
    start = perf_counter()
    executor = concurrent.futures.ThreadPoolExecutor()
    futures = []
    for prime in primes:
        futures.append(executor.submit(is_prime, prime))
    for future in futures:
        print(future.result())
    end = perf_counter()
    print("Tempo total COM threads: ", end - start)


def main():
    print("\nExemplo 4\n")
    without_threads()
    print("\n==============================\n")
    with_threads()


if __name__ == "__main__":
    main()
