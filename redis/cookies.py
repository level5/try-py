import time


def check_token(conn, token):
    return conn.hget('login:', token)


def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)
        # 增加一行用来记录商品被访问的次数, 访问次数最多的将被放在最前面
        conn.zincrby('viewed:', item, -1)


def add_to_cart(conn, token, item, count):
    if count <= 0:
        conn.hrem('cart:' + token, item)
    else:
        conn.hset('cart:' + token, item, count)

QUIT = False
LIMIT = 10000000


def clean_session(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size < LIMIT:
            time.sleep(1)
            continue

        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange('recent:', 0, end_index - 1)

        conn.delete(*['viewed:' + token for token in tokens])
        conn.delete(*['cart:' + token for token in tokens])
        conn.hdel('login:', *tokens)
        conn.zrem('recent:', *tokens)


def rescale_viewed(conn):
    while not QUIT:
        conn.zremrangebyrank('viewed:', 0,  -20001)
        conn.zinterstore('viewed:', {'viewed:': 0.5})
        time.sleep(300)
