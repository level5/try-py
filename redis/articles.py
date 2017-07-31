# import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

# connection = redis.Redis()


def post_article(conn, user, title, link):
    article_id = str(conn.inc('article:'))

    voted = 'voted:{}'.format(article_id)
    conn.sadd(voted, user)
    # 使得发表的文章一周后过期，删除掉投票记录
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:{}'.format(article_id)
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1
    })

    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)


ARTICLES_PER_PAGE = 25


def get_articles(conn, page, order='score:'):
    """分页获取文章的信息"""
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    ids = conn.zrevrange(order, start, end)
    articles = []
    for article_id in ids:
        article_data = conn.hgetall(article_id)
        article_data['id'] = article_id
        articles.append(article_data)
    return articles


def article_vote(conn, user, article):
    """给对应的文章投票，文章必须是近一周内发表的才能投票。用户不能重复投票"""
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

    # 如果时间早于一周，不能再投票
    if conn.zscore('time:', article) < cutoff:
        return

    # 返回的是3个元素的一个tuple，(part_before_separator, separator, part_after_separator)
    article_id = article.partition(':')[-1]
    if conn.sadd('voted:{}'.format(article_id), user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)


def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    article = 'article:{}'.format(article_id)
    for group in to_add:
        conn.sadd('group:{}'.format(group), article)
    for group in to_remove:
        conn.srem('group:{}'.format(group), article)


def get_group_articles(conn, group, page, order='score:'):
    key = order + group
    if not conn.exists(key):
        conn.zinterstore(key, ['group:{}'.format(group), order], aggregate='max')
        conn.expire(key, 60)
    return get_articles(conn, page, key)

