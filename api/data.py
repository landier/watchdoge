import redis
from tornado.options import define, options

define("redis_host", default="localhost", help="run on the given port", type=str)
define("redis_port", default=6379, help="run on the given port", type=int)

r = redis.Redis(host=options.redis_host, port=options.redis_port, db=0)
r.set('bing', 'baz')
print(r.get('bing'))