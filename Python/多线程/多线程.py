import time
import multiprocessing


def make_calculation():
    s = 0
    for j in range(2000000000000):
        s += j
    print('计算结果', s)


if __name__ == '__main__':
    start_time = time.time()
    # p1 = multiprocessing.Process(target=make_calculation)
    # p2 = multiprocessing.Process(target=make_calculation)
    # p3 = multiprocessing.Process(target=make_calculation)
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    ps = []
    for i in range(160):
        p = multiprocessing.Process(target=make_calculation)
        ps.append(p)
        p.start()
    for p in ps:
        p.join()
    print(f'完成，用时{time.time() - start_time:.2f}秒')
