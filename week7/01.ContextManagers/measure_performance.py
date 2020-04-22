import time


class measure_performance:
    def __init__(self):
        self.index = 1

    def __enter__(self):
        self.start_time = time.time()
        self.current_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Finished for:  {time.time() - self.start_time}')
        return exc_type, exc_val, exc_tb

    def benchmark(self, message=None, restart=False):
        if message is None:
            message = f'Benchmark No.{self.index}'

        print(f'{message}: {time.time() - self.current_time}')

        if restart:
            self.current_time = time.time()
        self.index += 1


def main():
    with measure_performance() as p:
        time.sleep(1)
        p.benchmark('1st step')

        time.sleep(2)
        p.benchmark('2nd step', restart=True)

        time.sleep(3)
        p.benchmark()


if __name__ == '__main__':
    main()
