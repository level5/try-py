import threading


count = 0
lock = threading.Lock()


def inc():
    global count
    with lock:
        count += 1


def work():
    for i in range(0, 100000):
        inc()


# 启动并执行线程
threads = [threading.Thread(target=work) for i in range(0, 5)]
for t in threads:
    t.start()
for t in threads:
    t.join()        # 当前线程block等待t结束
print("count is %s" % count)
