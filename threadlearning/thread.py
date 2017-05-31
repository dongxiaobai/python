import concurrent.futures
import urllib.request

URLS = ['Fox News',
        'CNN - Breaking News, U.S., World, Weather, Entertainment & Video News',
        'http://europe.wsj.com/',
        'BBC - Home',
        'http://some-made-up-domain.com/']

# 获取一个单页，同时报告URL和内容
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# 我们通过with语句来确保线程能够被及时地清理，
# 这边max_workers=5，表示最多同时有5个线程去执行
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 字典生成器,使用的方法是`executor.submit()`
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    '''
    字典生成器用for循环实现的话，如下
    future_to_url = {}
    for url in URLS:
        future = executor.submit(load_url, url, 60)
        future_to_url[future] = url
    '''
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        # 这边的future就是 通过`Executor.submit()`函数来创建的。
        #有以下常用方法方法
        # future.result(),返回由相关回调产生的结果，在本案列中，返回函数`load_url`的结果
        # future.exception() 返回由相关回调抛出的异常，如果没有异常则返回`None`
        # 更多future对象介绍请看下文
        if future.exception() is not None:
            print('%r generated an exception: %s' % (url,future.exception()))
        else:
            print('%r page is %d bytes' % (url, len(future.result())))